import pyautogui
import time
import re
import sys
import os

from actors.ActorTemplate import ActorTemplate
from actors.utilities.save_helper.GuildSaveHelper import GuildSaveHelper


class Guild2(ActorTemplate):
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        super(Guild2, self).__init__(bot)
        self.save_helper = GuildSaveHelper(bot)
        #self.expedition_regions = bot.screenshot_data.data["guild_expedition"]

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.guild_screen = bot.data["guild"]
        self.guild_icon = {"x": 1510, "y": 140}

        
        self.points = {
            "expedition_icon": {"x": 260, "y": 370},
            "expedition_claim": {"x": 1330, "y": 310},
            "expedition_claim_success_exit": {"x": 380, "y": 1000},
            "expedition_close": {"x": 1510, "y": 70},
        }


    def runExpeditionCheck(self):
        pyautogui.press("t")        
        self.game_bot.click(self.guild_icon)
        time.sleep(0.5)
        in_menu = self.menuCheck("Guild", self.game_bot)
        if in_menu:
            for point in self.points:
                self.game_bot.click(self.points[point])
                time.sleep(0.5)
            print("Finished clicking points")
        else:
            print("Did not find guild menu")


    def completeMinerQuest(self, times_completed):
        return True

    def startDuties(self):
        self.loadData()
        instructions = self.instructions
        coordinates = self.coordinates

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
        print(self.coordinates)

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
        data = {
            "expedition_1_time": int(expedition_1_time),
            "expedition_reset_time": int(expedition_reset_time),
            "current_time": time.time(),
            "has_renewed": instructions["has_renewed"],
            "server": self.server,
        }
        self.saveProgress(data)

    def claimExpedition(self):
        server = self.server
        self.game_bot.click(self.coordinates["expedition_1"])
        self.game_bot.click(self.coordinates["expedition_ok"])
        print("Claimed Expedition")
        self.game_bot.db.data[server]["guild_progress"]["expeditions_remaining"] -= 1
        time.sleep(2)

    def startExpedition(self):
        self.game_bot.click(self.coordinates["expedition_1"])

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
