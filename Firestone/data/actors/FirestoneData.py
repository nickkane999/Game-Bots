class FirestoneData:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.data = self.getFirestoneData()
        self.priority = self.getFirestoneSetPriority()

    # Major object functions
    def getFirestoneData(self):
        data = {
            "requirements": {
                "tier_1": {
                    "set_1": {
                        "firestone_damage": 10,
                    },
                    "set_2": {
                        "firestone_health": 4,
                        "firestone_armor": 4
                    },
                    "set_3": {
                        "firestone_fist": 4,
                        "firestone_guardian": 4,
                        "firestone_projectiles": 4
                    },
                    "set_4": {
                        "firestone_gold": 6,
                    },
                    "set_5": {
                        "firestone_loot_chance": 4,
                        "firestone_loot_bonus": 4
                    },
                    "set_6": {
                        "firestone_weak_enemy": 5,
                        "firestone_weak_boss": 5
                    },
                    "set_7": {
                        "firestone_honor": 8,
                        "firestone_prestigious": 8
                    },
                    "set_8": {
                        "firestone_health": 0,
                        "firestone_armor": 0
                    },
                },
                "tier_2": {
                    "set_1": {
                        "firestone_skip": 4,
                        "firestone_main_attribute": 4,
                        "firestone_prestigious": 4
                    },
                    "set_2": {
                        "firestone_enemy_dmg": 5,
                        "firestone_boss_dmg": 5
                    },
                    "set_3": {
                        "firestone_raining_gold": 6,
                    },
                    "set_4": {
                        "firestone_meteorite": 4,
                    },
                    "set_5": {
                        "firestone_damage": 5,
                        "firestone_enemy_health": 5
                    },
                    "set_6": {
                        "firestone_guardian": 6,
                        "firestone_boss_health": 5
                    },
                    "set_7": {
                        "firestone_health": 10,
                        "firestone_armor": 10
                    },
                    "set_8": {
                        "firestone_rage": 0,
                        "firestone_mana": 0,
                        "firestone_energy": 0
                    },
                }
            }
        }

        return data

    def getFirestoneSetPriority(self):
        set_order = [
            "set_8",
            "set_7",
            "set_6",
            "set_5",
            "set_4",
            "set_3",
            "set_2",
            "set_1"
        ]

        return set_order
