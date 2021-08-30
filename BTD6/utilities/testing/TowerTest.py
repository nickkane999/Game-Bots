import pyautogui
import time
import re
import sys
import os

import easyocr
import pytesseract

from utilities.TowerSelector import TowerSelector
from templates.TestTemplate import TestTemplate


class TowerTest(TestTemplate):
    # Initializing Object
    def __init__(self):
        super(TowerTest, self).__init__()
        self.tests = self.getTests()
        self.tower_selector = TowerSelector()

    def getTests(self):
        return [
            self.selectTowers
        ]

    def selectTowers(self):
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

    def placeTowers(self):
        pass

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
