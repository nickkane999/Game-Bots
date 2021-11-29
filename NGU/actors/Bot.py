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

# from commonFunctions import *
# from SegmentedData import *
from actors.GearManager import GearManager
from actors.GameUI import GameUI
from actors.TimeMachineManager import TimeMachineManager
from actors.AugmentationManager import AugmentationManager

class Bot:
    # Initializing Object
    def __init__(self, data):
        self.instructions = data['instructions']
        self.save_data = data['save_data']

        self.gear_manager = GearManager(self)
        self.game_ui = GameUI(self)
        self.time_machine_manager = TimeMachineManager(self)
        self.augmentation_manager = AugmentationManager(self)
        
        self.phase_count = 0

    def startCycle(self):
        self.current_cycle_time = time.time()

        self.game_ui.startRebirth()
        print("10 seconds before cycle starts")
        time.sleep(5)

        self.setBasicTraining()
        self.fightBosses()
        #self.setLoadout(1)
        self.phase_count = 0
        
        while (time.time() - self.current_cycle_time < 900):
            self.rebirthPhaseOne()
            self.phaseCheck()
        self.phase_count = 0

        while (time.time() - self.current_cycle_time < 1800):
            self.rebirthPhaseTwo()
            self.phaseCheck()
        self.phase_count = 0

    def rebirthPhaseOne(self):
        self.setTimeMachine()
        print("Time machine set in phase 1 rebirth cycle. Sleeping 60 seconds")
        self.phase_count = self.phase_count + 1
        time.sleep(60)

    def rebirthPhaseTwo(self):
        self.setAugmentation(True)
        self.setTimeMachine()
        print("Phase 2 rebirth cycle complete. Sleeping 60 seconds")
        self.phase_count = self.phase_count + 1
        time.sleep(60)

    def phaseCheck(self):
        if self.phase_count % 5 == 0:
            self.fightBosses()


    def setTimeMachine(self, reclaim = False):
        if reclaim:
            self.reclaimResources()
        self.game_ui.accessMenu("time_machine")
        self.time_machine_manager.add("machine_speed")
        self.time_machine_manager.add("gold_speed")

    def setBasicTraining(self):
        menu = self.save_data.db["basic_training"]
        self.game_ui.accessMenu("basic_training")
        attack_point = menu["attack_1"]
        defense_point = menu["defense_1"]

        time.sleep(1)
        pyautogui.click(attack_point[0], attack_point[1])
        time.sleep(1)
        pyautogui.click(defense_point[0], defense_point[1])

    def fightBosses(self):
        menu = self.save_data.db["fight_boss"]
        self.game_ui.accessMenu("fight_boss")
        time.sleep(0.2)
        nuke = menu["nuke"]
        fight = menu["fight"]
        pyautogui.click(nuke[0], nuke[1])
        time.sleep(6)
        for x in range(0, 4):
            pyautogui.click(fight[0], fight[1])
            time.sleep(3)

    def setLoadout(self, loadout):
        self.game_ui.accessMenu("inventory")
        self.gear_manager.swapLoadout(loadout)

    def setAugmentation(self, reclaim = False):
        if reclaim:
            self.reclaimResources()
        self.game_ui.accessMenu("augmentation")
        self.augmentation_manager.assignEnergy()


    def reclaimResources(self):
        pyautogui.press("r")
        pyautogui.press("t")