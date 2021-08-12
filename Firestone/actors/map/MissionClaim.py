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
            save_data = {
                "remaining_missions": remaining_missions
            }
            self.saveClaimData(save_data)

    def clickOnClaims(self):
        instructions = self.instructions
        claim_images = self.claim_regions
        map_coordinates = self.map_screen["icons"]

        missions = instructions["mission_claim_list"]
        missions_adjusted = dict(missions)
        screenshot_helper = self.game_bot.screenshot_helper

        for mission in missions:
            adjusted_slot = missions_adjusted[mission]["slot"]
            slot_string = "claim_slot_" + str(adjusted_slot)
            claim_text = screenshot_helper.getScreenshotTime(
                claim_images[slot_string])
            if claim_text == "Claim":
                point_claim = map_coordinates[slot_string]
                point_ok = map_coordinates["claim_ok_side"]
                self.game_bot.click(point_claim)
                self.game_bot.click(point_ok)
                time.sleep(1)
                #print("Clicked point")
                # print(point)
                missions_adjusted = self.changeMissionSlots(
                    missions_adjusted, mission)
                mission_text = mission
                del missions_adjusted[mission_text]

        return missions_adjusted

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
