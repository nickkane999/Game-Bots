import pyautogui
import time
import re
import sys
import os


class Tavern:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.tavern_screen = bot.data["tavern"]

    def completeQuest(self, times_completed):
        self.game_bot.db.refreshData()
        queue_processor = self.game_bot.queue_processor
        self.coordinates = self.tavern_screen["icons"]
        times_to_play = 10 - times_completed

        mission_completion_amount = 10
        times_to_complete = mission_completion_amount - times_completed
        token_data = {
            "region": (1565, 17, 50, 40),
            "image": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\tavern_tokens.png',
            "type": "token-number",
            "msg": "Token's Available ",
        }

        self.enterTavernZone()

        tokens = self.game_bot.screenshot_helper.getScreenshotTime(token_data)
        print("Current tokens: " + tokens)
        tokens = int(tokens)

        if (tokens == 0):
            self.buyTokens(2) if (tokens <= 4) else self.buyTokens(1)
        self.playGame(times_to_play)
        self.returnToBattleScreen()

    def enterTavernZone(self):
        self.game_bot.click(self.battle_screen["icons"]["town"])
        self.game_bot.click(self.town_screen["icons"]["tavern"])

    def buyTokens(self, amount):
        bot = self.game_bot
        coordinates = self.coordinates
        print("Pressing token buy button this many times: " + str(amount))
        bot.click(coordinates["tavern_play_buy"])

        for x in range(amount):
            bot.click(coordinates["buy_tokens"])
        bot.click(coordinates["x_icon"])

    def playGame(self, times_to_play):
        bot = self.game_bot
        coordinates = self.coordinates

        for x in range(times_to_play):
            bot.click(coordinates["tavern_play_buy"])
            time.sleep(0.5)
            bot.click(coordinates["card_1"])
            time.sleep(0.5)

    def returnToBattleScreen(self):
        self.game_bot.click(self.coordinates["x_icon"])
        self.game_bot.click(self.coordinates["x_icon"])
