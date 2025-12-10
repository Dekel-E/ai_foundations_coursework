import search
from math import gcd
from functools import reduce
from collections import deque
import heapq

ids = ["111111111", "111111111"]


def lcm(a, b):
    """Calculate least common multiple of two numbers"""
    return a * b // gcd(a, b)


class RobotNavigationProblem(search.Problem):
    """Robot navigation problem with dynamic obstacles and charging stations"""
    
    def __init__(self, initial):
        """
        State: (robot_pos, battery, turn_mod, charging_cooldowns)
        - robot_pos: (x, y) tuple
        - battery: current battery level
        - turn_mod: turn number modulo period (tracks robovac positions cyclically)
        - charging_cooldowns: tuple of remaining cooldown times for each station
        """
        self.game = initial
        self._init_map_and_robot(initial)
        self._init_special_tiles(initial)
        self._init_robovacs(initial)
        self._init_charging_stations(initial)
        self._precompute_neighbors_and_costs()
        self._precompute_distances()
        
        initial_state = (self.start_pos, self.start_battery, 0, tuple(0 for _ in self.charging_stations))
        search.Problem.__init__(self, initial_state)
    
    def _init_map_and_robot(self, initial):
        """Initialize map and robot parameters."""
        self.map = initial["map"]
        self.rows = len(self.map)
        self.cols = len(self.map[0]) if self.rows > 0 else 0
        
        robot = initial["robot"]
        self.start_pos = tuple(robot["starting_location"])
        self.start_battery = robot["starting_moves_left"]
        self.max_battery = robot["maximum_moves_left_possible"]
        self.robovac_damage = robot["robovac_battery_damage"]
        self.uneven_penalty = robot["uneven_floor_penalty"]
    
    def _init_special_tiles(self, initial):
        """Find destination and uneven floor tiles."""
        self.destination = None
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] == 'D':
                    self.destination = (i, j)
                    break
        
        self.uneven_floor = set(tuple(p) for p in initial.get("uneven_floor", []))
    
    def _init_robovacs(self, initial):
        """Initialize robovac paths and compute oscillation period."""
        self.robovacs = initial.get("robovacs", {})
        self.robovac_list = list(self.robovacs.keys())
        self.robovac_paths = {name: [tuple(p) for p in path] for name, path in self.robovacs.items()}
        
        # the period is LCM of all oscillation periods
        periods = [max(1, 2 * (len(path) - 1)) for path in self.robovac_paths.values()]
        self.period = reduce(lcm, periods, 1) if periods else 1
        
        # precompute robovac positions for each turn
        self._robovac_cache = {}
        for turn in range(self.period):
            positions = tuple(self._get_robovac_pos_at_turn(name, turn) for name in self.robovac_list)
            self._robovac_cache[turn] = positions
        
        self.robovac_positions = set()
        for path in self.robovac_paths.values():
            self.robovac_positions.update(path)
    
    def _get_robovac_pos_at_turn(self, name, turn):
        """Get position of a robovac at given turn (oscillating motion)."""
        path = self.robovac_paths[name]
        if len(path) == 1:
            return path[0]
        
        period = 2 * (len(path) - 1)
        pos_in_cycle = turn % period
        return path[pos_in_cycle] if pos_in_cycle < len(path) else path[period - pos_in_cycle]
    
    def _init_charging_stations(self, initial):
        """Initialize charging stations."""
        self.charging_stations = initial.get("charging_stations", [])
        self._max_charge = max((s["charge_amount"] for s in self.charging_stations), default=0)
        self.station_locations = {tuple(s["location"]): i for i, s in enumerate(self.charging_stations)}
    
    def _precompute_neighbors_and_costs(self):
        """Cache valid neighbors and movement costs for all positions."""
        self._neighbors_cache = {}
        self._move_cost_cache = {}
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.map[i][j] == 'I':
                    continue
                
                pos = (i, j)
                neighbors = []
                
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.rows and 0 <= nj < self.cols and self.map[ni][nj] != 'I':
                        neighbor = (ni, nj)
                        neighbors.append(neighbor)
                        cost = self.uneven_penalty if (pos in self.uneven_floor or neighbor in self.uneven_floor) else 1
                        self._move_cost_cache[(pos, neighbor)] = cost
                
                self._neighbors_cache[pos] = neighbors
    
    def _precompute_distances(self):
        """Precompute minimum turns/battery to goal and nearest charger for heuristic/pruning."""
        passable = {(i, j) for i in range(self.rows) for j in range(self.cols) if self.map[i][j] != 'I'}
        
        # BFS for minimum turns to destination
        self.min_turns_to_goal = {pos: float('inf') for pos in passable}
        self.min_turns_to_goal[self.destination] = 0
        queue = deque([self.destination])
        
        while queue:
            pos = queue.popleft()
            for neighbor in self._neighbors_cache.get(pos, []):
                if self.min_turns_to_goal[neighbor] == float('inf'):
                    self.min_turns_to_goal[neighbor] = self.min_turns_to_goal[pos] + 1
                    queue.append(neighbor)
        
        # Dijkstra for minimum battery cost to destination
        self.min_battery_to_goal = {pos: float('inf') for pos in passable}
        self.min_battery_to_goal[self.destination] = 0
        pq = [(0, self.destination)]
        
        while pq:
            cost, pos = heapq.heappop(pq)
            if cost > self.min_battery_to_goal[pos]:
                continue
            for neighbor in self._neighbors_cache.get(pos, []):
                move_cost = self._move_cost_cache[(pos, neighbor)]
                new_cost = cost + move_cost
                if new_cost < self.min_battery_to_goal[neighbor]:
                    self.min_battery_to_goal[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        
        # Dijkstra for minimum battery cost to nearest charger
        self.min_battery_to_charger = {pos: float('inf') for pos in passable}
        pq = []
        for station in self.charging_stations:
            loc = tuple(station["location"])
            self.min_battery_to_charger[loc] = 0
            heapq.heappush(pq, (0, loc))
        
        while pq:
            cost, pos = heapq.heappop(pq)
            if cost > self.min_battery_to_charger[pos]:
                continue
            for neighbor in self._neighbors_cache.get(pos, []):
                move_cost = self._move_cost_cache[(pos, neighbor)]
                new_cost = cost + move_cost
                if new_cost < self.min_battery_to_charger[neighbor]:
                    self.min_battery_to_charger[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
    
    def get_neighbors(self, pos):
        """Get adjacent passable neighbors (cached)."""
        return self._neighbors_cache.get(pos, [])
    
    def get_move_cost(self, from_pos, to_pos):
        """Get battery cost for a move (cached)."""
        return self._move_cost_cache.get((from_pos, to_pos), 1)
    
    def count_robovacs_at(self, pos, turn_mod):
        """Count robovacs at position after turn_mod."""
        return self._robovac_cache[turn_mod].count(pos)
    
    def actions(self, state):
        """Return valid actions from current state."""
        robot_pos, battery, turn_mod, cooldowns = state
        
        if robot_pos == self.destination:
            return []
        
        # prune dead ends
        can_reach_goal = battery >= self.min_battery_to_goal.get(robot_pos, float('inf'))
        can_reach_charger = battery >= self.min_battery_to_charger.get(robot_pos, float('inf'))
        
        if not can_reach_goal and not can_reach_charger:
            return []
        
        valid_actions = []
        next_turn_mod = (turn_mod + 1) % self.period
        
        # check wait action
        if len(self.robovac_list) > 0 or any(cd > 0 for cd in cooldowns):
            robovac_damage = self.count_robovacs_at(robot_pos, next_turn_mod) * self.robovac_damage
            if battery >= robovac_damage:
                valid_actions.append(("wait",))
        
        # check charge action
        if robot_pos in self.station_locations:
            station_idx = self.station_locations[robot_pos]
            if cooldowns[station_idx] == 0:
                valid_actions.append(("charge",))
        
        # check move actions
        for neighbor in self.get_neighbors(robot_pos):
            move_cost = self.get_move_cost(robot_pos, neighbor)
            robovac_damage = self.count_robovacs_at(neighbor, next_turn_mod) * self.robovac_damage
            total_cost = move_cost + robovac_damage
            
            if battery >= total_cost:
                valid_actions.append(("move", neighbor))
        
        return valid_actions
    
    def result(self, state, action):
        """Return the state resulting from an action."""
        robot_pos, battery, turn_mod, cooldowns = state
        new_turn_mod = (turn_mod + 1) % self.period
        new_cooldowns = tuple(max(0, c - 1) for c in cooldowns)
        
        action_type = action[0]
        
        if action_type == "wait":
            robovac_damage = self.count_robovacs_at(robot_pos, new_turn_mod) * self.robovac_damage
            new_battery = battery - robovac_damage
            return (robot_pos, new_battery, new_turn_mod, new_cooldowns)
        
        elif action_type == "charge":
            station_idx = self.station_locations[robot_pos]
            station = self.charging_stations[station_idx]
            
            charge_amount = station["charge_amount"] if cooldowns[station_idx] == 0 else 0
            new_battery = min(battery + charge_amount, self.max_battery)
            
            if charge_amount > 0:
                cooldown_list = list(new_cooldowns)
                cooldown_list[station_idx] = station["charge_wait"]
                new_cooldowns = tuple(cooldown_list)
            
            robovac_damage = self.count_robovacs_at(robot_pos, new_turn_mod) * self.robovac_damage
            new_battery -= robovac_damage
            return (robot_pos, new_battery, new_turn_mod, new_cooldowns)
        
        elif action_type == "move":
            new_pos = action[1]
            move_cost = self.get_move_cost(robot_pos, new_pos)
            robovac_damage = self.count_robovacs_at(new_pos, new_turn_mod) * self.robovac_damage
            new_battery = battery - move_cost - robovac_damage
            return (new_pos, new_battery, new_turn_mod, new_cooldowns)
        
        return state
    
    def goal_test(self, state):
        """Check if state is goal state."""
        return state[0] == self.destination
    
    def h(self, node):
        """A* heuristic: minimum turns plus estimated charging needs."""
        robot_pos, battery, _, _ = node.state
        
        if robot_pos == self.destination:
            return 0
        
        min_turns = self.min_turns_to_goal.get(robot_pos, float('inf'))
        min_battery_needed = self.min_battery_to_goal.get(robot_pos, float('inf'))
        
        # can reach goal without charging
        if battery >= min_battery_needed:
            return min_turns
        
        # must charge
        if self._max_charge > 0:
            battery_deficit = min_battery_needed - battery
            min_charges = (battery_deficit + self._max_charge - 1) // self._max_charge
            return min_turns + min_charges
        
        return float('inf')


def create_robot_navigation_problem(game):
    """Factory function to create a RobotNavigationProblem"""
    return RobotNavigationProblem(game)


def astar_search(problem, heuristic):
    """A* search with state pruning and dominance checking"""
    def state_key(state):
        """Simplify state for dominance checking"""
        robot_pos, battery, turn_mod, cooldowns = state
        min_needed = problem.min_battery_to_goal.get(robot_pos, float('inf'))
        
        # Don't track cooldowns if we can reach goal
        if battery >= min_needed:
            cooldowns = ()
        
        # if not in robovac path, don't track turn_mod
        if robot_pos not in problem.robovac_positions:
            turn_mod = 0
        
        return (robot_pos, turn_mod, cooldowns)
    
    node = search.Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    
    frontier = [(heuristic(node), 0, node)]
    best_battery = {}
    counter = 0
    
    while frontier:
        _, _, node = heapq.heappop(frontier)
        state = node.state
        key = state_key(state)
        battery = state[1]
        
        # skip dominated states
        if key in best_battery and best_battery[key] >= battery:
            continue
        best_battery[key] = battery
        
        # goal check
        if problem.goal_test(state):
            return node
        
        # expand
        for action in problem.actions(state):
            child = node.child_node(problem, action)
            child_key = state_key(child.state)
            child_battery = child.state[1]
            
            if child_key not in best_battery or best_battery[child_key] < child_battery:
                f_value = child.path_cost + heuristic(child)
                counter += 1
                heapq.heappush(frontier, (f_value, counter, child))
    
    return None