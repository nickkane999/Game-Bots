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
            "cycle_six": self.getCycleSix()
        } 
        self.cycle_rotation = [
            "cycle_two", 
            ["cycle_three", 2],
            ["cycle_four", 2],
            ["cycle_five", 7],
            ["cycle_one", 5],
        ] 
        
     #Reached boss 37 (blood unlocked)
    def getCycleFive(self):
        cycle_time = 420
        augment = "energy_buster"
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
                    ["digger", [True]]
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
                    ["time_machine", [5, "energy"]],
                ]
            },
            {
                "time": 120,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
                    ["select_gear", [self.gear["weapon"]]],
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
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
                    ["select_gear", [self.gear["accessory_2"], 1]],
                ],
                "order": [
                    "nuke",
                    "attack"
                ]
            },

        ]
        return [cycle_data, cycle_time]

    #Current cap is 116, time is around 10:00
    def getCycleOne(self):
        cycle_time = 600
        augment = "energy_buster"
        self.augment = "energy_buster"
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
                        ["augment", [10, self.augment]],
                        "nuke",
                        ["adventure", ["increment"]]
                    ]],
                    "reclaim",
                    ["time_machine", [10]]
                ]
            },
            {
                "time": 70,
                "pre_cycle": [
                    "reclaim",
                    ["augment", [3, self.augment, True]],
                    "reclaim",
                    ["augment", [3, self.augment]],
                    "reclaim",
                    ["digger", [True, "advemture"]]
                ],
                "order": [
                    "nuke",
                    ["time_machine", [10]],
                    ["once_delay", [4, [
                        ["select_gear_slot", ["resource_build"]],
                        "start_itopod"
                    ]]]
                ]
            },
            {
                "time": 20,
                "pre_cycle": [],
                "order": [
                    ["reclaim", [True]],
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 40,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5, "energy"]],
                ]
            },            
            {
                "time": 60,
                "pre_cycle": [],
                "order": [
                    ["reclaim", [True]],
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 10,
                "pre_cycle": [
                    ["select_gear", [self.gear["chest"]]],
                    ["select_gear", [self.gear["weapon"]]]
                ],
                "order": [
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 75,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5, "energy"]],
                ]
            },
            {
                "time": 80,
                "pre_cycle": [],
                "order": [
                    "reclaim",
                    ["augment", [8, self.augment, True]],
                    "reclaim",
                    ["augment", [8, self.augment]],
                    ["blood", ["blood_5"]],
                    "nuke",
                ]
            },
            {
                "time": 130,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
                    ["select_gear", [self.gear["weapon"]]],
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

    #Current cap is unknown, EST time is 7:00
    def getCycleSix(self):
        cycle_time = 420
        augment = "energy_buster"
        self.augment = "energy_buster"
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
                "time": 50,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        "adventure",
                        ["augment", [4, self.augment]],
                        "nuke",
                        ["adventure", ["increment"]]
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
                    ["augment", [2, self.augment, True]],
                    "reclaim",
                    ["augment", [3, self.augment]],
                    "reclaim",
                ],
                "order": [
                    "nuke",
                    ["time_machine", [8]],
                    ["once_delay", [2, [
                        ["select_gear_slot", ["resource_build"]],
                        "start_itopod"
                    ]]]
                ]
            },
            {
                "time": 30,
                "pre_cycle": [],
                "order": [
                    ["reclaim", [True]],
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 40,
                "pre_cycle": [
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5, "energy"]],
                ]
            },    
            {
                "time": 30,
                "pre_cycle": [],
                "order": [
                    ["reclaim", [True]],
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 20,
                "pre_cycle": [
                    ["select_gear", [self.gear["chest"]]],
                    ["select_gear", [self.gear["weapon"]]],
                    ["reclaim", [True]],
                    "spell_swap"
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    ["time_machine", [10, "energy"]],
                    "nuke"
                ]
            },
            {
                "time": 40,
                "pre_cycle": [],
                "order": [
                    ["blood", ["blood_5"]],
                    "reclaim",
                    ["augment", [2, self.augment, True]],
                    "reclaim",
                    ["augment", [8, self.augment]],
                    "nuke",
                ]
            },
            {
                "time": 100,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["head"]]],
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
                    ["select_gear", [self.gear["head"]]],
                    ["select_gear", [self.gear["weapon"]]],
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
