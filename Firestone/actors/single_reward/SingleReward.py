import pyautogui
import time
import re
import sys
import os

from actors.ActorTemplate import ActorTemplate
from actors.utilities.save_helper.SingleRewardSaveHelper import SingleRewardSaveHelper


class SingleReward(ActorTemplate):
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        super(SingleReward, self).__init__(bot)
        self.game_bot = bot
        self.save_helper = SingleRewardSaveHelper(bot)
        self.conditions = bot.conditions
        self.img_regions = bot.screenshot_data.data["single_reward"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.shop_screen = bot.data["shop"]

    def startDuties(self):
        self.loadData()
        instructions = self.instructions

        needs_visit = instructions["single_reward"]["needs_visit"]

        if (needs_visit):
            print("Doing daily reset")
            self.game_bot.db.refreshData()
            game_bot = self.game_bot

            self.getDailyReward()
            reset_time = self.getDailyResetTimer()
            if (reset_time > 86280):  # Reset timer is greater than 23:59:00 (Haven't done dailies yet)
                print("Reseting dailies timers: " + str(reset_time))

            data = {"reset_time": reset_time}
            self.saveProgress(data)
            self.returnToBattleScreen()

    def getDailyReward(self):
        self.enterDailyRewardZone()
        self.claimDailyReward()

    def enterDailyRewardZone(self):
        self.game_bot.click(self.battle_screen["icons"]["daily_reward"])
        self.game_bot.click(self.shop_screen["icons"]["daily_reward_tab"])

    def claimDailyReward(self):
        self.game_bot.click(self.shop_screen["icons"]["daily_reward_claim"])
        # Exits claim "ok" menu if that's currently open
        self.game_bot.click(self.shop_screen["icons"]["daily_reward_claim"])

    def getDailyResetTimer(self):
        daily_timer_data = self.img_regions["daily_timer"]
        screenshot_helper = self.game_bot.screenshot_helper
        time = screenshot_helper.getScreenshotTime(daily_timer_data)
        return int(time)

    def returnToBattleScreen(self):
        self.game_bot.click(self.shop_screen["icons"]["x_icon"])
