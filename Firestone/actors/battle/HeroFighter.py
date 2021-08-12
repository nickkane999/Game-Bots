import pyautogui
import time
import re
import sys
import os


class HeroFighter:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.server_swap = bot.server_swap
        self.fighter_screen = bot.data["battle"]

    # Major object functions
    def startAutoFighting(self, battle_settings):
        self.autoAttackButton = str(battle_settings["idle_attack_button"])
        self.captain_slot = str(battle_settings["captain_slot"])
        self.buyUpgrades()

    def buyUpgrades(self):
        bot = self.game_bot
        fighter_coordinates = self.fighter_screen["icons"]

        self.setupUpgradeMenu(fighter_coordinates)
        self.autoBuyUpgrades(fighter_coordinates)

    def setupUpgradeMenu(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["upgrades"])
        bot.click(coordinates["upgrades_amount"])
        bot.click(coordinates["upgrades_amount"])
        bot.click(coordinates["upgrades_amount"])

    def autoBuyUpgrades(self, coordinates):
        # Space autoclicks for guardian
        # Press 1 is for auto-using abilities
        # Upgrades_amount click is to make upgrade amount reset back to 1
        bot = self.game_bot
        pyautogui.keyDown('space')
        auto_attack = self.autoAttackButton if self.autoAttackButton else "1"

        dpsResults = self.server_swap.pullBattleDps()
        hero_dps = dpsResults["hero_dps"]
        enemy_health = dpsResults["enemy_health"]
        starting_reset = (len(hero_dps) <= 1 or len(enemy_health) <= 1)

        if (starting_reset):
            self.normalAutoBuy(auto_attack, coordinates)
        else:
            reaching_higher_levels = (
                float(hero_dps[-1]) <= float(enemy_health[-1]) + 8)
            if (reaching_higher_levels):
                self.priorityAutoBuy(auto_attack, coordinates)
            else:
                self.normalAutoBuy(auto_attack, coordinates)

        pyautogui.keyUp('space')
        bot.click(coordinates["upgrades_amount"])
        bot.click(coordinates["upgrades_amount"])
        exit = coordinates["upgrades_x_icon"]
        bot.click(exit)

    def normalAutoBuy(self, auto_attack, coordinates):
        bot = self.game_bot
        for x in range(1, 30):
            bot.click(coordinates["upgrade_1"])
            bot.click(coordinates["upgrade_2"])
            bot.click(coordinates["upgrade_3"])
            pyautogui.press(auto_attack)
            bot.click(coordinates["upgrade_4"])
            bot.click(coordinates["upgrade_5"])
            bot.click(coordinates["upgrade_6"])
            pyautogui.press(auto_attack)
            bot.click(coordinates["upgrade_7"])
            pyautogui.press(auto_attack)

    def priorityAutoBuy(self, auto_attack, coordinates):
        bot = self.game_bot
        priority = self.captain_slot
        for x in range(1, 30):
            bot.click(coordinates["upgrade_1"])
            bot.click(coordinates["upgrade_1"])
            bot.click(coordinates["upgrade_" + priority])
            pyautogui.press(auto_attack)
            bot.click(coordinates["upgrade_" + priority])
            bot.click(coordinates["upgrade_" + priority])
            bot.click(coordinates["upgrade_" + priority])
            pyautogui.press(auto_attack)
            bot.click(coordinates["upgrade_1"])
            pyautogui.press(auto_attack)
