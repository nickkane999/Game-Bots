import pyautogui
import time
import re
import sys
import os

import easyocr
import pytesseract

from utilities.menus.MenuNavigator import MenuNavigator
from utilities.ScreenHelper import ScreenHelper
from templates.TestTemplate import TestTemplate
from actors.Bot import Bot


class MenuTest(TestTemplate):
    # Initializing Object
    def __init__(self):
        super(MenuTest, self).__init__()
        self.menu_navigator = MenuNavigator()
        self.screenshot_helper = ScreenHelper()
        self.tests = self.getTests()
        self.bot = Bot()

    def getTests(self):
        return [
            self.selectMaps
        ]

    def selectMaps(self):
        menus = self.menu_navigator.menus
        home_menu = menus["1"]["home"]
        map_menu = menus["2"]["maps"]

        sh = self.screenshot_helper
        info = {
            "area": (900, 880, 120, 70),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\BTD6\data\img\map_victory.png',
            "type": "victory"
        }
        has_finished = sh.verifyVictoryMsg(info)
        print(has_finished)
        sys.exit()

        self.enterMapSelection()
        settings = {
            "map": "monkey meadow",
            "stage_difficulty": "beginner",
            "mode_difficulty": "easy",
            "mode_option": "standard"
        }
        self.selectMap(settings)
        print("I entered map")
        sys.exit()

    def enterMapSelection(self):
        home_menu = self.menu_navigator.menus["1"]["home"]
        self.bot.click(home_menu["play"])
        time.sleep(1)

    def selectMap(self, settings):
        stage_difficulty = settings["stage_difficulty"]
        mode_difficulty = settings["mode_difficulty"]
        map_button = settings["map"]
        mode = settings["mode_option"]

        map_menu = self.menu_navigator.menus["2"]["maps"]
        difficulty_menu = self.menu_navigator.menus["3"]["difficulty"]
        options_menu = self.menu_navigator.menus["4"][mode_difficulty]

        self.resetMapOptions(stage_difficulty)
        self.bot.click(map_menu[stage_difficulty][map_button])
        self.bot.click(difficulty_menu[mode_difficulty])
        self.bot.click(options_menu[mode])
        self.bot.click(options_menu["overrite_save"])

        # sleep while loading map
        time.sleep(5)

    def resetMapOptions(self, current_difficulty):
        map_menu = self.menu_navigator.menus["2"]["maps"]
        difficulties = ["beginner", "intermediate", "advanced", "expert"]
        for mode in difficulties:
            if mode is not current_difficulty:
                self.bot.click(map_menu["navigation"][mode])
                break
        self.bot.click(map_menu["navigation"][current_difficulty])

    def getMenuOneTowers(self):
        towers = {
            "hero": {"x": 1710, "y": 220},
            "dart monkey": {"x": 1820, "y": 220},
            "boomerang monkey": {"x": 1710, "y": 350},
            "bomb shooter": {"x": 1820, "y": 350},
            "tack shooter": {"x": 1710, "y": 500},
            "ice monkey": {"x": 1820, "y": 500},
            "glue gunner": {"x": 1710, "y": 620},
            "sniper monkey": {"x": 1820, "y": 620},
            "monkey sub": {"x": 1710, "y": 750},
            "monkey buccaneer": {"x": 1820, "y": 750},
            "monkey ace": {"x": 1710, "y": 900},
            "heli pilot": {"x": 1820, "y": 900},
        }
        return towers
