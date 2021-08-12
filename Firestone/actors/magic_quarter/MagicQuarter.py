import pyautogui
import time
import re
import sys
import os
import operator


class MagicQuarter:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.magic_screen = bot.data["magic_quarter"]
        self.coordinates = ""

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def startMagicDuties(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        magic_quarter_coordinates = self.magic_screen["icons"]
        db = game_bot.db.data
        instructions = queue_processor.verifyQueueMagicQuarter(db)
        self.assignQueueData(magic_quarter_coordinates, instructions)

        needs_visit = instructions["magic_quarter"]["needs_upgrade"]

        if needs_visit:
            self.enterMagicQuarterZone()
            time.sleep(1)
            self.processMagicQuarterQueue()
            self.returnToBattleScreen()

    def enterMagicQuarterZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["magic_quarter"])

    def processMagicQuarterQueue(self):
        bot = self.game_bot
        instructions = self.instructions["magic_quarter"]
        coordinates = self.coordinates
        server = instructions["server"]

        guardian_slot = instructions["upgrade_info"]["guardian_slot"]
        guardian_point = coordinates[guardian_slot]
        train_point = coordinates["train"]

        bot.click(guardian_point)
        time_for_upgrade = self.getMagicTrainTime()
        bot.click(train_point)

        self.game_bot.db.data[server]["magic_quarter_progress"]["upgrade_time"] = str(
            time_for_upgrade)
        self.game_bot.db.data[server]["magic_quarter_progress"]["save_time"] = time.time(
        )

        self.game_bot.db.saveDataFile()

    def getMagicTrainTime(self):
        screenshot_helper = self.game_bot.screenshot_helper
        upgrade_info = {
            "area": (1145, 705, 130, 40),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\magic_progress_temp.png',
            "type": "magic-progress"
        }
        text = screenshot_helper.getScreenshotText2(upgrade_info)
        print("Magic Quarter train timer: " + text)
        return text

    def returnToBattleScreen(self):
        bot = self.game_bot
        coordinates = self.coordinates

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])

    def getUpgradeInstructions(self, active_upgrades):
        # If process becomes more complex, this will need to get made for the "QueueInstructions" class to use
        string = "tbd"
