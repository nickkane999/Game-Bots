import pyautogui
import time
import re
import sys
import os

import easyocr
import pytesseract

from data.menus.Menus import Menus
from templates.MenuTemplate import MenuTemplate


class MenuNavigator(MenuTemplate):
    # Initializing Object
    def __init__(self):
        self.menu_layer = 1
        self.menus = Menus().data

    def getTests(self):
        return [
            self.selectTowers
        ]

    def selectMenu(self):
        sample_towers = [
            "bomb shooter",
            "druid",
            "banana farm",
            "alchemist",
            "ice monkey",
            "monkey ace",
        ]
        print("I ran")
        for tower in sample_towers:
            self.tower_selector.selectTower(tower)
            time.sleep(1)
        sys.exit()

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
