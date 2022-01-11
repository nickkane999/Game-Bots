from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import selenium
import time
import os
import glob
import shutil
from time import sleep
import json
import sys
import math
import win32gui



class Cycles:
    # Initializing Object
    def __init__(self):
        self.reset()

    def reset(self):
        self.cycles = {
            "cycle_one": self.getCycleOne(),
            "cycle_two": self.getCycleTwo(), 
            "cycle_three": self.getCycleThree(), 
            "cycle_four": self.getCycleFour(),
            "cycle_five": self.getCycleFive(),
            "cycle_six": self.getCycleSix(),
            "cycle_seven": self.getCycleSeven()
        }
        self.cycle_level = [
            ["cycle_six", 2],
            "cycle_one"
        ]
        self.cycle_rotation = [
            "cycle_two", 
            "cycle_three",
            "cycle_four",
            ["cycle_five", 5],
            ["cycle_one", 5],
        ] 
        
     #Reached boss 37 (blood unlocked)
    def getCycleFive(self):
        cycle_time = 420
        self.augment = "shoulder_mounted"
        blood_1 = "blood_1"
        blood_2 = "blood_2"
        blood_3 = "blood_3"
        blood_4 = "blood_4"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3,
            "accessory_2": 4
        }
        cycle_data = [
            {
                "time": 60,
                "pre_cycle": [
                    "scroll_augment"
                ],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        "adventure",
                        ["augment", [10, self.augment]],
                        "nuke",
                        ["adventure", ["increment"]]
                    ]],
                    "reclaim",
                    ["time_machine", [10]]
                ]
            },
            {
                "time": 50,
                "pre_cycle": [
                    "reclaim",
                    ["augment", [2, self.augment, True]],
                    "reclaim",
                    ["augment", [4, self.augment]],
                    "reclaim",
                    ["digger", [True]],
                    ["adventure", ["increment"]]
                ],
                "order": [
                    "nuke",
                    ["time_machine", [10]],
                    ["once_delay", [2, [
                        ["select_gear_slot", ["resource_build"]],
                        "start_itopod"
                    ]]]
                ]
            },
            {
                "time": 110,
                "pre_cycle": [],
                "order": [
                    ["reclaim", [True]],
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 80,
                "pre_cycle": [
                    ["reclaim", [True]]
                ],
                "order": [
                    ["blood", [blood_1]],
                    ["blood", [blood_2]],
                    ["blood", [blood_3]],
                    ["blood", [blood_4]],
                    "nuke",
                    ["time_machine", [5]],
                ]
            },
            {
                "time": 120,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    ["digger", [False]],
                    "start_itopod",
                    ["set_augment_reclaim_flag", [True]],   
                ],
                "order": [
                    ["wandos", [2]],
                    ["rotate", [
                        ["augment", [1, self.augment]],
                        ["augment", [1, self.augment, True]]
                    ]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    "apply_boost",
                    ["digger", [False]],
                    ["set_augment_reclaim_flag", [False]],
                    ["wandos", [1]],
                    "nuke",
                    "attack"
                ],
                "order": []
            },
        ]
        return [cycle_data, cycle_time]

    #Cycle 30 to 37
    def getCycleFour(self):
        cycle_time = 300
        augment_1 = "cannon_implant"
        augment_2 = "energy_buster"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3,
            "accessory_2": 4
        }
        cycle_data = [
            {
                "time": 60,
                "pre_cycle": [
                    "nuke",
                    "attack",
                    ["select_gear_slot", ["drop_rate_build"]],
                    "adventure"
                ],
                "order": [
                    "nuke",
                    ["wandos", [10]],
                    ["once_delay", [3, [
                       ["augment", [2, augment_1]]
                    ]]]
                ]
            },
            {
                "time": 80,
                "pre_cycle": [
                    "nuke",
                    "attack",
                    ["select_gear_slot", ["drop_rate_build"]],
                    "adventure"
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["time_machine", [10]],
                    "reclaim",
                    ["augment", [6, augment_1]],
                    "reclaim",
                    ["augment", [2, self.augment, True]],
                ]
            },
            {
                "time": 70,
                "pre_cycle": [
                    "nuke",
                    "attack",
                    ["select_gear_slot", ["drop_rate_build"]],
                    "adventure",
                    ["digger", [False]],
                    "reclaim",
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["augment", [2, self.augment, True]],
                    "reclaim",
                    ["augment", [6, augment_1]],
                ]
            },
            {
                "time": 80,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["wandos", [10]],
                    ["once_delay", [2, [
                       ["augment", [2, augment_2]]
                    ]]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    "reclaim",
                ],
                "order": [
                    "reclaim",
                    ["augment", [2, augment_2]],
                    ["augment", [2, augment_1]],
                    "nuke",
                    "attack"
                ]
            },

        ]
        return [cycle_data, cycle_time]

    #2nd cycle up to 30
    def getCycleThree(self):
        cycle_time = 300
        augment_1 = "milk"
        augment_2 = "cannon_implant"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3,
            "accessory_2": 4
        }
        cycle_data = [
            {
                "time": 90,
                "pre_cycle": [
                    "nuke",
                    "attack",
                    ["select_gear_slot", ["drop_rate_build"]],
                    "adventure"
                ],
                "order": [
                    "nuke",
                    ["wandos", [10]],
                    ["once_delay", [3, [
                       ["augment", [2, augment_1]]
                    ]]]
                ]
            },
            {
                "time": 210,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["wandos", [10]],
                    ["once_delay", [2, [
                       ["augment", [2, augment_2]]
                    ]]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    "reclaim",
                ],
                "order": [
                    "reclaim",
                    ["augment", [2, augment_2]],
                    ["augment", [2, augment_1]],
                    "nuke",
                    "attack"
                ]
            },

        ]
        return [cycle_data, cycle_time]

    #Start boss is 1
    def getCycleTwo(self):
        cycle_time = 300
        augment_1 = "scissors"
        augment_2 = "milk"
        augment_3 = "cannon_implant"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3,
            "accessory_2": 4
        }
        cycle_data = [
            {
                "time": 90,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                ],
                "order": [
                    "nuke",
                    ["wandos", [10]],
                ]
            },
            {
                "time": 20,
                "pre_cycle": [
                    "adventure",
                    ["select_gear_slot", ["drop_rate_build"]],
                    "attack"
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["wandos", [10]],
                    ["augment", [2, augment_1]],
                ]
            },
            {
                "time": 40,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                ],
                "order": [
                    "nuke",
                    "reclaim",
                    ["wandos", [10]],
                    ["once_delay", [1, [
                       ["augment", [2, augment_2]]
                    ]]]
                ]
            },
            {
                "time": 140,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    "reclaim",
                    ["wandos", [10]],
                    ["augment", [2, augment_3]],
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                ],
                "order": [
                    "nuke",
                    "attack"
                ]
            },

        ]
        return [cycle_data, cycle_time]

    #Current cap is around 130, time is around 10:00
    def getCycleOne(self):
        cycle_time = 600
        augment = "shoulder_mounted"
        self.augment = "shoulder_mounted"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3,
            "accessory_2": 4
        }
        self.bood_type = "blood_5"
        cycle_data = [
            {
                "time": 60,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        "adventure",
                        ["augment", [4, self.augment]],
                        "nuke"
                    ]],
                    "reclaim",
                    ["time_machine", [10]],
                    ["once_delay", [3, [
                        ["digger", [True, "advemture"]],
                        "adventure"
                    ]]]
                ]
            },
            {
                "time": 70,
                "pre_cycle": [
                    "reclaim",
                    ["augment", [3, self.augment, True]],
                    "reclaim",
                    ["augment", [3, self.augment]],
                    "reclaim"
                ],
                "order": [
                    "nuke",
                    ["time_machine", [10]]
                ]
            },
            {
                "time": 20,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                    "start_itopod"
                ],
                "order": [
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 30,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5]]
                ]
            },            
            {
                "time": 60,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    ["blood", ["blood_4"]],
                    ["time_machine", [10, "energy"]],
                    "nuke"
                ]
            },
            {
                "time": 10,
                "pre_cycle": [],
                "order": [
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 75,
                "pre_cycle": [],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5, "energy"]]
                ]
            },
            {
                "time": 80,
                "pre_cycle": [],
                "order": [
                    "reclaim",
                    ["augment", [12, self.augment, True]],
                    "reclaim",
                    ["augment", [8, self.augment]],
                    ["blood", ["blood_5"]],
                    "nuke"
                ]
            },
            {
                "time": 130,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    ["digger", [False]],
                    "start_itopod",
                    ["set_augment_reclaim_flag", [True]]
                ],
                "order": [
                    ["wandos", [2]],
                    ["blood", ["blood_5"]],
                    ["rotate", [
                        ["augment", [1, self.augment]],
                        ["augment", [1, self.augment, True]]
                    ]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                    "apply_boost",
                    ["digger", [False]],
                    ["set_augment_reclaim_flag", [False]],
                    ["wandos", [1]],
                    "nuke",
                    "attack"
                ],
                "order": []
            },
        ]
        return [cycle_data, cycle_time]

    #Current cap is around 107, EST time is 7:00
    def getCycleSix(self):
        cycle_time = 420
        augment = "energy_buster"
        self.augment = "energy_buster"
        self.gear = {
            "accessory": 0,
            "accessory_2": 1,
            "weapon": 2
        }
        self.bood_type = "blood_5"
        cycle_data = [
            {
                "time": 50,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        ["adventure", ["increment", [14, 0]]],
                        ["augment", [4, self.augment]],
                        "nuke",
                        ["adventure", ["increment", [2, 0]]]
                    ]],
                    "reclaim",
                    ["time_machine", [6]],
                    ["once_delay", [2, [
                        ["digger", [True, "advemture"]]
                    ]]]
                ]
            },
            {
                "time": 40,
                "pre_cycle": [
                    "reclaim",
                    ["augment", [4, self.augment, True]],
                    "reclaim",
                    ["augment", [3, self.augment]],
                    "reclaim"
                ],
                "order": [
                    "nuke",
                    ["time_machine", [8]],
                    ["once", [
                        ["select_gear_slot", ["resource_build"]],
                        "start_itopod",
                        ["reclaim", [True]]
                    ]]
                ]
            },
            {
                "time": 30,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap",
                    ["reclaim", [True]]
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [8]],
                    "reclaim",
                    ["augment", [4, self.augment, True]],
                    "reclaim",
                    ["augment", [1, self.augment]]
                ]
            },    
            {
                "time": 50,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_6"]],
                    ["blood", ["blood_5"]],
                    ["blood", ["blood_4"]],
                    ["time_machine", [10, "energy"]],
                    ["once_delay", [1, [
                        ["reclaim", [True]],
                        ["blood", ["blood_6"]],
                        ["blood", ["blood_5"]],
                        ["blood", ["blood_4"]],
                        ["blood", ["blood_3"]],
                        ["blood", ["blood_2"]],
                        ["blood", ["blood_1"]],
                        ["time_machine", [2]]
                    ]]],
                    "nuke"
                ]
            },
            {
                "time": 50,
                "pre_cycle": [],
                "order": [
                    ["blood", ["blood_6"]],
                    ["blood", ["blood_5"]],
                    ["once", [
                        ["reclaim", [True]],
                        "reclaim",
                        ["select_gear_slot", ["augment_build"]],
                        "start_itopod",
                        ["time_machine", [1, "magic"]]
                    ]],
                    "reclaim",
                    ["augment", [9, self.augment, True]],
                    "reclaim",
                    ["augment", [1, self.augment]],
                    "nuke"
                ]
            },
            {
                "time": 150,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["digger", [False]],
                    "start_itopod",
                    ["set_augment_reclaim_flag", [True]]
                ],
                "order": [
                    ["wandos", [2]],
                    ["blood", ["blood_6"]],
                    ["blood", ["blood_5"]],
                    ["rotate", [
                        ["augment", [1, self.augment]],
                        ["augment", [1, self.augment, True]]
                    ]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["accessory"]]],
                    "apply_boost",
                    ["digger", [False]],
                    ["set_augment_reclaim_flag", [False]],
                    ["wandos", [1]],
                    ["augment", [1, self.augment, True]],
                    "nuke",
                    "attack"
                ],
                "order": []
            },
        ]
        return [cycle_data, cycle_time]


    #Current cap is around 107, EST time is 7:00
    def getCycleSeven(self):
        cycle_time = 300
        self.augment = "energy_buster"
        self.gear = {
            "accessory": 0,
            "accessory_2": 1,
            "weapon": 2
        }
        cycle_data = [
            {
                "time": 45,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        ["adventure", ["increment", [14, 0]]],
                        ["augment_set", [self.augment, 100000000, "add", 0, "add"]],
                        "nuke",
                        ["adventure", ["increment", [2, 0]]]
                    ]],
                    ["time_machine_set", [15000000, "add", 200000000, "add"]],
                    ["augment_set", [self.augment, 30000000, "add", 10000000, "add"]],
                ]
            },
            {
                "time": 45,
                "pre_cycle": [
                    "nuke",
                    ["select_gear_slot", ["resource_build"]],
                    "start_itopod",
                    ["time_machine_set", [10000000, "add", 2000000000, "remove"]],
                    "spell_swap",
                    ["blood", ["blood_1"]],
                    ["blood", ["blood_2"]],
                    ["blood", ["blood_3"]],
                    ["blood", ["blood_4"]],
                    ["blood", ["blood_5"]],
                    ["blood", ["blood_6"]]
                ],
                "order": [
                    ["time_machine_set", [14000000, "add", 2000000000, "add"]],
                    ["augment_set", [self.augment, 25000000, "add", 15000000, "add"]]
                ]
            },
            {
                "time": 90,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["digger", [False]],
                    "start_itopod",
                    "nuke",
                    ["blood", ["blood_1"]],
                    ["blood", ["blood_2"]],
                    ["blood", ["blood_3"]],
                    ["blood", ["blood_4"]],
                    ["blood", ["blood_5"]],
                    ["blood", ["blood_6"]],
                    "spell_swap",
                    ["time_machine_set", [10000000, "add", 2000000000, "remove"]]
                ],
                "order": [
                    ["time_machine_set", [5000000, "add", 2000000000, "add"]],
                    ["augment_set", [self.augment, 25000000, "add", 15000000, "add"]]
                ]
            },
            {
                "time": 80,
                "pre_cycle": [],
                "order": [
                    ["once", [
                        ["reclaim", [True]],
                        ["digger", [False]],
                        "reclaim",
                        ["select_gear_slot", ["augment_build"]],
                        "start_itopod",
                        ["wandos", [2]],
                        ["blood", ["blood_1"]],
                        ["blood", ["blood_2"]],
                        ["blood", ["blood_3"]],
                        ["blood", ["blood_4"]]
                    ]],
                    ["augment_set", [self.augment, 300000000, "add", 600000000, "add"]],
                    ["blood", ["blood_6"]],
                    ["blood", ["blood_5"]],
                    ["wandos", [2]],
                    ["blood", ["blood_7"]],
                    "nuke"
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    "apply_boost",
                    ["digger", [False]],
                    ["wandos", [1]],
                    ["augment_set", [self.augment, 0, "add", 30000000000000, "add"]],
                    "nuke",
                    "attack"
                ],
                "order": []
            },
        ]
        return [cycle_data, cycle_time]
