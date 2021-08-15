import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np

from actors.map.MissionStart import MissionStart
from actors.map.MissionClaim import MissionClaim


class Map:
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

        self.vertical_map_movement = 0
        self.mission_images = self.buildMissions()

        self.mission_claim = MissionClaim(bot)
        self.mission_start = MissionStart(bot)

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
