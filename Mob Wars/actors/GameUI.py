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

class GameUI:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.xpaths = self.bot.save_data.db["xpaths"]

    def loopBattleRoyal(self, loop_counter):
        print("Looping battle royal")
