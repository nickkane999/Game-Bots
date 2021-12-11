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
    def __init__(self, bot, game_ui):
        self.bot = bot
        self.game_ui = game_ui
        self.reset()

    def reset(self):
        self.cycle_type = "cycle_1"
        self.settings = self.bot.save_data.db
        self.yggdrasil_inactive_color = (180, 179, 180)

    def idleCycle(self, cycle_time):
        reset_time = time.time()
        while True:
            if (time.time() - reset_time) > cycle_time * 60:
                self.yggdrasilHarvest()
            self.nguCycle()
            self.game_ui.accessMenu("inventory")
            time.sleep(0.2)
            self.bot.gear_manager.upgradeItems(True, 30)
            print("Finished upgrade cycle and yggdrasil harvest cycle. Resting 20 seconds")
            time.sleep(1)


    def nguCycle(self):
        self.game_ui.accessMenu("ngu")
        ngu_settings = self.settings["ngu"]
        time.sleep(0.2)

        energy = ngu_settings["power"]
        magic = ngu_settings["yggdrasil"]
        swap = ngu_settings["swap"]

        pyautogui.click(energy[0], energy[1]) 
        pyautogui.click(magic[0], magic[1])
        pyautogui.click(swap[0], swap[1])
        time.sleep(0.2)
        pyautogui.click(energy[0], energy[1]) 
        pyautogui.click(magic[0], magic[1])
        pyautogui.click(swap[0], swap[1])
        time.sleep(0.2)

        print("Finished NGU cycle")

    def yggdrasilHarvest(self):
        yggdrasil_settings = self.settings["yggdrasil"]
        harvest = yggdrasil_settings["harvest_max"]
        fruits = ["luck", "power", "ap"]

        self.game_ui.accessMenu("yggdrasil")
        time.sleep(0.2)
        pyautogui.click(harvest[0], harvest[1])
        time.sleep(0.2)
        pyautogui.click(harvest[0], harvest[1])

        for fruit in fruits:
            button = yggdrasil_settings[fruit]
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
