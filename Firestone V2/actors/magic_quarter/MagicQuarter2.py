import pyautogui
import time
import re
import sys
import os
import operator

from actors.ActorTemplate import ActorTemplate
from actors.utilities.save_helper.MagicQuarterSaveHelper import MagicQuarterSaveHelper

class MagicQuarter2(ActorTemplate):

    # Initializing Object
    def __init__(self, bot):
        super(MagicQuarter2, self).__init__(bot)
        self.game_bot = bot
        self.save_helper = MagicQuarterSaveHelper(bot)
        self.magic_quarter_regions = bot.screenshot_data.data["magic_quarter"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.magic_screen = bot.data["magic_quarter"]

        self.points = {
            "upgrade": {"x": 1230, "y": 810},
            "close": {"x": 1840, "y": 50},
        }
        
    def runMagicQuarterCheck(self):
        pyautogui.press('g')
        time.sleep(0.5)
        self.game_bot.click(self.points["upgrade"])
        time.sleep(0.5)
        self.game_bot.click(self.points["close"])
        time.sleep(0.5)
        

    def startDuties(self):
        self.loadData()
        instructions = self.instructions
        coordinates = self.coordinates
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
        screenshot_helper = bot.screenshot_helper
        instructions = self.instructions["magic_quarter"]
        coordinates = self.coordinates
        server = instructions["server"]

        guardian_slot = instructions["upgrade_info"]["guardian_slot"]
        guardian_point = coordinates[guardian_slot]
        train_point = coordinates["train"]
        magic_timer = self.magic_quarter_regions["magic_quarter_timer"]

        bot.click(guardian_point)
        time_for_upgrade = screenshot_helper.getScreenshotTime(magic_timer)
        bot.click(train_point)

        data = {
            "time_for_upgrade": str(time_for_upgrade)
        }
        self.saveProgress(data)

    def returnToBattleScreen(self):
        bot = self.game_bot
        coordinates = self.coordinates

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
