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



class TimeMachineManager:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.reset()

    def reset(self):
        self.settings = self.bot.save_data.db["time_machine"]

    def add(self, section):
        menu = self.bot.save_data.db["time_machine"]
        point = menu[section]
        pyautogui.click(point[0], point[1])
        time.sleep(0.2)
    
    def lower(self, section):
        menu = self.bot.save_data.db["time_machine"]
        point = menu[section]
        pyautogui.click(point[0] + 50, point[1])
        time.sleep(0.2)
