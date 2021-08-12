import pyautogui
import time
import re
import sys
import os

from actors.utilities.GameStartup import GameStartup


class ServerSwap:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.battle_screen = bot.data["battle"]
        self.setting_screen = bot.data["settings"]
        self.conditions = bot.conditions
        self.screenshot_helper = bot.screenshot_helper

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def startServerSwapDuties(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        coordinates = self.setting_screen["icons"]
        db = game_bot.db
        instructions = queue_processor.verifyQueueServerSwap(db)
        self.assignQueueData(coordinates, instructions)

        needs_swap = instructions["server_swap"]["needs_swap"]

        if needs_swap:
            self.processServerSwap()

            swap_info = {
                "current_time": time.time(),
                "current_server": self.getChangedServerData()
            }
            self.saveCurrentProgress(swap_info)

    def determineServerSwap(self, server_swap_settings):
        game_bot = self.game_bot
        battle_coordinates = self.battle_screen["icons"]
        setting_coordinates = self.setting_screen["icons"]
        print("a")

        low_hero_dps = self.evaluateDps()
        print(low_hero_dps)

        if (low_hero_dps):
            self.startServerSwap()

        return server_swap_settings

    def processServerSwap(self):
        bot = self.game_bot
        battle_coordinates = self.battle_screen["icons"]
        setting_coordinates = self.setting_screen["icons"]

        bot.click(battle_coordinates["settings"])
        time.sleep(5)
        bot.click(setting_coordinates["save_before_swap"])

        bot.click(setting_coordinates["server_switch_start"])
        bot.click(setting_coordinates["server_1"])
        bot.click(setting_coordinates["server_5"])
        bot.click(setting_coordinates["confirm_switch"])
        bot.click(setting_coordinates["refresh_confirm"])
        self.resetFullScreen()

    def resetFullScreen(self):
        time.sleep(40)
        print("Now in fullscreen mode")
        bot = self.game_bot
        startup = GameStartup(bot)
        startup_coordinates = startup.startup_screen["icons"]
        startup.enterFullScreen(startup_coordinates)

    def getChangedServerData(self):
        server = self.game_bot.db.getServerString()
        return "1" if (server == "server_5") else "5"

    def saveCurrentProgress(self, data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveServerSwap(data, file)
        self.game_bot.db.saveDataFile()

    def pullBattleDps(self):
        screenshot_helper = self.screenshot_helper
        enemy_info = {
            "area": (1020, 65, 190, 50),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\enemy_dps.png',
            "type": "battle_enemy_dps"
        }
        hero_info = {
            "area": (10, 1040, 200, 40),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\hero_dps.png',
            "type": "battle_hero_dps"
        }
        time.sleep(2)

        hero_dps = self.getDpsScreenshot(hero_info)
        enemy_health = self.getDpsScreenshot(enemy_info)

        hero_dps = hero_dps.split("e")
        enemy_health = self.convertEnemyHealth(enemy_health, enemy_info)

        return {"hero_dps": hero_dps, "enemy_health": enemy_health}

    '''
    def evaluateDps(self):
        dpsResults = self.pullBattleDps()
        hero_dps = dpsResults["hero_dps"]
        enemy_health = dpsResults["enemy_health"]

        starting_reset = (len(hero_dps) <= 1 or len(enemy_health) <= 1)
        if (starting_reset):
            return False
        else:
            if (self.verifyValidValues(hero_dps[-1], enemy_health[-1])):
                return True if (float(hero_dps[-1]) <= float(enemy_health[-1])) else False


    def getDpsScreenshot(self, info):
        screenshot_helper = self.screenshot_helper
        area = info["area"]
        img_path = info["img_path"]
        dps_type = info["type"]

        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(img_path)
        dps_text = screenshot_helper.convertImageToText(img_path, dps_type)
        print(dps_text)
        return dps_text

    def convertEnemyHealth(self, enemy_health, enemy_info):
        count = 0
        while (enemy_health == "bad string" and count < 10):
            enemy_health = self.getDpsScreenshot(enemy_info)
            count = count + 1

        new_enemy_health = enemy_health.split("e")

        return new_enemy_health

    def verifyValidValues(self, hero_dps, enemy_health):
        try:
            test_float_conversion = float(hero_dps)
            test_float_conversion = float(enemy_health)
            return True
        except:
            print("unable to convert enemy or hero data to float")
            return False
    '''
