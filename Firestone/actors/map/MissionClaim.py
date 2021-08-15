import pyautogui
import time
import re
import sys
import os


class MissionClaim:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.map_screen = bot.data["map"]

        self.claim_regions = bot.screenshot_data.data["mission-claim"]
        self.mission_images = self.buildMissions()

    def buildMissions(self):
        missions = {
            "type_1": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\map_type_1.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\maps\side_menu_1.png',
            },
            "type_2": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\map_type_2.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\side_menu_2.png',
            },
            "type_3": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\map_type_3.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\side_menu_3.png',
            },
            "type_4": {
                "map": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\map\map_type_4.png',
                "side_menu": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\imgs\maps\side_menu_4.png',
            },
        }

        return missions

    def processMissionClaim(self, instructions):
        self.instructions = instructions
        needs_claim = instructions["needs_claim"]
        remaining_missions = instructions["mission_unclaimed_list"]

        if needs_claim:
            self.clickOnClaims()
            print("Missions have been claimed")

        save_data = {
            "remaining_missions": remaining_missions
        }
        # print("remaining missions")
        # print(remaining_missions)
        self.saveClaimData(save_data)
        print("Missions claims have been saved")

    def clickOnClaims(self):
        instructions = self.instructions
        claim_images = self.claim_regions
        screenshot_helper = self.game_bot.screenshot_helper
        map_coordinates = self.map_screen["icons"]

        claim_count = instructions["mission_claim_count"]
        claim_area = claim_images["claim_slot_1"]
        point_claim = map_coordinates["claim_slot_1"]
        point_ok = map_coordinates["claim_ok_side"]

        for x in range(claim_count):
            claim_text = screenshot_helper.getScreenshotTime(claim_area)
            if claim_text == "Claim":
                self.game_bot.click(point_claim)
                self.game_bot.click(point_ok)
                time.sleep(1)
                # print("Clicked point")
                # print(point_claim)

    def changeMissionSlots(self, missions, lookup_mission):
        found_mission = False

        for mission in missions:
            if found_mission:
                missions[mission]["slot"] -= 1
            if mission == lookup_mission:
                found_mission = True

        #print("Adjusted missions")
        # print(missions)
        return missions

    def saveClaimData(self, data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveMissionsClaimed(
            data, file)
        self.game_bot.db.saveDataFile()
