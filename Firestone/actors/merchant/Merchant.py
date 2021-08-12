import pyautogui
import time
import re
import sys
import os


class Merchant:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.item_options = bot.screenshot_data.data["merchant"]
        self.item_slots = {
            1: "Scroll of Speed",
            2: "Scroll of Damage",
            3: "Scroll of Health",
            4: "Midas' Touch",
            5: "Pouch of Gold",
            6: "Bucket of Gold",
            7: "Crate of Gold",
            8: "Pile of Gold",
            9: "War Banner",
            10: "Dragon Armor",
            11: "Guardian's Rune",
            12: "Totem of Agony",
            13: "Totem of Annihilation",
        }

        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.merchant_screen = bot.data["merchant"]

    def moveMenuHalfDown(self):
        pyautogui.click(1860, 820)
        pyautogui.dragTo(1860, 190, 3, button='left')
        time.sleep(4)

    def moveMenuUp(self):
        pyautogui.click(1860, 300)
        pyautogui.dragTo(1860, 900, 1, button='left')
        pyautogui.click(1860, 300)
        pyautogui.dragTo(1860, 900, 2, button='left')
        time.sleep(2)

    def moveFirestoneMenuSlightUp(self):
        pyautogui.click(1500, 200)
        pyautogui.dragTo(1800, 200, 0.5, button='left')

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def completeQuest(self, times_completed):
        self.game_bot.db.refreshData()
        self.server = self.game_bot.db.getServerString()
        self.coordinates = self.merchant_screen["icons"]

        self.enterMerchantZone()
        self.updateQuantities()
        self.buyItems(times_completed)
        self.returnToBattleScreen()

    def updateQuantities(self):
        game_bot = self.game_bot
        screenshot_helper = game_bot.screenshot_helper
        items = self.item_options
        item_data = {
            "item_1": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_1"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_1"])
            },
            "item_2": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_2"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_2"])
            },
            "item_3": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_3"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_3"])
            },
            "item_4": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_4"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_4"])
            },
            "item_5": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_5"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_5"])
            },
            "item_6": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_6"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_6"])
            },
        }
        self.moveMenuHalfDown()
        item_menu2_data = {
            "item_7": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_7"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_7"])
            },
            "item_8": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_8"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_8"])
            },
            "item_9": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_9"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_9"])
            },
            "item_10": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_10"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_10"])
            },
            "item_11": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_11"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_11"])
            },
            "item_12": {
                "title": screenshot_helper.getScreenshotTime(items["item_title_12"]),
                "quantity": screenshot_helper.getScreenshotTime(items["item_quantity_12"])
            },
        }
        item_data.update(item_menu2_data)
        print(item_data)
        self.saveData(item_data)
        self.moveMenuUp()

    def buyItems(self, times_completed):
        bot = self.game_bot
        coordinates = self.merchant_screen["icons"]
        server = self.server

        items = self.game_bot.db.data[server]["merchant_progress"]["items"]
        times_to_complete = 10 - times_completed
        processed_items = self.item_slots
        current_item_slot = 1
        current_item = processed_items[current_item_slot]
        current_quantity = items[current_item]

        while (times_to_complete > 0):
            self.game_bot.click(coordinates[current_item])
            print("Clicked on " + current_item)
            current_quantity -= 1
            times_to_complete -= 1
            print("Current quantity: " + str(current_quantity))
            if (current_quantity <= 0):
                current_item_slot += 1
                current_item = processed_items[current_item_slot]
                current_quantity = items[current_item]

    def getAvailableItems(self, items, buy_amount):
        item_queue = []
        for name, value in items:
            print("Name: " + name + ". Value: " + str(value))
            item_queue.append(name)
            remaining_buy_amount = buy_amount - value
            if remaining_buy_amount <= 0:
                return item_queue

        return item_queue

    def saveData(self, items):
        server = self.server
        for item in items:
            name = items[item]["title"]
            quantity = int(items[item]["quantity"])
            print(name)
            self.game_bot.db.data[server]["merchant_progress"]["items"][name] = quantity
        self.game_bot.db.saveDataFile()

    def enterMerchantZone(self):
        bot = self.game_bot
        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["merchant"])
        self.moveMenuUp()

    def returnToBattleScreen(self):
        bot = self.game_bot
        coordinates = self.coordinates

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])
        time.sleep(2)
