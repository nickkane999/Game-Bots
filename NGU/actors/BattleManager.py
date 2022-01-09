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



class BattleManager:
    # Initializing Object
    def __init__(self, bot, game_ui):
        self.bot = bot
        self.game_ui = game_ui
        self.reset()

    def reset(self):
        self.cycle_type = "cycle_1"
        self.settings = self.bot.save_data.db["adventure"]
        self.cooldown = 0.60
        self.states = {
            "unavailable_row_1": (124, 78, 78),
            "available_row_1": (248, 155, 155),
            "unavailable_row_2": (51, 68, 82),
            "available_row_2": (102, 135, 163),
            "unavailable_row_3": (98, 74, 74),
            "available_row_3": (195, 148, 148),
            "hp_low": (176, 175, 176),
            "hp_high": (236, 52, 52),
            "enemy_dead": (160, 160, 160)
        }
        self.cooldowns = self.bot.save_data.db["adventure"]["cooldowns_start"]
        self.healthPoint = self.bot.save_data.db["adventure"]["hp"]
        self.defensive_rotate_buttons = ["block", "paralyze"]
        self.use_defense = True

    def get_pixel_colour(self, i_x, i_y):
        i_desktop_window_id = win32gui.GetDesktopWindow()
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
        i_colour = int(long_colour)
        win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
        return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

    def adventureCycle(self, offensive = False):
        if offensive:
            self.use_defense = False 
        start_time = time.time()        
        defensive_buttons = ["defense_buff", "regen", "heal", "parry"]
        offensive_buttons = ["charge", "ultimate_attack", "pierce"]
        heavy_attack = ["offense_buff", "ultimate_buff", "charge", "ultimate_attack", "pierce"]
        normal_attacks = ["strong", "regular"]
        arrow_left = self.settings["arrow_left"]
        arrow_right = self.settings["arrow_right"]

        home_menu_color = (160, 160, 160)
        exploder_color = False
        count = 0

        while True:
            current_time = time.time()
            if self.get_pixel_colour(1250, 710) == home_menu_color:
                print("Died. Getting health for 10 seconds")
                time.sleep(10)
                for x in range(0, 19):
                    pyautogui.click(arrow_right[0], arrow_right[1])
                    time.sleep(0.2)

            if self.get_pixel_colour(1250, 710) == exploder_color:
                print ("found exploder")
                while self.get_pixel_colour(1250, 710) == exploder_color:
                    print ("looping through exploder")
                    self.processButtons(offensive_buttons, True)
                    self.processButtons(heavy_attack, True)
                    self.processButtons(normal_attacks, True)
            else:
                if self.lowHealth():
                    self.processButtons(defensive_buttons)
                if self.getState("offense_buff") and self.getState("ultimate_buff"):
                    self.processButtons(heavy_attack)
                else: 
                    self.processButtons(offensive_buttons)
                self.processButtons(normal_attacks)

    def processButtons(self, buttons, exploder = False):
        for button in buttons:
            point = self.getPoint(button)
            if self.getState(button, point):
                self.clickButton(point)
                print("Clicked " + button)
        if not exploder and self.use_defense:
            self.defenseRotation(self.defensive_rotate_buttons)
        #print("Enemy ID")
        #print(self.get_pixel_colour(1250, 710))

    def defenseRotation(self, buttons):
        defense_point = self.getPoint(buttons[0])
        defense_available = self.getState(buttons[0], defense_point)
        paralyze_point = self.getPoint(buttons[1])
        paralyze_available = self.getState(buttons[1], paralyze_point)

        if (defense_available and paralyze_available) or defense_available:
            self.clickButton(defense_point)
            print("Clicked " + buttons[0])
        elif paralyze_available:
            self.clickButton(paralyze_point)
            print("Clicked " + buttons[1])

    def getState(self, button, point = None):
        if not point:
            point = self.getPoint(button)
        color = self.get_pixel_colour(point[0], point[1])
        if (color == self.states["available_row_1"] or color == self.states["available_row_2"] or color == self.states["available_row_3"]):
            return True
        else:
            return False

    def lowHealth(self):
        point = self.healthPoint
        color = self.get_pixel_colour(point[0], point[1])
        if (color == self.states["hp_low"]):
            return True
        else:
            return False


    def getPoint(self, button):
        button = self.settings["buttons"][button]
        point = self.settings["first_button"]
        button_adjustment = self.settings["button_space"]
        point = [point[0] + (button_adjustment[0] * button[0]), point[1] + (button_adjustment[1] * button[1])]
        return point

    def clickButton(self, point):
        pyautogui.click(point[0], point[1])
        time.sleep(self.cooldown + 0.3)

    def quickKillCycle(self, click_times = None, kill_count = None):
        enemy_hp_point = [1600, 720]
        regular_attack = [1000, 267]
        strong_attack = [1160, 267]
        pierce_attack = [1480, 267]
        ultimate_attack = [1640, 267]
        count = 0
        if not kill_count:
            kill_count = 10000

        while True:
            if self.get_pixel_colour(enemy_hp_point[0], enemy_hp_point[1]) == self.states["hp_high"]:
                if click_times:
                    attacks = 0
                    while attacks < click_times:
                        if (self.get_pixel_colour(ultimate_attack[0], ultimate_attack[1]) == self.states["available_row_1"])
                            pyautogui.press("y")
                            attacks += 1
                        if (self.get_pixel_colour(pierce_attack[0], pierce_attack[1]) == self.states["available_row_1"])
                            pyautogui.press("t")
                            attacks += 1
                        if (self.get_pixel_colour(regular_attack[0], regular_attack[1]) == self.states["available_row_1"]):
                            pyautogui.press("w")
                            attacks += 1
                        if (self.get_pixel_colour(strong_attack[0], strong_attack[1]) == self.states["available_row_1"]):
                            pyautogui.press("e")
                            attacks += 1
                    time.sleep(1)
                    pyautogui.press("g")
                    pyautogui.press("h")
                    pyautogui.press("f")
                else:
                    pyautogui.press("w")
                count += 1
                print("Kill count: " + str(count))
            time.sleep(0.1)
            if count >= kill_count:
                break
        print("Finished kills")