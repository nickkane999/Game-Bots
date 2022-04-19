import pyautogui
import time
import re
import sys
import os


class ConditionManager:

    # Initializing Object
    def __init__(self):
        self.zone = "123"

    def skipAction(self, action, zone):
        # skipped_zones = ["library", "startup", "guild", "campaign", "temple"]
        # skipped_zones = ["library", "startup", "guild", "campaign", "battle"]
        # skipped_zones = ["library", "startup", "temple"]
        skipped_zones = ["startup", "guild", "campaign", "temple", "server_swap"]
        in_skipped_zone = (zone in skipped_zones)
        # print(action)
        has_ran_once = ("run_once" in action["action_settings"] and (
            action["action_settings"]["run_once"] and action["action_settings"]["has_ran"]))

        # print(action["has_ran"])
        # print(has_ran_once)

        return has_ran_once or in_skipped_zone

    def needToPerformAction(self, current_time, action):
        cycle_time = action["rotation_time"] * action["times_performed"]

        return current_time > cycle_time

    def needToAssignParty(self, active_party):
        return not active_party

    def shouldResetTemple(self, firestone_results, temple_settings):
        time_firestone_level_reached = temple_settings["time_firestone_level_reached"]
        goal_met = firestone_results["goal_met"]
        early_reset = firestone_results["early_reset"]
        enough_time_passed = (time.time(
        ) - temple_settings["time_firestone_level_reached"]) > temple_settings["reset_time_requirement"]

        if (early_reset or (enough_time_passed and goal_met)):
            return True
        else:
            return False
