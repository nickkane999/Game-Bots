import pyautogui
import time
import re
import sys
import os
import webbrowser


class GameStartup:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot, device_type):
        self.game_bot = bot
        if device_type == "desktop":
            self.startup_screen = bot.data["startup_desktop_100_zoom"]
        elif device_type == "laptop":
            self.startup_screen = bot.data["startup_laptop_100_zoom"]

        self.conditions = bot.conditions

    def runStartup(self, startup_settings):
        webbrowser.open_new(
            'https://armorgames.com/play/18485/firestone-idle-rpg')
        game_bot = self.game_bot
        coordinates = self.startup_screen["icons"]
        print(startup_settings)
        time.sleep(20)

        self.enterFullScreen(coordinates)
        startup_settings["has_ran"] = True
        print(startup_settings)

        return startup_settings

    def enterFullScreen(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["loot_collect"])
        bot.click(coordinates["loot_collect"])
        bot.click(coordinates["settings_icon"])
        bot.click(coordinates["fullscreen_button"])
        bot.click(coordinates["fullscreen_button"])
        bot.click(coordinates["x_icon"])
