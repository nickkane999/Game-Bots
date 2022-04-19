import pyautogui
import time
import re
import sys
import os


class Party:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot
        self.party_screen = bot.data["party"]
        self.battle_screen = bot.data["battle"]

    # Major object functions
    def addParty(self, battle_settings):
        captain_slot = battle_settings["captain_slot"]
        self.buyPartySlots()
        self.assignPartyMembers()
        self.assignCaptain(captain_slot)
        self.saveAndExit()

    def buyPartySlots(self):
        bot = self.game_bot
        party_coordinates = self.party_screen["icons"]
        battle_coordinates = self.battle_screen["icons"]

        bot.click(battle_coordinates["party"])
        bot.click(party_coordinates["party_1"])
        bot.click(party_coordinates["party_2"])
        bot.click(party_coordinates["party_3"])
        bot.click(party_coordinates["party_4"])
        bot.click(party_coordinates["party_5"])

    def assignPartyMembers(self):
        bot = self.game_bot
        party_coordinates = self.party_screen["icons"]

        party_members_point1 = party_coordinates["column1_row1"]
        party_members_point2 = party_coordinates["column2_row1"]
        self.addMembersByColumn(party_members_point2)
        self.addMembersByColumn(party_members_point1)

    def addMembersByColumn(self, column_start_point):
        bot = self.game_bot
        coordinate_x = column_start_point["x"]
        coordinate_y = column_start_point["y"]

        for x in range(1, 6):
            point = {"x": coordinate_x, "y": coordinate_y}
            bot.click(point)
            coordinate_y = coordinate_y + 200

    def assignCaptain(self, slot):
        bot = self.game_bot
        party_coordinates = self.party_screen["icons"]
        slot = "party_" + str(slot)

        bot.click(party_coordinates["choose_leader"])
        bot.click(party_coordinates[slot])

    def saveAndExit(self):
        bot = self.game_bot
        party_coordinates = self.party_screen["icons"]

        save = party_coordinates["save_icon"]
        bot.click(save)
        exit = party_coordinates["x_icon"]
        bot.click(exit)
