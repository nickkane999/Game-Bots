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
from actors.GameUI import GameUI



class GearManager:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.GameUI = GameUI(bot)
        self.reset()

    def reset(self):
        self.slot_priority = "head"
        self.gear_settings = self.bot.save_data.db["gear"]
        self.transform_color = "yellow"
        self.method = "upgrade"
        self.cycle_count = 0

    def get_pixel_colour(self, i_x, i_y):
        i_desktop_window_id = win32gui.GetDesktopWindow()
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
        i_colour = int(long_colour)
        win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
        return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

    def getGearSlotPoint(self, slot):
        slot_position = self.gear_settings["positions"][slot]
        grid_start = self.gear_settings["positions"]["grid_start"]
        point = {
            "x": grid_start[0] + (75 * (slot_position % 3) ),
            "y": grid_start[1] + (75 * math.trunc(slot_position / 3) )
        }
        return point

    def getInventorySlotPoint(self, slot):
        grid_start = self.gear_settings["inv_grid_start"]
        point = {
            "x": grid_start[0] + (75 * (slot % 12) ),
            "y": grid_start[1] + (75 * math.trunc(slot / 12) )
        }
        return point

    def upgradeItems(self, is_reversed = False):
        start_time = time.time()
        gear_points = self.getGearPoints()
        inventory_points = self.getInventoryPoints()

        self.cycle_count = 0
        while True:
            self.cycle_count = self.cycle_count + 1;
            if is_reversed:
                self.clickSlots(gear_points)
                self.mergeSlots(gear_points)
                self.clickSlots(inventory_points)
                self.mergeSlots(inventory_points)                
                self.clearInventory()
            if not is_reversed:
                self.clearInventory()
                self.clickSlots(gear_points)
                self.mergeSlots(gear_points)
                self.clickSlots(inventory_points)
                self.mergeSlots(inventory_points)                
            print("Cycle for upgrading items completed. Sleeping 30 seconds")
            print(time.time() - start_time)
            time.sleep(30)
            


    def getGearPoints(self):
        slot_priority = self.gear_settings["gear_slot_priority"]
        ordered_points = []
        for slot in slot_priority:
            point = self.getGearSlotPoint(slot)
            ordered_points.append(point)
        return ordered_points

    def getInventoryPoints(self):
        start_time = time.time()
        slot_priority = self.gear_settings["inventory_slot_priority"]
        ordered_points = []
        for slot in slot_priority:
            point = self.getInventorySlotPoint(slot)
            ordered_points.append(point)
        return ordered_points

    def upgradeGear(self, slot):
        point = self.getGearSlotPoint(slot)
        pyautogui.click(point["x"], point["y"])
        time.sleep(1)
        
        while True:
            self.clickSlot(point)
            self.clearInventory()

    def upgradeGearPriority(self):
        start_time = time.time()
        slot_priority = self.gear_settings["gear_slot_priority"]
        ordered_slot_points = []
        for slot in slot_priority:
            point = self.getGearSlotPoint(slot)
            ordered_slot_points.append(point)

        while True:
            for point in ordered_slot_points:
                self.clickSlot(point)
            self.clearInventory()
            print("Cycle for upgrading gear completed")
            print(time.time() - start_time)

    def upgradeInventoryPriority(self):
        start_time = time.time()
        slot_priority = self.gear_settings["inventory_slot_priority"]
        ordered_slot_points = []
        for slot in slot_priority:
            point = self.getInventorySlotPoint(slot)
            ordered_slot_points.append(point)

        while True:
            for point in ordered_slot_points:
                self.clickSlot(point)
            self.clearInventory()
            print("Cycle for upgrading gear completed")
            print(time.time() - start_time)

    def clickSlots(self, points):
        pyautogui.keyDown("a")
        time.sleep(0.2)
        for point in points:
            for x in range(0, 4):
                pyautogui.click(point["x"], point["y"])
                time.sleep(0.1)
        pyautogui.keyUp("a")
        time.sleep(0.2)

    def mergeSlots(self, points):
        pyautogui.keyDown("d")
        time.sleep(0.2)
        for point in points:
            for x in range(0, 2):
                pyautogui.click(point["x"], point["y"])
                time.sleep(0.1)
        pyautogui.keyUp("d")
        time.sleep(0.2)

    def clickSlot(self, point):
        pyautogui.keyDown("a")
        time.sleep(0.3)
        for x in range(0, 10):
            pyautogui.click(point["x"], point["y"])
            time.sleep(0.1)
        pyautogui.keyUp("a")
        time.sleep(0.3)

    def mergeSlot(self, point):
        pyautogui.keyDown("d")
        time.sleep(0.3)
        pyautogui.click(point["x"], point["y"])
        time.sleep(0.1)
        pyautogui.keyUp("d")
        time.sleep(0.3)

    def clearInventory(self):
        start_slot = self.gear_settings["start_slot"]
        grid_start = self.gear_settings["inv_grid_start"]
        grid = self.gear_settings["grid"]
        start_point = {
            "x": grid_start[0] + (75 * (start_slot % 12) ), 
            "y": grid_start[1] + (75 * math.trunc(start_slot / 12) )
        }
        grid_size = grid[0] * grid[1]
        pyautogui.click(start_point["x"], start_point["y"])

        pyautogui.keyDown("ctrl")
        time.sleep(0.3)
        for current_slot in range(0, grid_size):
            point = {
                "x": start_point["x"] + (75 * (current_slot % grid[0]) ),
                "y": start_point["y"] + (75 * math.trunc(current_slot / grid[1]) )
            }
            if self.get_pixel_colour(point["x"], point["y"]) == (238, 238, 188):
                pyautogui.keyUp("ctrl")
                self.transformColor(point)
                pyautogui.keyDown("ctrl")
            else:
                pyautogui.click(point["x"], point["y"])
                time.sleep(0.1)
        pyautogui.keyUp("ctrl")
        time.sleep(0.3)

    def transformColor(self, point):
        color_key = self.gear_settings["colors"][self.transform_color]
        pyautogui.keyDown(color_key)
        pyautogui.click(point["x"] - 10, point["y"])
        pyautogui.keyUp(color_key)