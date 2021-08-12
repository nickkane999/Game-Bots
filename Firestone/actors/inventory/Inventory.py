import pyautogui
import time
import re
import sys
import os


class Inventory:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.campaign_screen = bot.data["campaign"]

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def completeQuest(self, times_completed):
        return True

    def enterCampaignZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["battles"])
        bot.click(self.town_screen["icons"]["campaign_confirm"])

    def processCampaignQueue(self):
        bot = self.game_bot
        instructions = self.instructions["campaign"]
        coordinates = self.coordinates
        server = instructions["server"]
        bot.click(coordinates["claim_reward"])
        bot.click(coordinates["claim_reward"])
        time.sleep(1)

        campaign_claim_data = {
            "region": (60, 780, 180, 45),
            "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\campaign_claim.png',
            "type": "campaign-claim",
            "msg": "Campaign Claim reset timer: ",
        }
        campaign_claim_time = self.getScreenshotTime(campaign_claim_data)
        data = {
            "campaign_claim_time": campaign_claim_time,
            "current_time": time.time(),
            "server": server
        }
        self.saveCurrentProgress(data)

    def returnToBattleScreen(self):
        bot = self.game_bot
        campaign_coordinates = self.campaign_screen["icons"]

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])

    def saveCurrentProgress(self, data):
        server = data["server"]
        self.game_bot.db.data[server]["campaign_progress"]["campaign_claim_time"] = data["campaign_claim_time"]
        self.game_bot.db.data[server]["guild_progress"]["save_time"] = data["current_time"]
        self.game_bot.db.saveDataFile()

    def getScreenshotTime(self, data):
        screenshot_helper = self.game_bot.screenshot_helper
        upgrade_info = {
            "area": data["region"],
            "img_path": data["image"],
            "type": data["type"]
        }
        text = screenshot_helper.getScreenshotText2(upgrade_info)
        print(data["msg"] + text)
        return text
