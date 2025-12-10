import search
import random
import math
import itertools


ids = ["111111111", "111111111"]


class RobotNavigationProblem(search.Problem):
    """This class implements a medical problem according to problem description file"""
    def __init__(self, initial):
        search.Problem.__init__(self, initial)

    def actions(self, state):
        """Return the valid actions that can be executed in the given state."""
        raise NotImplementedError 
    

    def result(self, state, action):
        """Return the state that results from executing the given action in the given state."""
        raise NotImplementedError 
    

    def goal_test(self, state):
        """Return True if the state is a goal state."""
        raise NotImplementedError 
    

    def h(self, node):
        """
        Heuristic function for A* search.
        Estimates the minimum number of moves needed to reach the goal.
        """
        raise NotImplementedError


def create_robot_navigation_problem(game):
    return RobotNavigationProblem(game)

def astar_search(problem, heuristic):
    raise NotImplementedError
