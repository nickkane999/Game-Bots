class Zones:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.data = self.getZones()

    # Major object functions
    def getZones(self):
        zones = {
            "battle": {
                "layer": 0,
                "icons": {
                    "town": {"x": 1840, "y": 190},
                    "map": {"x": 1840, "y": 320},
                    "party": {"x": 1840, "y": 420},
                    "upgrades": {"x": 1840, "y": 560},
                    "bag": {"x": 1840, "y": 690},
                    "fellowship": {"x": 1840, "y": 830},
                    "auto_spell": {"x": 700, "y": 1020},
                    "spell_1": {"x": 800, "y": 1020},
                    "spell_2": {"x": 900, "y": 1020},
                    "spell_3": {"x": 1000, "y": 690},
                    "daily_reward": {"x": 1830, "y": 1000},
                    "upgrade_1": {"x": 1720, "y": 200},
                    "upgrade_2": {"x": 1720, "y": 320},
                    "upgrade_3": {"x": 1720, "y": 440},
                    "upgrade_4": {"x": 1720, "y": 560},
                    "upgrade_5": {"x": 1720, "y": 680},
                    "upgrade_6": {"x": 1720, "y": 800},
                    "upgrade_7": {"x": 1720, "y": 920},
                    "profile": {"x": 100, "y": 100},
                    "upgrades_amount": {"x": 1600, "y": 1000},
                    "upgrades_x_icon": {"x": 1875, "y": 100},
                    "settings": {"x": 1830, "y": 60},
                    "achievement_close": {"x": 1380, "y": 880},
                }
            },
            "town": {
                "layer": 1,
                "icons": {
                    "temple": {"x": 960, "y": 250},
                    "magic_quarter": {"x": 630, "y": 270},
                    "battles": {"x": 400, "y": 200},
                    "campaign_confirm": {"x": 750, "y": 540},
                    "hall_of_heros": {"x": 1840, "y": 560},
                    "library": {"x": 270, "y": 680},
                    "guild": {"x": 1500, "y": 200},
                    "tavern": {"x": 940, "y": 950},
                    "temple": {"x": 960, "y": 250},
                    "merchant": {"x": 1460, "y": 660},
                    "x_icon": {"x": 1840, "y": 60},
                }
            },
            "party": {
                "layer": 1,
                "icons": {
                    "column1_row1": {"x": 1500, "y": 200},
                    "column2_row1": {"x": 1670, "y": 200},
                    "party_1": {"x": 800, "y": 810},
                    "party_2": {"x": 770, "y": 560},
                    "party_3": {"x": 570, "y": 860},
                    "party_4": {"x": 545, "y": 470},
                    "party_5": {"x": 500, "y": 640},
                    "choose_leader": {"x": 880, "y": 100},
                    "x_icon": {"x": 1840, "y": 60},
                    "save_icon": {"x": 1130, "y": 90},
                }
            },
            "guild": {
                "layer": 2,
                "icons": {
                    "expeditions": {"x": 260, "y": 390},
                    "expedition_1": {"x": 1360, "y": 330},
                    "expedition_ok": {"x": 1200, "y": 700},
                    "expedition_x_icon": {"x": 1500, "y": 70},
                    "x_icon": {"x": 1840, "y": 60},
                }
            },
            "library": {
                "layer": 2,
                "icons": {
                    "firestone": {"x": 1820, "y": 1000},
                    "meteorite": {"x": 1600, "y": 1000},
                    "tier_1_firestone": {
                        "firestone_damage": {"x": 400, "y": 560},
                        "firestone_health": {"x": 900, "y": 420},
                        "firestone_armor": {"x": 900, "y": 700},
                        "firestone_fist": {"x": 1400, "y": 300},
                        "firestone_guardian": {"x": 1400, "y": 560},
                        "firestone_projectiles": {"x": 1400, "y": 820},
                        "firestone_gold": {"x": 1840, "y": 560},
                        "firestone_training": {"x": 1200, "y": 300},
                        "firestone_wave": {"x": 1200, "y": 560},
                        "firestone_mission_planning": {"x": 1200, "y": 800},
                        "firestone_honor": {"x": 700, "y": 420},
                        "firestone_prestigious": {"x": 700, "y": 700},
                        "firestone_weak_enemy": {"x": 100, "y": 420},
                        "firestone_weak_boss": {"x": 100, "y": 700},
                        "firestone_loot_chance": {"x": 100, "y": 700},
                        "firestone_loot_bonus": {"x": 100, "y": 420},
                    },
                    "research_start": {"x": 800, "y": 790},
                    "x_icon": {"x": 1840, "y": 60},
                }
            },
            "map": {
                "layer": 1,
                "icons": {
                    "claim_slot_1": {"x": 160, "y": 310},
                    "claim_slot_2": {"x": 160, "y": 460},
                    "claim_slot_3": {"x": 160, "y": 620},
                    "claim_ok_side": {"x": 950, "y": 470},
                    "claim_ok": {"x": 950, "y": 620},
                    "empty_space": {"x": 20, "y": 1000},
                    "start_ok": {"x": 960, "y": 960},
                    "x_icon": {"x": 1840, "y": 60},
                }
            },
            "campaign": {
                "layer": 1,
                "icons": {
                    "claim_reward": {"x": 150, "y": 1000},
                    "daily_mission": {"x": 1780, "y": 1020},
                    "empty_space": {"x": 20, "y": 1000},
                    "start_ok": {"x": 960, "y": 960},
                    "battle_ok": {"x": 960, "y": 770},
                    "x_icon": {"x": 1840, "y": 60},
                    "daily_main_x_icon": {"x": 1510, "y": 90},
                    "daily_liberation_x_icon": {"x": 1820, "y": 60},
                    "campaign_daily_start": {"x": 1790, "y": 1020},
                    "campaign_daily_liberation_open": {"x": 680, "y": 850},
                    "daily_missions": {
                        "mission_set_1": {
                            "mission_1": {"x": 280, "y": 790},
                            "mission_2": {"x": 700, "y": 790},
                            "mission_3": {"x": 1120, "y": 790},
                            "mission_4": {"x": 1560, "y": 790},
                        },
                    }
                }
            },
            "tavern": {
                "layer": 2,
                "icons": {
                    "tavern_play_buy": {"x": 970, "y": 1000},
                    "buy_tokens": {"x": 420, "y": 800},
                    "card_1": {"x": 550, "y": 700},
                    "x_icon": {"x": 1840, "y": 60},
                }
            },
            "startup_desktop_100_zoom": {
                "layer": 0,
                "icons": {
                    "loot_collect": {"x": 950, "y": 820},
                    "settings_icon": {"x": 1530, "y": 340},
                    "fullscreen_button": {"x": 1550, "y": 510},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "startup_laptop_100_zoom": {
                "layer": 0,
                "icons": {
                    "loot_collect": {"x": 975, "y": 980},
                    "settings_icon": {"x": 1640, "y": 420},
                    "fullscreen_button": {"x": 1600, "y": 630},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "temple": {
                "layer": 2,
                "icons": {
                    "prestige_select": {"x": 1350, "y": 560},
                    "prestige_confirm": {"x": 1150, "y": 520},
                    "prestige_exit": {"x": 1840, "y": 50},
                    "firestone_tab": {"x": 1270, "y": 150},
                    "firetoken_tab": {"x": 1420, "y": 150},
                    "firetoken_magic_confirm": {"x": 1350, "y": 820},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "settings": {
                "layer": 1,
                "icons": {
                    "save_before_swap": {"x": 850, "y": 850},
                    "server_switch_start": {"x": 1800, "y": 630},
                    "server_1": {"x": 770, "y": 300},
                    "server_5": {"x": 1130, "y": 300},
                    "confirm_switch": {"x": 800, "y": 520},
                    "refresh_confirm": {"x": 1180, "y": 800},
                }
            },
            "magic_quarter": {
                "layer": 2,
                "icons": {
                    "train": {"x": 1130, "y": 819},
                    "guardian_1": {"x": 880, "y": 1000},
                    "guardian_2": {"x": 1030, "y": 1000},
                    "evolve_tab": {"x": 1340, "y": 160},
                    "train_tab": {"x": 1210, "y": 150},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "profile": {
                "layer": 1,
                "icons": {
                    "character": {"x": 1820, "y": 250},
                    "talents": {"x": 1820, "y": 430},
                    "achievements": {"x": 1820, "y": 600},
                    "statistics": {"x": 1820, "y": 780},
                    "quests": {"x": 1820, "y": 950},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "merchant": {
                "layer": 2,
                "icons": {
                    "Scroll of Speed": {"x": 1000, "y": 600},
                    "Scroll of Damage": {"x": 1310, "y": 600},
                    "Scroll of Health": {"x": 1620, "y": 600},
                    "Midas' Touch": {"x": 1000, "y": 940},
                    "Pouch of Gold": {"x": 1310, "y": 940},
                    "Bucket of Gold": {"x": 1620, "y": 940},
                    "Crate of Gold": {"x": 1000, "y": 600},
                    "Pile of Gold": {"x": 1310, "y": 600},
                    "War Banner": {"x": 1620, "y": 600},
                    "Dragon Armor": {"x": 1000, "y": 940},
                    "Guardian's Rune": {"x": 1310, "y": 940},
                    "Totem of Agony": {"x": 1620, "y": 940},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "shop": {
                "layer": 1,
                "icons": {
                    "daily_reward_tab": {"x": 160, "y": 870},
                    "daily_reward_claim": {"x": 1640, "y": 650},
                    "x_icon": {"x": 1840, "y": 50},
                }
            },
            "quests": {
                "layer": 1,
                "icons": {
                    "quest_1": {"x": 520, "y": 600},
                    "quest_2": {"x": 960, "y": 600},
                    "quest_3": {"x": 1400, "y": 600},
                    "quest_4": {"x": 520, "y": 960},
                    "quest_5": {"x": 960, "y": 960},
                    "quest_6": {"x": 1400, "y": 960},
                    "x_icon": {"x": 1840, "y": 50},
                }
            }
        }

        return zones
