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


class GameUI:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.reset()

    def accessMenu(self, name):
        menu = self.menu_settings
        position = menu["positions"][name]
        point = menu["menu_start"]
        box = menu["box_size"]
        point = [point[0], point[1] + (position * box[1])]
        pyautogui.click(point[0], point[1])
        time.sleep(0.2)

    def startRebirth(self):
        menu = self.menu_settings
        rebirth_point = menu["rebirth"]
        rebirth_2_point = menu["rebirth_2"]
        rebirth_confirm_point = menu["rebirth_confirm"]

        pyautogui.click(rebirth_point[0], rebirth_point[1])
        time.sleep(0.2)
        pyautogui.click(rebirth_2_point[0], rebirth_2_point[1])
        time.sleep(0.2)
        pyautogui.moveTo(rebirth_confirm_point[0], rebirth_confirm_point[1])
        time.sleep(0.2)        

    def reset(self):
        self.menu_settings = self.bot.save_data.db["menu"]
        self.cycle_count = 0

