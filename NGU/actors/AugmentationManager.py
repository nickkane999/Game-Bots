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



class AugmentationManager:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.reset()

    def reset(self):
        self.settings = self.bot.save_data.db["augmentation"]
        self.cycle_count = 0
        self.priority = "energy_buster"

    def assignEnergy(self):
        self.cycle_count = self.cycle_count + 1
        
        menu = self.settings
        point = menu["scroll_bottom"]
        pyautogui.click(point[0], point[1])
        time.sleep(0.2)

        point = menu["energy_buster"]
        if self.cycle_count % 5 == 0:
            pyautogui.click(point[0], point[1] + menu["aug_adjustment"])
        else:
            pyautogui.click(point[0], point[1])
