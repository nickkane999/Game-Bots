import pyautogui
import time
import re
import sys
import os

from actors.campaign.Dailies import Dailies
from actors.campaign.Story import Story


class Campaign:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.dailies = Dailies(bot)
        self.campaign_regions = bot.screenshot_data.data["campaign"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.campaign_screen = bot.data["campaign"]

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def completeQuest(self, times_completed):
        self.coordinates = self.campaign_screen["icons"]

        self.enterCampaignZone()
        dailies = self.dailies
        dailies.processDailyMissions()
        return True

    def startCampaignDuties(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        campaign_coordinates = self.campaign_screen["icons"]
        db = game_bot.db.data
        instructions = queue_processor.verifyQueueCampaign(db)
        self.assignQueueData(campaign_coordinates, instructions)

        needs_visit = instructions["campaign"]["needs_visit"]

        if needs_visit:
            self.enterCampaignZone()
            self.processCampaignQueue()
            self.returnToBattleScreen()

    def enterCampaignZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["battles"])
        bot.click(self.town_screen["icons"]["campaign_confirm"])

    def processCampaignQueue(self):
        bot = self.game_bot
        screenshot_helper = bot.screenshot_helper

        instructions = self.instructions["campaign"]
        coordinates = self.coordinates
        server = instructions["server"]

        bot.click(coordinates["claim_reward"])
        bot.click(coordinates["claim_reward"])
        time.sleep(1)
        campaign_claim_data = self.campaign_regions["campaign_claim"]
        claim_time = screenshot_helper.getScreenshotTime(campaign_claim_data)
        data = {
            "campaign_claim_time": claim_time,
            "current_time": time.time(),
            "server": server
        }
        self.saveCurrentProgress(data)

    def returnToBattleScreen(self):
        bot = self.game_bot
        campaign_coordinates = self.campaign_screen["icons"]
        print("Exiting Campaign")
        print(campaign_coordinates)

        bot.click(campaign_coordinates["x_icon"])
        bot.click(campaign_coordinates["x_icon"])

    def saveCurrentProgress(self, data):
        server = data["server"]
        claim_time = int(data["campaign_claim_time"])

        self.game_bot.db.data[server]["campaign_progress"]["campaign_claim_time"] = claim_time
        self.game_bot.db.data[server]["campaign_progress"]["save_time"] = data["current_time"]
        self.game_bot.db.saveDataFile()
