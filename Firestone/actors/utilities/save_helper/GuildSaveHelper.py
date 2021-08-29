import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class GuildSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(GuildSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveExpeditions
        ]

    def saveExpeditions(self, file):
        data = self.data
        server = data["server"]
        save_time = data["current_time"]
        renew_time = data["expedition_reset_time"]
        current_expedition_time = data["expedition_1_time"]
        has_renewed = data["has_renewed"]

        file[server]["guild_progress"]["expeditions"]["save_time"] = save_time
        file[server]["guild_progress"]["expeditions"]["renew_time"] = renew_time
        file[server]["guild_progress"]["expeditions"]["upgrade_time"] = current_expedition_time
        if has_renewed:
            file[server]["guild_progress"]["expeditions_remaining"] = 5

        return file
