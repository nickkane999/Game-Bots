import pyautogui
import time
import re
import sys
import os
import win32gui

from actors.utilities.ConditionManager import ConditionManager

class Bot:

    # Initializing Object
    def __init__(self, info):
        self.data = info["zones_data"]
        self.conditions = info["conditions"]
        self.db = info["db"]
        self.screenshot_helper = info["screenshot_helper"]
        self.screenshot_data = info["screenshot_data"]

        self.queue_processor = info["queue_processor"]
        self.queue_processor.game_bot = None

        # self.run_actions = ["single_reward", "multiple_rewards"]
        # self.run_actions = ["library", "single_reward", "multiple_rewards"]
        # self.run_actions = ["library", "single_reward",
        #                    "multiple_rewards", "magic_quarter", "campaign", "guild", "server_swap", "map"]
        # self.run_actions = ["single_reward", "multiple_rewards", "magic_quarter", "campaign", "guild", "map", "server_swap"]
        # self.run_actions = ["library"]
        self.run_actions = ["Guild", "Campaign",
                            "MagicQuarter", "MultipleRewards", "SingleReward"]
        # run_actions = ["startup", "guild", "library", "campaign", "temple", "battle"]
        # run_actions = ["library", "magic_quarter"]
        # run_actions = ["magic_quarter", "guild"]
        # run_actions = ["campaign", "guild", "magic_quarter"]
        # run_actions = ["multiple_rewards"]

    def click(self, point):
        pyautogui.moveTo(point["x"], point["y"])
        pyautogui.moveTo(point["x"], point["y"])
        pyautogui.click(point["x"], point["y"])
        print("Clicked at " + str(point["x"]) + ", " + str(point["y"]))

    def setData(self, actors, timer):
        self.actors = actors
        self.timer = timer
        self.actions = timer.data["actions"]

    def updateTimerActions(self):
        self.timer["area"]

    def start(self):
        # self.setupGame()
        self.timer.startTimer()
        time.sleep(0.2)
        # self.actions["startup"]["has_ran"] = True
        self.runAutoBuild()

    def setupGame(self):
        startup_action_settings = self.actions["startup"]["action_settings"]
        self.timer.startTimer()
        time.sleep(0.2)

        actions = self.actions
        updated_startup_action_settings = actions["startup"]["start_function"](
            startup_action_settings)
        self.actions["startup"]["action_settings"] = updated_startup_action_settings

    def runAutoBuild(self):
        actions = self.actions
        timer = self.timer
        conditions = self.conditions

        while (True):
            for zone, action in actions.items():
                if (conditions.skipAction(action, zone)):
                    print("Action ran once and is being skipped: " + zone)
                else:
                    current_time = timer.getCurrentTime()
                    print("Zone Name: " + zone + ". Curent Time: " + str(current_time) + ". Rotation Time: " +
                          str(action["rotation_time"] * action["times_performed"]))
                    if (conditions.needToPerformAction(current_time, action)):
                        action_data = action["action_settings"]
                        new_action_data = action["start_function"](action_data)

                        print("Action has been processed: " + zone)
                        self.actions[zone]["times_performed"] = actions[zone]["times_performed"] + 1
                        self.actions[zone]["action_settings"] = new_action_data

    def assignSeverSwap(self, server_swap):
        self.server_swap = server_swap


# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------

    def startQueue(self):
        print("I've started running")
        actions = self.queue_processor.actions
        run_actions = self.run_actions
        while True:
            for item in actions:
                if item in run_actions:
                    print("Processing action: " + item)
                    actions[item]()
                    print("Action finished processing: " + item)
                else:
                    print("Not processing action: " + item)
            break

    def get_pixel_color(self, i_x, i_y):
        i_desktop_window_id = win32gui.GetDesktopWindow()
        i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
        long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
        i_colour = int(long_colour)
        win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
        return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

    def test(self):
        print("testing bot 123")
