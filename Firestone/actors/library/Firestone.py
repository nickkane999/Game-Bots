import pyautogui
import time
import re
import sys
import os
import operator


class Firestone:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.library_screen = bot.data["library"]
        self.coordinates = ""
        self.firestone_data = {}

    def moveFirestoneMenuRight(self):
        pyautogui.click(1800, 200)
        pyautogui.dragTo(100, 200, 0.5, button='left')
        pyautogui.click(1800, 200)
        pyautogui.dragTo(100, 200, 0.5, button='left')

    def moveFirestoneMenuLeft(self):
        pyautogui.click(100, 200)
        pyautogui.dragTo(1800, 200, 0.5, button='left')
        pyautogui.click(100, 200)
        pyautogui.dragTo(1800, 200, 0.5, button='left')

    def moveFirestoneMenuSlightLeft(self):
        pyautogui.click(1500, 200)
        pyautogui.dragTo(1800, 200, 0.5, button='left')

    def assignQueueData(self, instructions):
        self.coordinates = self.library_screen["icons"]
        self.instructions = instructions

    def processFirestonesQueue(self, instructions):
        self.assignQueueData(instructions)
        print(instructions)

        available_upgrades = instructions["available_upgrades"]
        sorted_options = instructions["sorted_options"]
        upgrade_amount = instructions["upgrade_amount"]

        self.firestone_data["items"] = {}

        self.game_bot.click(self.coordinates["firestone"])

        for upgrade in sorted_options:
            if upgrade["name"] in available_upgrades:
                print(upgrade_amount)
                self.displayFirestoneUpgrade(upgrade)
                self.upgradeFirestone(upgrade)

                upgrade_amount -= 1
                if upgrade_amount <= 0:
                    break
                print("New upgrade amount")
                print(upgrade_amount)

        print("Finish firestone upgrading")
        # self.updateFirestoneDatabase()
        self.returnToBattleScreen()

    def displayFirestoneUpgrade(self, upgrade):

        menu = upgrade["placement_area"]
        self.navigateToMenu(menu)

        tier = self.instructions["tier"]
        tier = "tier_" + str(tier) + "_firestone"
        upgrade_name = upgrade["name"]

        upgrade_point = self.coordinates[tier][upgrade_name]
        self.game_bot.click(upgrade_point)
        time.sleep(1)

    def upgradeFirestone(self, upgrade):
        bot = self.game_bot
        coordinates = self.coordinates
        screenshot_helper = self.game_bot.screenshot_helper

        empty_point = {"x": 1800, "y": 200}
        name = upgrade["name"]

        upgrade_info = {
            "region": (1040, 680, 140, 45),
            "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\firestone_progress_temp.png',
            "type": "firestone-progress",
            "msg": "Firestone " + upgrade["name"] + " upgrade time: "
        }
        upgrade_time = screenshot_helper.getScreenshotTime(upgrade_info)

        self.firestone_data["items"][name] = int(upgrade_time)
        print("clicking on point")
        print(coordinates["research_start"])
        # bot.click(coordinates["research_start"])
        self.firestone_data["save_time"] = time.time()
        bot.click(empty_point)
        time.sleep(1)

    def updateFirestoneDatabase(self):
        data = {
            "count": 2,
            "items": self.firestone_data["items"],
            "save_time": self.firestone_data["save_time"]
        }

        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveFirestone(data, file)
        self.game_bot.db.saveDataFile()
        '''
        print("Saved this data: ")
        print(self.game_bot.db.data)
        '''

    def navigateToMenu(self, menu):
        if menu == 1:
            self.moveFirestoneMenuLeft()
        elif menu == 2:
            self.moveFirestoneMenuRight()
        elif menu == 3:
            self.moveFirestoneMenuRight()
            self.moveFirestoneMenuSlightLeft()

    def returnToBattleScreen(self):
        bot = self.game_bot
        coordinates = self.coordinates

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])

    def getSortedUpgradeOptions(self):
        data = self.game_bot.db.data
        server = "server_" + data["general"]["current_server"]
        firestone_data = data[server]["firestone_progress"]
        options = firestone_data["options"]
        sorted_options = sorted(
            options.items(), key=lambda option: option[1]["priority"])
        return sorted_options

    def getUpgradeInstructions(self, upgrades_available):
        db = self.game_bot.db
        data = db.data
        server = db.getServerString()

        sorted_options = self.getSortedUpgradeOptions()
        active_items = db.data[server]["firestone_progress"]["upgrades_in_progress"]["items"]

        upgrades = []

        if (upgrades_available > 0):
            for key, item in sorted_options:
                if not item["completed"] and item["name"] not in active_items:
                    upgrades.append(item)
                    upgrades_available -= 1
                    if upgrades_available <= 0:
                        break

        # print(upgrades)
        return upgrades

    '''
    def processPriorityFirestones(self):
        bot = self.game_bot

        self.moveFirestoneMenuLeft()
        self.selectFirestone("firestone_gold_left")
        self.selectFirestone("firestone_gold_left")
        self.selectFirestone("firestone_damage_left")
        self.moveFirestoneMenuRight()
        self.selectFirestone("firestone_prestigious_right")
        self.selectFirestone("firestone_mission_planning_right")
        self.selectFirestone("firestone_wave_right")
        self.selectFirestone("firestone_training_right")
        self.selectFirestone("firestone_honor_right")

    def processSecondaryFirestones(self):
        bot = self.game_bot

        self.selectFirestone("firestone")
        self.moveFirestoneMenuLeft()
        self.selectFirestone("firestone_projectiles_left")
        self.selectFirestone("firestone_guardian_left")
        self.selectFirestone("firestone_fist_left")
        self.selectFirestone("firestone_health_left")
        self.selectFirestone("firestone_armor_left")
        self.moveFirestoneMenuRight()
        self.selectFirestone("firestone_weak_enemy_right")
        self.selectFirestone("firestone_weak_boss_right")
        self.moveFirestoneMenuSlightLeft()
        self.selectFirestone("firestone_loot_chance_right_slight")
        self.selectFirestone("firestone_loot_bonus_right_slight")
    '''
