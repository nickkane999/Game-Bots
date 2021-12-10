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