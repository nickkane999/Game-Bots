import pyautogui
import time
import re
import sys
import os

from actors.library.Firestone import Firestone
from actors.library.Meteorite import Meteorite


class Library:
    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.library_screen = bot.data["library"]

        self.firestone = Firestone(bot)
        self.meteorite = Meteorite(bot)

    def startLibraryDuties(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor
        library_coordinates = self.library_screen["icons"]
        db = game_bot.db

        instructions = queue_processor.verifyQueueLibrary(db)
        conditions = {
            "meteorite_upgrade": instructions["meteorite"]["needs_upgrade"],
            "firestone_upgrade": instructions["firestone"]["needs_upgrade"],
        }
        needs_visit = conditions["meteorite_upgrade"] or conditions["firestone_upgrade"]
        print(instructions)

        if needs_visit:
            self.enterLibraryZone()

        if conditions["meteorite_upgrade"]:
            # action tbd
            test = 123
        if conditions["firestone_upgrade"]:
            self.firestone.processFirestonesQueue(instructions["firestone"])
            # self.performFirestoneMaintenance(library_coordinates, instructions)

    def verifyNeeds(self):
        data = self.game_bot.db.data
        server = "server_" + data["general"]["current_server"]
        active_library_upgrades = data[server]["firestone_progress"]["upgrades_in_progress"]["count"]
        return active_library_upgrades

    def enterLibraryZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["library"])

    def performFirestoneMaintenance(self, coordinates, instructions):
        self.firestone.assignQueueData(coordinates, instructions)
        firestone = self.firestone
        firestone.processFirestonesQueue()

    def returnToBattleScreen(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
        print("done")
