import pyautogui
import time
import re
import sys
import os


class Temple:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot, conditions, screenshot_helper):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = conditions
        self.screenshot_helper = screenshot_helper

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.temple_screen = bot.data["temple"]

    def startTempleDuties(self, temple_settings):
        game_bot = self.game_bot
        temple_coordinates = self.temple_screen["icons"]

        self.enterTempleZone()
        game_bot.click(temple_coordinates["prestige_select"])

        firestone_results = self.firestoneRewardIsHigh(temple_settings)
        if (firestone_results["goal_met"]):
            temple_settings["time_firestone_level_reached"] = time.time()
            time.sleep(0.2)

        if (self.conditions.shouldResetTemple(firestone_results, temple_settings)):
            self.performTempleReset(temple_coordinates)
        else:
            self.exitMenu(temple_coordinates)

        return temple_settings  # do not reset the temple again

    def firestoneRewardIsHigh(self, temple_settings):
        screenshot_helper = self.screenshot_helper
        save_img_path = r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\firestone_progress.png'

        im3 = pyautogui.screenshot(region=(1020, 740, 260, 70))
        im3.save(save_img_path)
        a = screenshot_helper.convertImageToText(save_img_path, "firestone")
        print(a)
        a = float(a)
        if (a > 100):
            goal_met = True
            early_reset = True if (a > 500) else False
        else:
            goal_met = False
            early_reset = False
        return {
            "goal_met": goal_met,
            "early_reset": early_reset
        }

    def enterTempleZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["temple"])

    def performTempleReset(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["prestige_confirm"])
        time.sleep(6)

        self.getPartyGold()

    def getPartyGold(self):
        pyautogui.keyDown('space')
        time.sleep(10)
        pyautogui.keyUp('space')

    def exitMenu(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
