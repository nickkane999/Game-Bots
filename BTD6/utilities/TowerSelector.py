import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np


class TowerSelector():
    # Initializing Object
    def __init__(self):
        self.current_menu = "menu_one"
        self.menu_one = self.getMenuOneTowersDeflation()
        self.menu_two = self.getMenuTwoTowersDeflation()
        self.empty_point = {"x": 80, "y": 1040}

    def getMenuOneTowersDeflation(self):
        towers = {
            "hero": {"x": 1710, "y": 220},
            "dart monkey": {"x": 1820, "y": 220},
            "boomerang monkey": {"x": 1710, "y": 350},
            "bomb shooter": {"x": 1820, "y": 350},
            "tack shooter": {"x": 1710, "y": 500},
            "ice monkey": {"x": 1820, "y": 500},
            "glue gunner": {"x": 1710, "y": 620},
            "sniper monkey": {"x": 1820, "y": 620},
            "monkey sub": {"x": 1710, "y": 750},
            "monkey buccaneer": {"x": 1820, "y": 750},
            "monkey ace": {"x": 1710, "y": 900},
            "heli pilot": {"x": 1820, "y": 900},
        }
        return towers

    def getMenuTwoTowersDeflation(self):
        towers = {
            "motar monkey": {"x": 1710, "y": 350},
            "dartling monkey": {"x": 1820, "y": 350},
            "wizard monkey": {"x": 1710, "y": 500},
            "super monkey": {"x": 1820, "y": 500},
            "ninja monkey": {"x": 1710, "y": 620},
            "alchemist": {"x": 1820, "y": 620},
            "druid": {"x": 1710, "y": 750},
            "spike factory": {"x": 1820, "y": 750},
            "monkey village": {"x": 1710, "y": 900},
            "engineer monkey": {"x": 1820, "y": 900},
        }
        return towers

    def getMenuOneTowers(self):
        towers = {
            "hero": {"x": 1710, "y": 220},
            "dart monkey": {"x": 1820, "y": 220},
            "boomerang monkey": {"x": 1710, "y": 350},
            "bomb shooter": {"x": 1820, "y": 350},
            "tack shooter": {"x": 1710, "y": 500},
            "ice monkey": {"x": 1820, "y": 500},
            "glue gunner": {"x": 1710, "y": 620},
            "sniper monkey": {"x": 1820, "y": 620},
            "monkey sub": {"x": 1710, "y": 750},
            "monkey buccaneer": {"x": 1820, "y": 750},
            "monkey ace": {"x": 1710, "y": 900},
            "heli pilot": {"x": 1820, "y": 900},
        }
        return towers

    def getMenuTwoTowers(self):
        towers = {
            "motar monkey": {"x": 1710, "y": 220},
            "dartling monkey": {"x": 1820, "y": 220},
            "wizard monkey": {"x": 1710, "y": 350},
            "super monkey": {"x": 1820, "y": 350},
            "ninja monkey": {"x": 1710, "y": 500},
            "alchemist": {"x": 1820, "y": 500},
            "druid": {"x": 1710, "y": 620},
            "banana farm": {"x": 1820, "y": 620},
            "spike factory": {"x": 1710, "y": 750},
            "monkey village": {"x": 1820, "y": 750},
            "engineer monkey": {"x": 1710, "y": 900},
        }
        return towers

    def selectTower(self, monkey):
        menu_one = self.menu_one
        menu_two = self.menu_two
        current_menu = self.current_menu
        empty_point = self.empty_point

        if (monkey in menu_one):
            monkey_point = menu_one[monkey]
            print("selecting monkey " + monkey)
            if (current_menu == "menu_two"):
                self.moveMenu()
        if (monkey in menu_two):
            print("selecting monkey " + monkey)
            monkey_point = menu_two[monkey]
            if (current_menu == "menu_one"):
                self.moveMenu()
        if (monkey_point):
            pyautogui.click(empty_point["x"], empty_point["y"])
            pyautogui.click(monkey_point["x"], monkey_point["y"])

    def placeTower(self, monkey, point):
        self.selectTower(monkey)
        pyautogui.click(point["x"], point["y"])

    def moveMenu(self):
        current_menu = self.current_menu
        self.moveMenuUp() if (current_menu == "menu_two") else self.moveMenuDown()

    def moveMenuUp(self):
        pyautogui.click(1710, 180)
        pyautogui.dragTo(1710, 900, 1, button='left')
        pyautogui.click(1710, 180)
        pyautogui.dragTo(1710, 900, 1, button='left')
        time.sleep(2)
        self.current_menu = "menu_one"

    def moveMenuDown(self):
        pyautogui.click(1710, 900)
        pyautogui.dragTo(1710, 180, 1, button='left')
        pyautogui.click(1710, 900)
        pyautogui.dragTo(1710, 180, 1, button='left')
        time.sleep(2)
        self.current_menu = "menu_two"
