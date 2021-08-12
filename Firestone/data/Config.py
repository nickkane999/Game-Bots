class Config:
    # Initializing Object
    def __init__(self):
        self.data = self.setDefaultConfigData()

    # Major object functions
    def setDefaultConfigData(self):
        data = {
            "server_1": {
                "firestone_progress": {
                    "current_tier": 1,
                    "options": {
                        "0": {
                            "name": "firestone_prestigious",
                            "current_level": 20,
                            "max_level": 20,
                            "completed": True,
                            "priority": 1,
                            "placement_area": 2,
                            "index": 0
                        },
                        "1": {
                            "name": "firestone_gold",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 2,
                            "placement_area": 1,
                            "index": 1
                        },
                        "2": {
                            "name": "firestone_training",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 3,
                            "placement_area": 2,
                            "index": 2
                        },
                        "3": {
                            "name": "firestone_wave",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 4,
                            "placement_area": 2,
                            "index": 3
                        },
                        "4": {
                            "name": "firestone_mission_planning",
                            "current_level": 20,
                            "max_level": 20,
                            "completed": True,
                            "priority": 5,
                            "placement_area": 2,
                            "index": 4
                        },
                        "5": {
                            "name": "firestone_honor",
                            "current_level": 12,
                            "max_level": 12,
                            "completed": True,
                            "priority": 6,
                            "placement_area": 2,
                            "index": 5
                        },
                        "6": {
                            "name": "firestone_damage",
                            "current_level": 35,
                            "max_level": 50,
                            "completed": False,
                            "priority": 7,
                            "placement_area": 1,
                            "index": 6
                        },
                        "7": {
                            "name": "firestone_projectiles",
                            "current_level": 30,
                            "max_level": 30,
                            "completed": True,
                            "priority": 8,
                            "placement_area": 1,
                            "index": 7
                        },
                        "8": {
                            "name": "firestone_fist",
                            "current_level": 6,
                            "max_level": 30,
                            "completed": False,
                            "priority": 9,
                            "placement_area": 1,
                            "index": 8
                        },
                        "9": {
                            "name": "firestone_guardian",
                            "current_level": 6,
                            "max_level": 30,
                            "completed": False,
                            "priority": 10,
                            "placement_area": 1,
                            "index": 9
                        },
                        "10": {
                            "name": "firestone_weak_enemy",
                            "current_level": 8,
                            "max_level": 15,
                            "completed": False,
                            "priority": 11,
                            "placement_area": 2,
                            "index": 10
                        },
                        "11": {
                            "name": "firestone_weak_boss",
                            "current_level": 8,
                            "max_level": 15,
                            "completed": False,
                            "priority": 12,
                            "placement_area": 2,
                            "index": 11
                        },
                        "12": {
                            "name": "firestone_armor",
                            "current_level": 4,
                            "max_level": 50,
                            "completed": False,
                            "priority": 13,
                            "placement_area": 1,
                            "index": 12
                        },
                        "13": {
                            "name": "firestone_health",
                            "current_level": 4,
                            "max_level": 50,
                            "completed": False,
                            "priority": 14,
                            "placement_area": 1,
                            "index": 13
                        },
                        "14": {
                            "name": "firestone_loot_chance",
                            "current_level": 4,
                            "max_level": 20,
                            "completed": False,
                            "priority": 15,
                            "placement_area": 3,
                            "index": 14
                        },
                        "15": {
                            "name": "firestone_loot_bonus",
                            "current_level": 4,
                            "max_level": 30,
                            "completed": False,
                            "priority": 16,
                            "placement_area": 3,
                            "index": 15
                        }
                    },
                    "upgrades_in_progress": {
                        "count": 0,
                        "items": []
                    }
                },
                "max_wave": 350,
            },
            "server_5": {
                "firestone_progress": {
                    "current_tier": 1,
                    "options": {
                        "0": {
                            "name": "firestone_prestigious",
                            "current_level": 20,
                            "max_level": 20,
                            "completed": True,
                            "priority": 1,
                            "placement_area": 2,
                            "index": 0
                        },
                        "1": {
                            "name": "firestone_gold",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 2,
                            "placement_area": 1,
                            "index": 1
                        },
                        "2": {
                            "name": "firestone_training",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 3,
                            "placement_area": 2,
                            "index": 2
                        },
                        "3": {
                            "name": "firestone_wave",
                            "current_level": 25,
                            "max_level": 25,
                            "completed": True,
                            "priority": 4,
                            "placement_area": 2,
                            "index": 3
                        },
                        "4": {
                            "name": "firestone_mission_planning",
                            "current_level": 20,
                            "max_level": 20,
                            "completed": True,
                            "priority": 5,
                            "placement_area": 2,
                            "index": 4
                        },
                        "5": {
                            "name": "firestone_honor",
                            "current_level": 12,
                            "max_level": 12,
                            "completed": True,
                            "priority": 6,
                            "placement_area": 2,
                            "index": 5
                        },
                        "6": {
                            "name": "firestone_damage",
                            "current_level": 44,
                            "max_level": 50,
                            "completed": False,
                            "priority": 7,
                            "placement_area": 1,
                            "index": 6
                        },
                        "7": {
                            "name": "firestone_projectiles",
                            "current_level": 27,
                            "max_level": 30,
                            "completed": False,
                            "priority": 8,
                            "placement_area": 1,
                            "index": 7
                        },
                        "8": {
                            "name": "firestone_fist",
                            "current_level": 4,
                            "max_level": 30,
                            "completed": False,
                            "priority": 9,
                            "placement_area": 1,
                            "index": 8
                        },
                        "9": {
                            "name": "firestone_guardian",
                            "current_level": 4,
                            "max_level": 30,
                            "completed": False,
                            "priority": 10,
                            "placement_area": 1,
                            "index": 9
                        },
                        "10": {
                            "name": "firestone_weak_enemy",
                            "current_level": 15,
                            "max_level": 15,
                            "completed": True,
                            "priority": 11,
                            "placement_area": 2,
                            "index": 10
                        },
                        "11": {
                            "name": "firestone_weak_boss",
                            "current_level": 15,
                            "max_level": 15,
                            "completed": True,
                            "priority": 12,
                            "placement_area": 2,
                            "index": 11
                        },
                        "12": {
                            "name": "firestone_armor",
                            "current_level": 4,
                            "max_level": 50,
                            "completed": False,
                            "priority": 13,
                            "placement_area": 1,
                            "index": 12
                        },
                        "13": {
                            "name": "firestone_health",
                            "current_level": 4,
                            "max_level": 50,
                            "completed": False,
                            "priority": 14,
                            "placement_area": 1,
                            "index": 13
                        },
                        "14": {
                            "name": "firestone_loot_chance",
                            "current_level": 4,
                            "max_level": 20,
                            "completed": False,
                            "priority": 15,
                            "placement_area": 3,
                            "index": 14
                        },
                        "15": {
                            "name": "firestone_loot_bonus",
                            "current_level": 5,
                            "max_level": 30,
                            "completed": False,
                            "priority": 16,
                            "placement_area": 3,
                            "index": 15
                        }
                    },
                    "upgrades_in_progress": {
                        "count": 0,
                        "items": ["firestone_damage"],
                        "shortest_queue": 0
                    }
                },
                "max_wave": 273
            },
            "general": {
                "current_server": "5",
                "save_time": 1628008100.8750913
            }
        }

        return data
