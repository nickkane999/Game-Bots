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

    def processMissionMap(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        map_coordinates = self.map_screen["icons"]
        db = game_bot.db
        instructions = queue_processor.verifyQueueInstructionsMap(db)
        print(instructions)
        needs_claim = instructions["mission_claim"]["needs_claim"]
        needs_mission_start = instructions["mission_start"]["needs_mission_start"]

        if needs_claim or needs_mission_start:
            self.enterMapZone()
            print("Entered map")

            self.mission_claim.processMissionClaim(
                instructions["mission_claim"])
            print("Finished claim")
            self.game_bot.db.refreshData()
            self.mission_start.processMissionStart(
                instructions["mission_start"])

            self.returnToBattleScreen()

    def enterMapZone(self):
        self.game_bot.click(self.battle_screen["icons"]["map"])
        time.sleep(1)

    def returnToBattleScreen(self):
        self.game_bot.click(self.town_screen["icons"]["x_icon"])
