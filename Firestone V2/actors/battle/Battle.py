import pyautogui
import time
import re
import sys
import os

from actors.battle.Party import Party
from actors.battle.HeroFighter import HeroFighter


class Battle:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.battle_screen = bot.data["battle"]

        self.party = Party(bot)
        self.fighter = HeroFighter(bot)
        self.server_swap = bot.server_swap

    def assignParty(self):
        game_bot = self.game_bot
        game_bot.enterZone("party")

        party = self.party
        party.addParty()

    def startHeroFighter(self):
        game_bot = self.game_bot

        fighter = self.fighter
        fighter.startAutoFighting()

    def startBattleDuties(self, battle_settings):
        game_bot = self.game_bot
        fighter = self.fighter

        if (self.conditions.needToAssignParty(battle_settings["active_party"])):
            party = self.party
            party.addParty(battle_settings)
            battle_settings["active_party"] = True
        fighter.startAutoFighting(battle_settings)

        return battle_settings

    def test():
        a = "1"
