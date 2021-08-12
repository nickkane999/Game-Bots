import pyautogui
import time
import re
import sys
import os


class SingleReward:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.img_regions = bot.screenshot_data.data["single_reward"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.shop_screen = bot.data["shop"]

    def getDailyRewardTimer(self):
        self.game_bot.db.refreshData()
        db = self.game_bot.db
        instructions = self.game_bot.queue_processor.verifyQueueSingleRewards(
            db)
        needs_visit = instructions["single_reward"]["needs_visit"]

        if (needs_visit):
            print("Doing daily reset")
            self.game_bot.db.refreshData()
            game_bot = self.game_bot

            self.getDailyReward()
            reset_time = self.getDailyResetTimer()
            if (reset_time > 86280):  # Reset timer is greater than 23:59:00 (Haven't done dailies yet)
                print("Reseting dailies timers: " + str(reset_time))
                self.saveDailyQuestResets()

            data = {"reset_time": reset_time}
            self.saveResetTime(data)
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

    def saveResetTime(self, data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveDataSingleReward(
            data, file)
        self.game_bot.db.saveDataFile()

    def saveDailyQuestResets(self):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.resetMultipleRewardDailies(
            file)
        self.game_bot.db.saveDataFile()

    def returnToBattleScreen(self):
        self.game_bot.click(self.shop_screen["icons"]["x_icon"])
