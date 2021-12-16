from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import selenium
import time
import os
import glob
import shutil
from time import sleep
import json
import sys
import math
import win32gui



class RebirthManager:
    # Initializing Object
    def __init__(self, bot, game_ui):
        self.bot = bot
        self.game_ui = game_ui
        self.reset()

    def reset(self):
        self.settings = self.bot.save_data.db
        self.sleep_time = 0.1
        self.diggers = ["wandos", "stat"]
        self.augment = "energy_buster"
        self.gear = {
            "chest": 0,
            "accessory": 1
        }
        self.bood_type = "blood_4"
        self.cycle_time = 600

    def idleCycle(self):
        current_time = time.time()
        loop_time = current_time

        while True:
            rebirth_time = 0
            rebirth_start_time = time.time()

            adventure_zone_set = False
            while time.time() - rebirth_start_time < 60:
                self.nukeBoss()
                if not adventure_zone_set:
                    self.changeGearSlot("drop_rate_build")
                    self.setAdventureZone("low")
                    self.assignAugments(13, self.augment)
                    self.nukeBoss()
                    time.sleep(2)
                    self.setAdventureZone("increment")
                    self.bot.reclaimResource(True)
                    adventure_zone_set = True
                self.timeMachineCycle(10)
            
            print("Finished Cycle 1")
            sub_cycle_count = 0
            new_adventure_zone_set = False
            while time.time() - rebirth_start_time < 120:
                self.nukeBoss()
                if not new_adventure_zone_set and sub_cycle_count >= 1:
                    self.setAdventureZone("increment")
                    self.setDiggers()
                    new_adventure_zone_set = True
                if sub_cycle_count >= 2:
                    self.changeGearSlot("resource_build")
                self.bot.reclaimResource(True)
                self.assignAugments(2, self.augment, True)
                self.bot.reclaimResource(True)
                self.assignAugments(6, self.augment)
                self.bot.reclaimResource(True)
                self.timeMachineCycle(12)
                sub_cycle_count = sub_cycle_count + 1

            print("Finished Cycle 2")
            while time.time() - rebirth_start_time < 270:
                self.timeMachineCycle(10)
                self.nukeBoss()
                
            print("Finished Cycle 3")
            self.selectGear(self.gear["chest"])
            while time.time() - rebirth_start_time < 300:
                self.timeMachineCycle(10)
                self.nukeBoss()

            print("Finished Cycle 4")
            self.bot.reclaimResource(False)
            while time.time() - rebirth_start_time < 360:
                self.setBlood("blood_4")
                self.nukeBoss()
                self.timeMachineCycle(5, "energy")
                time.sleep(5)

            print("Finished Cycle 5")
            while time.time() - rebirth_start_time < 480:
                self.bot.reclaimResource(True)
                self.assignAugments(3, self.augment, True)
                self.bot.reclaimResource(True)
                self.assignAugments(9, self.augment)
                self.setBlood("blood_4")
                self.nukeBoss()
                time.sleep(5)

            print("Finished Cycle 6")
            self.bot.reclaimResource(True)
            self.bot.reclaimResource(False)
            self.selectGear(self.gear["accessory"])
            self.setDiggers(False)
            while time.time() - rebirth_start_time < 590:
                self.wandosCycle(10)
                self.nukeBoss()
                time.sleep(5)

            self.bot.reclaimResource(True)
            self.bot.reclaimResource(False)
            self.selectGear(self.gear["accessory"])
            self.attackBoss()
            
            print("Finished cycle. Restarting")
            self.enterRebirth()

    def nukeBoss(self):
        self.game_ui.accessMenu("fight_boss")
        time.sleep(0.2)
        nuke = self.settings["fight_boss"]["nuke"]
        self.click(nuke)
        print("Nuked boss")

    def attackBoss(self):
        self.game_ui.accessMenu("fight_boss")
        time.sleep(0.2)
        fight = self.settings["fight_boss"]["fight"]
        for x in range(0, 8):
            self.click(fight)
            time.sleep(2)

    def changeGearSlot(self, slot):
        #resource_build = 0, drop_rate_build = 1
        self.game_ui.accessMenu("inventory")
        time.sleep(0.2)
        self.bot.gear_manager.assignLoadout(slot)
        print("Changed gear slot")

    def assignAugments(self, set_time, augment, is_strong = False):
        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("augmentation")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            self.bot.augmentation_manager.assignEnergy(augment, is_strong)
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding augments")

    def setAdventureZone(self, my_type = None):
        self.game_ui.accessMenu("adventure")
        menu = self.bot.battle_manager.settings
        arrow_left = menu["arrow_left"]
        arrow_right = menu["arrow_right"]
        if my_type == "low":
            for x in range(0, 12):
                self.click(arrow_right)
            self.click(arrow_left)
        elif my_type == "increment":
            for x in range(0, 5):
                self.click(arrow_right)
        else:
            for x in range(0, 20):
                self.click(arrow_right)
        print("Set adventure zone")

    def setDiggers(self, clear = True):
        self.game_ui.accessMenu("gold_diggers")
        digger_settings = self.settings["gold_diggers"]
        page_point = digger_settings["page_start"]
        clear_point = digger_settings["clear_button"]
        diggers = []

        for digger in self.diggers:
            diggers.append(digger_settings["digger_info"][digger])

        if clear:
            self.click(clear_point)

        cap_buttons = digger_settings["cap_buttons"]
        for digger in diggers:
            self.click([page_point[0] + (digger[0] * 100), page_point[1]])
            self.click([cap_buttons[digger[1]][0], cap_buttons[digger[1]][1]])

        print("Assigned diggers with new caps")

    def wandosCycle(self, set_time, dump = "all"):
        wandos_settings = self.settings["wandos"]
        energy_dump = wandos_settings["energy_dump"]
        magic_dump = wandos_settings["magic_dump"]
        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("wandos")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            self.game_ui.accessMenu("wandos")
            if dump != "energy":
                self.click(magic_dump)
            if dump != "magic":
                self.click(energy_dump)
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding wandos")

    def timeMachineCycle(self, set_time, machine = "all"):
        time_machine_settings = self.settings["time_machine"]
        machine_speed = time_machine_settings["machine_speed"]
        gold_speed = time_machine_settings["gold_speed"]
        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("time_machine")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            self.game_ui.accessMenu("time_machine")
            if machine != "energy":
                self.click(gold_speed)
            if machine != "magic":
                self.click(machine_speed)
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding time machine")

    def setBlood(self, blood_type):
        self.game_ui.accessMenu("blood_magic")
        blood_settings = self.settings["blood"]
        start_point = blood_settings["blood_start"]
        distance = blood_settings["distance"]
        self.click([start_point[0], start_point[1] + (blood_settings["info"][blood_type] * distance)])
        print("Set blood")

    def selectGear(self, gear):
        self.game_ui.accessMenu("inventory")
        time.sleep(1)
        self.bot.gear_manager.selectGear(gear)
        print("Set gear slot")

    def enterRebirth(self):
        self.click(self.settings["rebirth"]["enter_menu"])
        self.click(self.settings["rebirth"]["rebirth_start"])
        time.sleep(3)
        self.click(self.settings["rebirth"]["rebirth_confirm_start"])
        print("Entered Rebirth")

    def click(self, point, rest_time = None):
        pyautogui.click(point[0], point[1])
        if not rest_time:
            time.sleep(self.sleep_time)
        else:
            time.sleep(rest_time)