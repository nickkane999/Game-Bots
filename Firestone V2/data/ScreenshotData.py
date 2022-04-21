class ScreenshotData:
    # Initializing Object
    def __init__(self):
        self.data = self.getScreenshotData()

    # Major object functions
    def getScreenshotData(self):
        screenshot_data = {
            "merchant": self.getMerchantScreenshotData(),
            "multiple_rewards": self.getMultipleRewardsScreenshotData(),
            "single_reward": self.getSingleRewardScreenshotData(),
            "quests": self.getQuestScreenshotData(),
            "campaign": self.getCampaignScreenshotData(),
            "guild-expedition": self.getGuildExpeditionData(),
            # "map": self.getMapScreenshotData(),
            "missions": self.getMapMissionData(),
            "mission-claim": self.getMapMissionClaimData(),
            "alchemy-experiments": self.getAlchemyExperimentData(),
            "magic_quarter": self.getMagicQuarterData(),
        }

        return screenshot_data

    def getMerchantScreenshotData(self):
        regions = {
            "item_title_1": (860, 370, 270, 70),
            "item_title_2": (1180, 370, 270, 70),
            "item_title_3": (1500, 370, 270, 70),
            "item_title_4": (860, 710, 270, 70),
            "item_title_5": (1180, 710, 270, 70),
            "item_title_6": (1500, 710, 270, 70),
            "item_title_7": (860, 370, 270, 70),
            "item_title_8": (1180, 370, 270, 70),
            "item_title_9": (1500, 370, 270, 70),
            "item_title_10": (860, 710, 270, 70),
            "item_title_11": (1180, 710, 270, 70),
            "item_title_12": (1500, 710, 270, 70),
            "item_title_13": (860, 370, 270, 70),
            "item_quantity_1": (970, 470, 80, 80),
            "item_quantity_2": (1290, 470, 80, 80),
            "item_quantity_3": (1610, 470, 80, 80),
            "item_quantity_4": (970, 810, 80, 80),
            "item_quantity_5": (1290, 810, 80, 80),
            "item_quantity_6": (1610, 810, 80, 80),
            "item_quantity_7": (970, 470, 80, 80),
            "item_quantity_8": (1290, 470, 80, 80),
            "item_quantity_9": (1610, 470, 80, 80),
            "item_quantity_10": (970, 810, 80, 80),
            "item_quantity_11": (1290, 810, 80, 80),
            "item_quantity_12": (1610, 810, 80, 80),
            "item_quantity_13": (970, 470, 80, 80),
        }
        merchant_data = {
            "item_title_1": {
                "region": regions["item_title_1"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_1_title.png',
                "type": "merchant-title",
                "msg": "Item 1 title: ",
            },
            "item_quantity_1": {
                "region": regions["item_quantity_1"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_1_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 1 quantity: ",
            },
            "item_title_2": {
                "region": regions["item_title_2"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_2_title.png',
                "type": "merchant-title",
                "msg": "Item 2 title: ",
            },
            "item_quantity_2": {
                "region": regions["item_quantity_2"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_2_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 2 quantity: ",
            },
            "item_title_3": {
                "region": regions["item_title_3"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_3_title.png',
                "type": "merchant-title",
                "msg": "Item 3 title: ",
            },
            "item_quantity_3": {
                "region": regions["item_quantity_3"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_3_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 3 quantity: ",
            },
            "item_title_4": {
                "region": regions["item_title_4"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_4_title.png',
                "type": "merchant-title",
                "msg": "Item 4 title: ",
            },
            "item_quantity_4": {
                "region": regions["item_quantity_4"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_4_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 4 quantity: ",
            },
            "item_title_5": {
                "region": regions["item_title_5"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_5_title.png',
                "type": "merchant-title",
                "msg": "Item 5 title: ",
            },
            "item_quantity_5": {
                "region": regions["item_quantity_5"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_5_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 5 quantity: ",
            },
            "item_title_6": {
                "region": regions["item_title_6"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_6_title.png',
                "type": "merchant-title",
                "msg": "Item 6 title: ",
            },
            "item_quantity_6": {
                "region": regions["item_quantity_6"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_6_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 6 quantity: ",
            },
            "item_title_7": {
                "region": regions["item_title_7"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_7_title.png',
                "type": "merchant-title",
                "msg": "Item 7 title: ",
            },
            "item_quantity_7": {
                "region": regions["item_quantity_7"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_7_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 7 quantity: ",
            },
            "item_title_8": {
                "region": regions["item_title_8"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_8_title.png',
                "type": "merchant-title",
                "msg": "Item 8 title: ",
            },
            "item_quantity_8": {
                "region": regions["item_quantity_8"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_8_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 8 quantity: ",
            },
            "item_title_9": {
                "region": regions["item_title_9"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_9_title.png',
                "type": "merchant-title",
                "msg": "Item 9 title: ",
            },
            "item_quantity_9": {
                "region": regions["item_quantity_9"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_9_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 9 quantity: ",
            },
            "item_title_10": {
                "region": regions["item_title_10"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_10_title.png',
                "type": "merchant-title",
                "msg": "Item 10 title: ",
            },
            "item_quantity_10": {
                "region": regions["item_quantity_10"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_10_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 10 quantity: ",
            },
            "item_title_11": {
                "region": regions["item_title_11"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_11_title.png',
                "type": "merchant-title",
                "msg": "Item 11 title: ",
            },
            "item_quantity_11": {
                "region": regions["item_quantity_11"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_11_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 11 quantity: ",
            },
            "item_title_12": {
                "region": regions["item_title_12"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_12_title.png',
                "type": "merchant-title",
                "msg": "Item 12 title: ",
            },
            "item_quantity_12": {
                "region": regions["item_quantity_12"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_12_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item 12 quantity: ",
            },
            "item_title_13": {
                "region": regions["item_title_13"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_13_title.png',
                "type": "merchant-title",
                "msg": "Item 13 title: ",
            },
            "item_quantity_13": {
                "region": regions["item_quantity_13"],
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\merchant_items\item_13_quantity.png',
                "type": "merchant-quantity",
                "msg": "Item13 quantity: ",
            }
        }
        return merchant_data

    def getMultipleRewardsScreenshotData(self):
        multiple_rewards_data = {
            "quest_1_title_data": {
                "region": (350, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_1_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 1 title: ",
            },
            "quest_1_claim_data": {
                "region": (420, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_1_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 1 text: ",
            },
            "quest_2_title_data": {
                "region": (800, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_2_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 2 title: ",
            },
            "quest_2_claim_data": {
                "region": (870, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_2_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 2 text: ",
            },
            "quest_3_title_data": {
                "region": (1240, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_3_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 3 title: ",
            },
            "quest_3_claim_data": {
                "region": (1310, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_3_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 3 text: ",
            },
            "quest_4_title_data": {
                "region": (350, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_4_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 4 title: ",
            },
            "quest_4_claim_data": {
                "region": (420, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_4_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 4 text: ",
            },
            "quest_5_title_data": {
                "region": (800, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_5_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 5 title: ",
            },
            "quest_5_claim_data": {
                "region": (870, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_5_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 5 text: ",
            },
            "quest_6_title_data": {
                "region": (1240, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_6_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 6 title: ",
            },
            "quest_6_claim_data": {
                "region": (1310, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_6_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 6 text: ",
            },
        }
        return multiple_rewards_data

    def getSingleRewardScreenshotData(self):
        single_reward_data = {
            "daily_timer": {
                "region": (1550, 805, 200, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\daily_reset_timer.png',
                "type": "daily-reset",
                "msg": "Daily reset timer title: ",
            },
        }
        return single_reward_data

    def getQuestScreenshotData(self):
        quest_data = {
            "quest_1_title_data": {
                "region": (350, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_1_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 1 title: ",
            },
            "quest_1_claim_data": {
                "region": (420, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_1_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 1 text: ",
            },
            "quest_2_title_data": {
                "region": (800, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_2_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 2 title: ",
            },
            "quest_2_claim_data": {
                "region": (870, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_2_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 2 text: ",
            },
            "quest_3_title_data": {
                "region": (1240, 310, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_3_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 3 title: ",
            },
            "quest_3_claim_data": {
                "region": (1310, 570, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_3_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 3 text: ",
            },
            "quest_4_title_data": {
                "region": (350, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_4_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 4 title: ",
            },
            "quest_4_claim_data": {
                "region": (420, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_4_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 4 text: ",
            },
            "quest_5_title_data": {
                "region": (800, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_5_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 5 title: ",
            },
            "quest_5_claim_data": {
                "region": (870, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_5_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 5 text: ",
            },
            "quest_6_title_data": {
                "region": (1240, 675, 320, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_6_title.png',
                "type": "daily-reward-quest",
                "msg": "Quest 6 title: ",
            },
            "quest_6_claim_data": {
                "region": (1310, 935, 200, 60),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\multiple_rewards\quest_6_claim.png',
                "type": "daily-reward-quest",
                "msg": "Quest 6 text: ",
            },
        }

        return quest_data

    def getCampaignScreenshotData(self):
        campaign_data = {
            "campaign_claim": {
                "region": (60, 780, 180, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\campaign_claim.png',
                "type": "campaign-claim",
                "msg": "Campaign Claim reset timer: ",
            },
        }

        return campaign_data

    def getGuildExpeditionData(self):
        guild_expedition_data = {
            "expedition_reset_data": {
                "region": (1030, 140, 150, 40),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\guild\expedition_renew.png',
                "type": "guild-expedition-time",
                "msg": "Guild Expedition reset timer: ",
            },
            "expedition_1_data": {
                "region": (770, 355, 150, 40),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\guild\expedition_timer.png',
                "type": "guild-expedition-special-case",
                "msg": "Guild Expedition 1 timer: ",
            },
            "expedition_1_complete_check": {
                "region": (600, 342, 190, 40),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\guild\expedition_is_complete.png',
                "type": "guild-expedition-is-complete",
                "msg": "Guild Expedition is complete text: ",
            },
        }

        return guild_expedition_data

    def getMapMissionClaimData(self):
        map_data = {
            "claim_slot_1": {
                "region": (90, 290, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_1.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 1 claim text: ",
            },
            "claim_slot_2": {
                "region": (90, 440, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_2.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 2 claim text: ",
            },
            "claim_slot_3": {
                "region": (90, 590, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_3.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 3 claim text: ",
            },
            "reset_timer": {
                "region": (10, 1020, 365, 45),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\reset_timer.png',
                "type": "map-reset-timer",
                "msg": "Map reset timer: ",
            },
            "mission_time_region": {
                "region": (1030, 860, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\mission_timer.png',
                "type": "map-mission-timer",
                "msg": "mission timer text: ",
            },
        }
        return map_data

    def getMapMissionData(self):
        missions = {
            "type_1": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\map_type_1.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\maps\side_menu_1.png',
            },
            "type_2": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\map_type_2.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\side_menu_2.png',
            },
            "type_3": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\map_type_3.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\side_menu_3.png',
            },
            "type_4": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\map_type_4.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\maps\side_menu_4.png',
            },
            "map_screenshot": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\map_save_mission_1.png',
            "mission_time_region": {
                "region": (1030, 860, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone V2\data\imgs\map\mission_timer.png',
                "type": "map-mission-timer",
                "msg": "mission timer text: ",
            }
        }
        return missions

    def getAlchemyExperimentData(self):
        map_data = {
            "experiement_timer_1": {
                "region": (860, 685, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_1.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 1 claim text: ",
            },
            "experiement_timer_2": {
                "region": (1240, 685, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_2.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 2 claim text: ",
            },
            "experiement_timer_3": {
                "region": (1615, 685, 150, 50),
                "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\claim_slot_3.png',
                "type": "map-sidebar-claim",
                "msg": "mission slot 3 claim text: ",
            },
        }
        return map_data

    def getMagicQuarterData(self):
        data = {
            "magic_quarter_timer": {
                "region": (1145, 705, 130, 40),
                "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\magic_progress_temp.png',
                "type": "magic-progress",
                "msg": "Magic quarter train timer: "
            },
        }
        return data
