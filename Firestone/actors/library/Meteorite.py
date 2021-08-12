import pyautogui
import time
import re
import sys
import os


class Meteorite:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.library_screen = bot.data["library"]

    def startGuildDuties(self):
        game_bot = self.game_bot
        guild_coordinates = self.guild_screen["icons"]

        self.enterGuildZone()
        self.performExpedition(guild_coordinates)
        self.returnToBattleScreen(guild_coordinates)

    def enterGuildZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["guild"])

    def performExpedition(self, coordinates):
        bot = self.game_bot

        print(coordinates)

        bot.click(coordinates["expeditions"])
        bot.click(coordinates["expedition_1"])
        bot.click(coordinates["expedition_x_icon"])

    def returnToBattleScreen(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
