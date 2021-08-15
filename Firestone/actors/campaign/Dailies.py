import pyautogui
import time
import re
import sys
import os


class Dailies:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.campaign_screen = bot.data["campaign"]
        self.coordinates = bot.data["campaign"]["icons"]

    def moveDailyMenuLeft(self):
        pyautogui.click(100, 400)
        pyautogui.dragTo(1800, 400, 0.5, button='left')
        pyautogui.click(100, 400)
        pyautogui.dragTo(1800, 400, 0.5, button='left')
        time.sleep(1)

    def moveDailyMenuRight(self):
        pyautogui.click(1800, 400)
        pyautogui.dragTo(100, 400, 0.5, button='left')
        pyautogui.click(1800, 400)
        pyautogui.dragTo(100, 400, 0.5, button='left')
        time.sleep(1)

    def processDailyMissions(self):
        self.game_bot.db.refreshData()
        self.server = self.game_bot.db.getServerString()
        self.dailies_data = self.game_bot.db.data[self.server]["campaign_progress"]["dailies"]
        game_bot = self.game_bot

        self.enterDailyLiberationZone()
        self.finishLiberationDailies()
        self.game_bot.db.saveDataFile()

        self.exitDailyLiberation()
        self.exitDailyMenu()
        self.returnToBattleScreen()

    def enterDailyLiberationZone(self):
        self.game_bot.click(self.coordinates["campaign_daily_start"])
        self.game_bot.click(self.coordinates["campaign_daily_liberation_open"])
        self.moveDailyMenuLeft()

    def finishLiberationDailies(self):
        missions = self.coordinates["daily_missions"]["mission_set_1"]
        liberation_has_completed = self.dailies_data["liberation"]
        server = self.server
        wait_time = self.game_bot.db.data[self.server]["campaign_progress"]["daily_wait_time"]

        for mission in missions:
            if not liberation_has_completed[mission] and liberation_has_completed[mission] != "locked":
                self.game_bot.click(missions[mission])
                self.game_bot.db.data[server]["campaign_progress"]["dailies"]["liberation"][mission] = True
                self.game_bot.db.saveDataFile()
                time.sleep(wait_time)
                self.game_bot.click(self.coordinates["battle_ok"])
                time.sleep(2)

        self.moveDailyMenuRight()

    def exitDailyLiberation(self):
        self.game_bot.click(self.coordinates["daily_liberation_x_icon"])

    def exitDailyMenu(self):
        self.game_bot.click(self.coordinates["daily_main_x_icon"])

    def returnToBattleScreen(self):
        self.game_bot.click(self.coordinates["x_icon"])
        self.game_bot.click(self.coordinates["x_icon"])
