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



class CycleManager:
    # Initializing Object
    def __init__(self, bot, game_ui, battle_manager):
        self.bot = bot
        self.game_ui = game_ui
        self.battle_manager = battle_manager
        self.reset()

    def reset(self):
        self.cycle_type = "cycle_1"
        self.settings = self.bot.save_data.db
        self.yggdrasil_inactive_color = (180, 179, 180)
        self.boss_data = {
            "cooldown_bonus": 15,
            "boss1": 60,
            "boss2": 120,
            "highest_boss_cooldown": 120
        }
        self.boss_cooldown_time = 15
        self.digger_type = "resource_build"
        self.diggers = {
            "resource_build": ["magic_ngu", "energy_ngu"],
            "drop_rate_build": ["drop_chance"]
        }
        self.slots = [2, 3, 4, 5]


    def idleCycle(self, rebirth_time, only_boosts = False):
        loop_start_time = time.time()
        rebirth_time = rebirth_time * 60

        while True:
            loop_start_time = time.time()
            self.harvest()
            #self.capNGULoop(20, "magic")
            time.sleep(0.2)
            self.game_ui.accessMenu("inventory")
            time.sleep(0.2)
            if only_boosts:
                self.bot.gear_manager.applyCubeBoost()
                # self.bot.gear_manager.applySlotBoosts(self.slots)
                # self.bot.gear_manager.upgradeGearPriority()
            else:
                self.bot.gear_manager.upgradeItems(True, 30)

            current_rebirth_time = time.time() - loop_start_time + rebirth_time
            # self.setGearSlot(current_rebirth_time)
            print("Finished upgrade cycle and yggdrasil harvest cycle. Resting 120 seconds")
            self.game_ui.accessMenu("adventure")
            idle_button = self.settings["adventure"]["idle"]
            pyautogui.click(idle_button[0], idle_button[1])
            rest_time = time.time()
            while time.time() - rest_time < 120:
                self.battle_manager.quickKillCycle(None, 10)
            pyautogui.click(idle_button[0], idle_button[1])
            rebirth_time = time.time() - loop_start_time + rebirth_time


    def harvest(self, action = None):
        self.game_ui.accessMenu("inventory")
        time.sleep(0.2)
        if action == "reclaim_magic":
            pyautogui.press("t")
        self.bot.gear_manager.selectGear(0)
        time.sleep(0.2)
        self.bot.gear_manager.equipAccessoryGear(1, 1)
        self.bot.gear_manager.selectGear(2)
        time.sleep(0.2)
        self.yggdrasilHarvest()
        print("Finish harvest")
        time.sleep(0.2)
        self.game_ui.accessMenu("inventory")
        time.sleep(0.2)
        self.bot.gear_manager.selectGear(2)
        self.bot.gear_manager.equipAccessoryGear(1, 1)
        time.sleep(0.2)
        self.bot.gear_manager.selectGear(0)
        time.sleep(0.2)

    def setGearSlot(self, rebirth_time):
        print(rebirth_time)
        largest_boss = self.boss_data["highest_boss_cooldown"] - self.boss_data["cooldown_bonus"]
        reset_time = largest_boss - (int(rebirth_time / 60)  % largest_boss)
        print(reset_time)
        if reset_time <= 5:
            self.bot.gear_manager.assignLoadout("drop_rate_build")
            if self.digger_type == "resource_build":
                self.setDigger("drop_rate_build")
        else:
            self.bot.gear_manager.assignLoadout("resource_build")
            if self.digger_type == "drop_rate_build":
                self.setDigger("resource_build")

    def setDigger(self, digger_type):
        self.game_ui.accessMenu("gold_diggers")
        digger_settings = self.settings["gold_diggers"]
        page_point = digger_settings["page_start"]
        clear_point = digger_settings["clear_button"]
        diggers = []

        for digger in self.diggers[digger_type]:
            diggers.append(digger_settings["digger_info"][digger])

        pyautogui.click(clear_point[0], clear_point[1])
        time.sleep(0.2)

        cap_buttons = digger_settings["cap_buttons"]
        for digger in diggers:
            pyautogui.click(page_point[0] + (digger[0] * 100), page_point[1])
            time.sleep(0.2)
            pyautogui.click(cap_buttons[digger[1]][0], cap_buttons[digger[1]][1])

        self.digger_type = digger_type

    def nguCycle(self):
        self.game_ui.accessMenu("ngu")
        ngu_settings = self.settings["ngu"]
        time.sleep(0.2)
        pyautogui.click(1170, 340)
        time.sleep(0.2)

        '''
        point = ngu_settings["start_power"]
        energy_slot = ngu_settings["energy"]["augment"]
        magic_slot = ngu_settings["magic"]["yggdrasil"]
        swap = ngu_settings["swap"]

        pyautogui.click(point[0], point[1] + (50 * energy_slot)) 
        pyautogui.click(point[0], point[1] + (50 * energy_slot))
        pyautogui.click(swap[0], swap[1])
        time.sleep(0.4)
        pyautogui.click(point[0], point[1] + (50 * magic_slot))
        pyautogui.click(point[0], point[1] + (50 * magic_slot)) 
        pyautogui.click(swap[0], swap[1])
        time.sleep(0.4)
        '''

        print("Finished NGU cycle")

    def yggdrasilHarvest(self):
        yggdrasil_settings = self.settings["yggdrasil"]
        harvest = yggdrasil_settings["harvest_max"]
        fruits = ["luck", "power", "ap", "number"]
        fruits = []

        self.game_ui.accessMenu("yggdrasil")
        time.sleep(0.2)
        pyautogui.click(harvest[0], harvest[1])
        time.sleep(0.2)
        pyautogui.click(harvest[0], harvest[1])

        for fruit in fruits:
            button = yggdrasil_settings[fruit]
            print(fruit)
            print(self.bot.get_pixel_colour(button[0], button[1] - 50))
            if self.bot.get_pixel_colour(button[0], button[1] - 50) == self.yggdrasil_inactive_color:
                self.bot.reclaimResources()
                time.sleep(0.2)
                pyautogui.click(button[0], button[1]) 
    
        print("Harvested yggdrasil and ate available fruits")

    def wandosCycle(self):
        wandos_settings = self.settings["wandos"]
        energy_dump = wandos_settings["energy_dump"]
        magic_dump = wandos_settings["magic_dump"]

        while True:
            self.game_ui.accessMenu("wandos")
            time.sleep(0.2)
            pyautogui.click(energy_dump[0], energy_dump[1])
            pyautogui.click(magic_dump[0], magic_dump[1])

            print("Added wandos sleeping 30 seconds")
            time.sleep(30)

    def timeMachineCycle(self):
        time_machine_settings = self.settings["time_machine"]
        machine_speed = time_machine_settings["machine_speed"]
        gold_speed = time_machine_settings["gold_speed"]

        while True:
            self.game_ui.accessMenu("time_machine")
            time.sleep(0.2)
            pyautogui.click(machine_speed[0], machine_speed[1])
            pyautogui.click(gold_speed[0], gold_speed[1])

            print("Added time machine, sleeping 30 seconds")
            time.sleep(30)

    def capNGULoop(self, Time = None, ngu_type = None):
        self.game_ui.accessMenu("ngu")
        ngu_settings = self.settings["ngu"]

        if ngu_type == "magic":
            swap_button = ngu_settings["swap"]
            pyautogui.click(swap_button[0], swap_button[1])

        if not Time:
            while True:
                pyautogui.click(1170, 340)
                time.sleep(0.1)
        else:
            start_time = time.time()
            print("Runing ngu loop for " + str(Time) + " seconds")
            while time.time() - start_time < Time:
                pyautogui.click(1170, 340)
                time.sleep(0.1)

        print("Finished NGU Cap loop")

    def addPerk(self, upgrade, times):
        itopod = self.settings["itopod"]
        size = itopod["box_size"]
        upgrade = [itopod["box_1"][0] + (size * (upgrade % 12)), itopod["box_1"][1] + (size * int(upgrade/12))]
        confirm_buy = itopod["confirm_buy"]
        for x in range(0, times):
            pyautogui.click(upgrade[0], upgrade[1])
            time.sleep(0.1)
            pyautogui.click(confirm_buy[0], confirm_buy[1])
            time.sleep(0.1)
