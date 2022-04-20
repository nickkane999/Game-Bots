import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np

from actors.map.MissionStart import MissionStart
from actors.map.MissionClaim import MissionClaim


class Map2:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.map_screen = bot.data["map"]
        # self.map_regions = bot.screenshot_data.data["map"]

        self.status = {
            "mission_cancel": (231, 88, 79),
            "mission_claim": (239, 218, 189),
            "mission_claim_confirm": (12, 158, 8),
            "mission_start": (13, 161, 5),
            "no_missions_available": (239, 218, 189),
        }

        self.locations = {
            "mission_cancel": [730, 905],
            "mission_claim": [960, 875],
            "mission_claim_confirm": [950, 450],
            "mission_start": [960, 925],
            "mission_exit": [50, 950],
        }

        self.claim_points = [
            {"x": 200, "y": 225},
        ]

        self.vertical_map_movement = 0
        self.mission_images = self.buildMissions()

        self.mission_claim = MissionClaim(bot)
        self.mission_start = MissionStart(bot)


    def runMapCheck(self):
        print("I'm in the map check")
        pyautogui.press("m")
        time.sleep(0.5)

        # Claim missions
        # self.claimMissions()

        # Start missions
        self.startMissions()

    def startMissions(self):
        print("Finding missions")

        

    def claimMissions(self):
        bot = self.game_bot
        for point in self.claim_points:
            bot.click(point)
            time.sleep(0.5)

            if bot.get_pixel_color(self.locations["mission_cancel"][0], self.locations["mission_cancel"][1]) == self.status["mission_cancel"]:
                print("Mission in progress")
                bot.click({"x": self.locations["mission_exit"][0], "y": self.locations["mission_exit"][1]})
                time.sleep(0.5)
            elif bot.get_pixel_color(self.locations["mission_claim"][0], self.locations["mission_claim"][1]) == self.status["mission_claim"] or \
            bot.get_pixel_color(self.locations["mission_claim_confirm"][0], self.locations["mission_claim_confirm"][1]) == self.status["mission_claim_confirm"]:
                print("Mission complete")
                bot.click({"x": self.locations["mission_claim"][0], "y": self.locations["mission_claim"][1]})
                time.sleep(0.5)
                bot.click({"x": self.locations["mission_claim_confirm"][0], "y": self.locations["mission_claim_confirm"][1]})
                time.sleep(0.5)        

    def buildMissions(self):
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
        }

        return missions

    def resetMissionMap(self):
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        time.sleep(2)

    def getClaimInstructions(self):
        self.game_bot.db.refreshData()
        db = self.game_bot.db
        queue_processor = self.game_bot.queue_processor

        instructions = queue_processor.verifyQueueInstructionsMissionClaim(db)
        print("Claim instructions")
        print(instructions)
        return instructions

    def getMissionStartInstructions(self):
        self.game_bot.db.refreshData()
        db = self.game_bot.db
        queue_processor = self.game_bot.queue_processor

        instructions = queue_processor.verifyQueueInstructionsMissionStart(db)
        print("Mission start instructions")
        print(instructions)
        return instructions

    def processMissionMap(self):
        game_bot = self.game_bot
        map_coordinates = self.map_screen["icons"]

        claim_instructions = self.getClaimInstructions()
        needs_claim = claim_instructions["needs_claim"]

        if needs_claim:
            self.enterMapZone()
            print("Entered map")

            self.mission_claim.processMissionClaim(claim_instructions)

        start_instructions = self.getMissionStartInstructions()
        needs_mission_start = start_instructions["needs_mission_start"]
        missions_have_reset = start_instructions["missions_have_reset"]

        if needs_mission_start or missions_have_reset:
            if not needs_claim:
                self.enterMapZone()

            print("Entered map. Starting mission select / refresh")
            self.game_bot.db.refreshData()
            self.mission_start.processMissionStart(start_instructions)

    def enterMapZone(self):
        self.game_bot.click(self.battle_screen["icons"]["map"])
        time.sleep(1)

    def returnToBattleScreen(self):
        self.game_bot.click(self.town_screen["icons"]["x_icon"])
