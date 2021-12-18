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



class RebirthManager:
    # Initializing Object
    def __init__(self, bot, game_ui):
        self.bot = bot
        self.game_ui = game_ui
        self.reset()

    def reset(self):
        self.settings = self.bot.save_data.db
        self.sleep_time = 0.1
        self.diggers = ["wandos", "stat"]
        self.augment = "energy_buster"
        self.gear = {
            "chest": 0,
            "accessory": 1,
            "head": 2,
            "weapon": 3
        }
        self.bood_type = "blood_4"
        self.cycle_time = 600
        self.open_adventure_color = (57, 61, 60)
        self.retrieve_augments = False
        self.actions = {
            "augment": self.assignAugments,
            "set_augment_reclaim_flag": self.updateAugmentFlag,
            "time_machine": self.timeMachineCycle,
            "blood": self.setBlood,
            "wandos": self.wandosCycle,
            "reclaim": self.bot.reclaimResource,
            "adventure": self.setAdventureZone,
            "start_itopod": self.startItopod,
            "nuke": self.nukeBoss,
            "attack": self.attackBoss,
            "digger": self.setDiggers,
            "select_gear_slot": self.changeGearSlot,
            "select_gear": self.selectGear,
            "apply_boost": self.bot.gear_manager.applyCubeBoost
        }
        self.cycle_data = [
            {
                "time": 60,
                "pre_cycle": [],
                "order": [
                    "nuke",
                    ["once", [
                        ["select_gear_slot", ["drop_rate_build"]],
                        "adventure",
                        ["augment", [7, self.augment]],
                        "nuke",
                        ["adventure", ["increment"]]
                    ]],
                    "reclaim",
                    ["time_machine", [10]]
                ]
            },
            {
                "time": 75,
                "pre_cycle": [
                    "reclaim",
                    ["augment", [3, self.augment, True]],
                    "reclaim",
                    ["augment", [3, self.augment]],
                    "reclaim",
                    "digger"
                ],
                "order": [
                    "nuke",
                    ["once_delay", [1, [
                        ["adventure", ["increment"]],
                    ]]],
                    ["time_machine", [10]],
                ]
            },
            {
                "time": 90,
                "pre_cycle": [
                    ["select_gear_slot", ["resource_build"]],
                    "start_itopod"
                ],
                "order": [
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 50,
                "pre_cycle": [
                    ["select_gear", [self.gear["chest"]]],
                    ["select_gear", [self.gear["weapon"]]]
                ],
                "order": [
                    ["time_machine", [10]],
                    "nuke"
                ]
            },
            {
                "time": 70,
                "pre_cycle": [
                    ["reclaim", [True]]
                ],
                "order": [
                    ["blood", ["blood_5"]],
                    "nuke",
                    ["time_machine", [5, "energy"]],
                ]
            },            
            {
                "time": 110,
                "pre_cycle": [],
                "order": [
                    "reclaim",
                    ["augment", [3, self.augment, True]],
                    "reclaim",
                    ["augment", [8, self.augment]],
                    ["blood", ["blood_5"]],
                    "nuke",
                ]
            },
            {
                "time": 110,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["head"]]],
                    ["digger", [False]],
                    ["set_augment_reclaim_flag", [True]],   
                ],
                "order": [
                    ["wandos", [2]],
                    ["rotate", [
                        ["augment", [1, self.augment]],
                        ["augment", [1, self.augment, True]]
                    ]]
                ]
            },
            {
                "time": 2,
                "pre_cycle": [
                    "reclaim",
                    ["reclaim", [True]],
                    ["select_gear", [self.gear["accessory"]]],
                    ["select_gear", [self.gear["head"]]],
                    ["select_gear", [self.gear["weapon"]]],
                    "apply_boost",
                    ["digger", [False]],
                    ["set_augment_reclaim_flag", [False]],
                    ["wandos", [1]],
                    "nuke",
                    "attack"
                ],
                "order": []
            },

        ]

    def idleCycle(self):
        current_time = time.time()
        loop_time = current_time
        '''
        while True:
            self.enterRebirth()
        '''
        while True:
            cycle_index = 0
            for cycle in self.cycle_data:
                self.processCycle(cycle)
                cycle_index += 1
                print("Finished cycle " + str(cycle_index))
            self.enterRebirth()
            # self.retrieve_augments = False

    def processCycle(self, info):
        # print(info)
        start_time = time.time()
        cycle_time = info["time"]
        pre_cycle = info["pre_cycle"]
        order = info["order"]

        self.flags = {
            "once": True,
            "once_delay": True,
        }

        if pre_cycle:
            # print("Pre cycle")
            self.processActions(pre_cycle)

        self.cycle_count = 0
        if order:
            # print("Order")
            while time.time() - start_time < cycle_time:
                self.processActions(order)
                self.cycle_count += 1

 
    def processActions(self, actions):
        special_actions = ["once", "once_delay", "rotate"]

        for item in actions:
            if isinstance(item, list) and item[0] in special_actions:
                self.runActionSpecial(item)
            else:
                self.runAction(item)

    def runAction(self, action):
        # print("Running action")
        # print(action)
        if isinstance(action, list):
            function = action[0]
            parameters = action[1]
            self.actions[function](parameters)
        else:
            self.actions[action]()

    def runActionSpecial(self, action):
        # print(action)
        if action[0] == "once" and self.cycle_count < 1 and self.flags["once"]:
            # print("Once action")
            for sub_action in action[1]:
                self.runAction(sub_action)
            self.flags["once"] = False
        if action[0] == "once_delay" and self.cycle_count == action[1][0] and self.flags["once_delay"]:
            # print("Once delay")
            for sub_action in action[1][1]:
                self.runAction(sub_action)
            self.flags["once_delay"] = False
        if action[0] == "rotate":
            selected_action = self.cycle_count % len(action[1])
            # print("Rotate")
            self.runAction(action[1][selected_action])
        
        print("Special Action Ran")

    def nukeBoss(self):
        self.game_ui.accessMenu("fight_boss")
        time.sleep(0.2)
        nuke = self.settings["fight_boss"]["nuke"]
        fight = self.settings["fight_boss"]["fight"]
        self.click(nuke)
        self.click(fight)
        print("Nuked and attacked boss boss")

    def attackBoss(self):
        self.game_ui.accessMenu("fight_boss")
        time.sleep(0.2)
        fight = self.settings["fight_boss"]["fight"]
        for x in range(0, 6):
            self.click(fight)
            time.sleep(2)

    def changeGearSlot(self, info):
        slot = info[0]

        #resource_build = 0, drop_rate_build = 1
        self.game_ui.accessMenu("inventory")
        time.sleep(0.2)
        self.bot.gear_manager.assignLoadout(slot)
        print("Changed gear slot")

    def assignAugments(self, info):
        set_time = info[0]
        augment = self.assignListIndex(info, "all", 1)
        is_strong = self.assignListIndex(info, False, 2)

        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("augmentation")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            if self.retrieve_augments:
                self.bot.augmentation_manager.retrieveEnergy(augment)
            self.bot.augmentation_manager.assignEnergy(augment, is_strong)
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding augments")

    def setAdventureZone(self, info = None):
        my_type = info

        self.game_ui.accessMenu("adventure")
        menu = self.bot.battle_manager.settings
        arrow_left = menu["arrow_left"]
        arrow_right = menu["arrow_right"]
        if my_type == "low":
            for x in range(0, 12):
                self.click(arrow_right)
        elif my_type == "increment":
            for x in range(0, 5):
                self.click(arrow_right)
        else:
            for x in range(0, 20):
                self.click(arrow_right)
        
        time.sleep(5)
        if self.get_pixel_colour(1160, 640) == self.open_adventure_color:
            self.click(arrow_left)

        print("Set adventure zone")

    def startItopod(self):
        self.game_ui.accessMenu("adventure")
        menu = self.bot.battle_manager.settings

        self.click(menu["itopod_start"])
        self.click(menu["itopod_optimal"])
        self.click(menu["itopod_confirm"])

        print("Set ITOPOD")


    def setDiggers(self, info = None):
        clear = info

        self.game_ui.accessMenu("gold_diggers")
        digger_settings = self.settings["gold_diggers"]
        page_point = digger_settings["page_start"]
        clear_point = digger_settings["clear_button"]
        diggers = []

        for digger in self.diggers:
            diggers.append(digger_settings["digger_info"][digger])

        if clear:
            self.click(clear_point)

        cap_buttons = digger_settings["cap_buttons"]
        for digger in diggers:
            self.click([page_point[0] + (digger[0] * 100), page_point[1]])
            self.click([cap_buttons[digger[1]][0], cap_buttons[digger[1]][1]])

        print("Assigned diggers with new caps")

    def wandosCycle(self, info):
        set_time = info[0]
        dump = self.assignListIndex(info, "all", 1)

        wandos_settings = self.settings["wandos"]
        energy_dump = wandos_settings["energy_dump"]
        magic_dump = wandos_settings["magic_dump"]
        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("wandos")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            self.game_ui.accessMenu("wandos")
            if dump != "energy":
                self.click(magic_dump)
            if dump != "magic":
                self.click([energy_dump[0] + 100, energy_dump[1]])
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding wandos")

    def timeMachineCycle(self, info):
        set_time = info[0]
        machine = self.assignListIndex(info, "all", 1)

        time_machine_settings = self.settings["time_machine"]
        machine_speed = time_machine_settings["machine_speed"]
        gold_speed = time_machine_settings["gold_speed"]
        current_time = time.time()
        loop_time = current_time
        self.game_ui.accessMenu("time_machine")
        time.sleep(0.2)

        while loop_time - current_time < set_time:
            self.game_ui.accessMenu("time_machine")
            if machine != "energy":
                self.click(gold_speed)
            if machine != "magic":
                self.click(machine_speed)
            loop_time = time.time()
            time.sleep(0.5)
        print("Finished adding time machine")

    def setBlood(self, info):
        blood_type = info[0]

        self.game_ui.accessMenu("blood_magic")
        blood_settings = self.settings["blood"]
        start_point = blood_settings["blood_start"]
        distance = blood_settings["distance"]
        self.click([start_point[0], start_point[1] + (blood_settings["info"][blood_type] * distance)])
        print("Set blood")

    def selectGear(self, info):
        gear = info[0]

        self.game_ui.accessMenu("inventory")
        time.sleep(1)
        self.bot.gear_manager.selectGear(gear)
        print("Set gear slot")

    def enterRebirth(self):
        self.click(self.settings["rebirth"]["enter_menu"])
        self.click(self.settings["rebirth"]["rebirth_start"])
        time.sleep(3)
        self.click(self.settings["rebirth"]["rebirth_confirm_start"])
        print("Entered Rebirth")

    def click(self, point, rest_time = None):
        pyautogui.click(point[0], point[1])
        if not rest_time:
            time.sleep(self.sleep_time)
        else:
            time.sleep(rest_time)

    def updateAugmentFlag(self, info):
        status = info[0]

        self.retrieve_augments = status
        print("Updated Augment flag")

    def assignListIndex(self, info, alt_value, index):
        if len(info) > index: 
            return info[1]
        else:
            return alt_value


    def get_pixel_colour(self, i_x, i_y):
        i_desktop_window_id = win32gui.GetDesktopWindow()
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
        i_colour = int(long_colour)
        win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
        return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)