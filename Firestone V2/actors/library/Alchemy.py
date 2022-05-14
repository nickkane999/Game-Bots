import pyautogui
import time
import re
import sys
import os
import operator
import win32gui

class Alchemy:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.points = {
            "check_1": { "x": 1040, "y": 785 },
            "check_2": { "x": 1410, "y": 785 },
            "check_3": { "x": 1790, "y": 785 },
            "alchemy_active": { "x": 580, "y": 885 },
            "alchemy_map": { "x": 460, "y": 800 },
        }
        self.completed_upgrade_slot = [1140, 1000] 
        self.status = {
            "not_ready": [(184, 183, 181)],
            "ready": [(255, 195, 82)],
            "change_active": [(255, 255, 255), (247, 0, 0)],
        }

    def runAlchemyCheck(self):
        print("I'm in the alchemy check")
        pyautogui.press("t")
        #in_menu = self.menuCheck("Town", self.game_bot)
        if self.alchemyReady():
            bot = self.game_bot
            points = self.points
            bot.click(self.points["alchemy_map"])
            time.sleep(0.5)
            if bot.get_pixel_color(points["check_1"]["x"], points["check_1"]["y"]) in self.status["ready"]:
                bot.click(points["check_1"])
            if bot.get_pixel_color(points["check_2"]["x"], points["check_2"]["y"]) in self.status["ready"]:
                bot.click(points["check_2"])
        else:
            print("Did not find alchemy menu")
        return

    def alchemyReady(self):
        if self.game_bot.get_pixel_color(self.points["alchemy_active"]["x"], self.points["alchemy_active"]["y"]) in self.status["change_active"]:
            print("Alchemy is active")
            time.sleep(0.5)
            return True
        else:
            return False