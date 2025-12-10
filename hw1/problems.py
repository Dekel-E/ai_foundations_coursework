
non_comp_problems = [
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 10, "robovac_battery_damage": 3,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 1, "robovac_battery_damage": 3,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 10, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {"robovac1": [(1,1)]},
        "charging_stations": [],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 10, "robovac_battery_damage": 3,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [],
        "uneven_floor": [(1,1), (1,2)],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 0, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [{"location": (0,0), "charge_amount": 7, "charge_wait": 1}],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 0, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [{"location": (0,0), "charge_amount": 2, "charge_wait": 1}],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'I', 'I'],
            ['P', 'I', 'D'],
            ['P', 'P', 'P']
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 0, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 10},
        "robovacs": {},
        "charging_stations": [{"location": (0,0), "charge_amount": 5, "charge_wait": 1}],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'I', 'I'],
            ['P', 'I', 'D'],
            ['P', 'P', 'P']
        ],
        "robot": {"starting_location": (0,0), "starting_moves_left": 0, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 3},
        "robovacs": {},
        "charging_stations": [{"location": (0,0), "charge_amount": 3, "charge_wait": 1},
                              {"location": (0,3), "charge_amount": 3, "charge_wait": 1}],
        "uneven_floor": [],
    },
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'D', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
        ],
        "robot": {"starting_location": (1,1), "starting_moves_left": 3, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 2, "maximum_moves_left_possible": 21},
        "robovacs": {"robovac1": [(2,1), (1,1), (1,2), (2,2)],
                     "robovac2": [(3,2), (3,3), (3,4)]},
        "charging_stations": [{"location": (0,0), "charge_amount": 3, "charge_wait": 1},
                              {"location": (0,3), "charge_amount": 10, "charge_wait": 3}],
        "uneven_floor": [(4,4), (3,4), (3,5)],
    },
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'I', 'I', 'P'],
            ['P', 'P', 'P', 'I', 'P', 'I'],
            ['P', 'P', 'I', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'I'],
            ['I', 'I', 'P', 'P', 'D', 'I'],
            ['P', 'P', 'P', 'I', 'P', 'P'],
        ],
        "robot": {"starting_location": (1,1), "starting_moves_left": 3, "robovac_battery_damage": 10,
                  "uneven_floor_penalty": 3, "maximum_moves_left_possible": 21},
        "robovacs": {"robovac1": [(2,1), (1,1), (1,2), (2,2)],
                     "robovac2": [(3,3), (3,4), (3,5)],
                     "robovac3": [(2,4)]},
        "charging_stations": [{"location": (0,0), "charge_amount": 3, "charge_wait": 1},
                              {"location": (0,3), "charge_amount": 10, "charge_wait": 3}],
        "uneven_floor": [(4,4), (3,4), (3,5)],
    },
    {
    "map": [
        [("D" if (i, j) == (24, 24) else
          "I" if (i % 7 == 0 and j % 9 == 0) else "P")
         for j in range(25)]
        for i in range(25)
    ],
    "robot": {
        "starting_location": [1, 1],
        "starting_moves_left": 50,
        "maximum_moves_left_possible": 100,
        "robovac_battery_damage": 2,
        "uneven_floor_penalty": 2
    },
    "robovacs": {
        "r1": [(5, j) for j in range(5, 20)],
        "r2": [(15, j) for j in range(5, 20)]
    },
    "charging_stations": [
        {"location": (0,12), "charge_amount": 40, "charge_wait": 3},
        {"location": (12,0), "charge_amount": 40, "charge_wait": 3},
        {"location": (20,20), "charge_amount": 40, "charge_wait": 3}
    ],
    "uneven_floor": [(i,j) for i in range(25) for j in range(25) if (i*j)%11==0],
},
{
    "map": [
    ["D" if (i, j) == (29, 29)
     else "P" if (i != 10 or j % 5 == 0)
     else "I"
     for j in range(30)]
    for i in range(30)
    ],
    "robot": {
        "starting_location": [0, 0],
        "starting_moves_left": 40,
        "maximum_moves_left_possible": 100,
        "robovac_battery_damage": 3,
        "uneven_floor_penalty": 3
    },
    "robovacs": {
        "r1": [(9, j) for j in range(30)],
        "r2": [(20, j) for j in range(5, 25)]
    },
    "charging_stations": [
        {"location": (5,5), "charge_amount": 30, "charge_wait": 4},
        {"location": (25,25), "charge_amount": 30, "charge_wait": 4}
    ],
    "uneven_floor": [(i,j) for i in range(30) for j in range(30) if (i+j)%13==0],
},
{
    "map": [
        [("D" if (i,j)==(29,29)
          else "I" if (5<=i<=7 and 5<=j<=24) or (15<=i<=17 and 0<=j<=19)
          else "P")
         for j in range(30)]
        for i in range(30)
    ],
    "robot": {
        "starting_location": [0,0],
        "starting_moves_left": 60,
        "maximum_moves_left_possible": 100,
        "robovac_battery_damage": 2,
        "uneven_floor_penalty": 2
    },
    "robovacs": {
        "r1": [(i, 29) for i in range(30)],
        "r2": [(i, 25) for i in range(30)]
    },
    "charging_stations": [
        {"location": (0,15), "charge_amount": 40, "charge_wait": 3},
        {"location": (20,25), "charge_amount": 40, "charge_wait": 3}
    ],
    "uneven_floor": [(i,j) for i in range(30) for j in range(30) if (i*j)%19==0],
},
{
    "map": [
        [("D" if (i,j)==(39,39)
          else "I" if (i==20 or j==20) and not (15<=i<=25 and 15<=j<=25)
          else "P")
         for j in range(40)]
        for i in range(40)
    ],
    "robot": {
        "starting_location": [0,0],
        "starting_moves_left": 80,
        "maximum_moves_left_possible": 120,
        "robovac_battery_damage": 4,
        "uneven_floor_penalty": 2
    },
    "robovacs": {
        "r1": [(i, 15) for i in range(20)],
        "r2": [(i, 25) for i in range(20)],
        "r3": [(19, j) for j in range(40)]
    },
    "charging_stations": [
        {"location": (10,10), "charge_amount": 50, "charge_wait": 4},
        {"location": (30,30), "charge_amount": 50, "charge_wait": 4}
    ],
    "uneven_floor": [(i,j) for i in range(40) for j in range(40) if (i+j)%17==0],
},
{
    "map": [
        [("D" if (i,j)==(49,49)
          else "I" if (10<=i<=12 and 10<=j<=20) or (30<=i<=35 and 5<=j<=10) or (20<=i<=25 and 35<=j<=45)
          else "P")
         for j in range(50)]
        for i in range(50)
    ],
    "robot": {
        "starting_location": [0,0],
        "starting_moves_left": 100,
        "maximum_moves_left_possible": 200,
        "robovac_battery_damage": 4,
        "uneven_floor_penalty": 3
    },
    "robovacs": {
        "r1": [(i, 25) for i in range(50)],
        "r2": [(26, j) for j in range(50)]
    },
    "charging_stations": [
        {"location": (5,5), "charge_amount": 60, "charge_wait": 8},
        {"location": (25,25), "charge_amount": 60, "charge_wait": 8},
        {"location": (45,45), "charge_amount": 60, "charge_wait": 8}
    ],
    "uneven_floor": [(i,j) for i in range(50) for j in range(50) if (i*j)%29==0],
}
]
