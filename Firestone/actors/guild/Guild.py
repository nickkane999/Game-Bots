import pyautogui
import time
import re
import sys
import os


class Guild:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.expedition_regions = bot.screenshot_data.data["guild-expedition"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.guild_screen = bot.data["guild"]

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def completeMinerQuest(self, times_completed):
        return True

    def startGuildDuties(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        db = game_bot.db
        instructions = queue_processor.verifyQueueGuild(db)
        guild_coordinates = self.guild_screen["icons"]
        self.assignQueueData(guild_coordinates, instructions)

        print("Guild Instructions: ")
        print(instructions)
        needs_visit = instructions["expeditions"]["needs_visit"]

        if needs_visit:
            self.enterGuildZone()
            self.processGuildQueue()
            self.returnToBattleScreen()

    def enterGuildZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["guild"])

    def processGuildQueue(self):
        bot = self.game_bot
        db = self.game_bot.db
        sh = bot.screenshot_helper

        self.server = db.getServerString()
        instructions = self.instructions["expeditions"]

        bot.click(self.coordinates["expeditions"])
        time.sleep(1)

        expedition_regions = self.expedition_regions
        expedition_1_time = expedition_regions["expedition_1_data"]
        expedition_reset_time = expedition_regions["expedition_reset_data"]
        expedition_1_complete = expedition_regions["expedition_1_complete_check"]

        expedition_1_complete = sh.getScreenshotTime(expedition_1_complete)
        if expedition_1_complete == "Completed":
            self.claimExpedition()
            # bot.click(self.coordinates["expeditions"])

        expedition_1_time = sh.getScreenshotTime(expedition_1_time)
        expedition_reset_time = sh.getScreenshotTime(expedition_reset_time)
        no_missions_available = expedition_1_time == "0"

        if not no_missions_available:
            self.startExpedition()
        else:
            expedition_1_time = 0

        bot.click(self.coordinates["expeditions"])
        save_data = {
            "expedition_1_time": int(expedition_1_time),
            "expedition_reset_time": int(expedition_reset_time),
            "current_time": time.time(),
            "has_renewed": instructions["has_renewed"],
            "server": self.server,
        }
        self.saveExpeditionData(save_data)

    def claimExpedition(self):
        server = self.server
        self.game_bot.click(self.coordinates["expedition_1"])
        self.game_bot.click(self.coordinates["expedition_ok"])
        print("Claimed Expedition")
        self.game_bot.db.data[server]["guild_progress"]["expeditions_remaining"] -= 1
        time.sleep(2)

    def startExpedition(self):
        self.game_bot.click(self.coordinates["expedition_1"])

    def saveExpeditionData(self, data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveExpeditions(data, file)
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

    def performExpedition(self):
        bot = self.game_bot
        coordinates = self.coordinates
        bot.click(coordinates["expedition_1"])
        bot.click(coordinates["expedition_ok"])
        bot.click(coordinates["expedition_1"])
        bot.click(coordinates["expedition_x_icon"])

    def returnToBattleScreen(self):
        self.game_bot.click(self.coordinates["x_icon"])
        self.game_bot.click(self.coordinates["x_icon"])
