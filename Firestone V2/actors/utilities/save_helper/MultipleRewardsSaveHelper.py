import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class MultipleRewardsSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(MultipleRewardsSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveMultipleDuties
        ]

    def saveMultipleDuties(self, file):
        server = self.getServerString()
        data = self.data
        save_time = time.time()

        del data["server"]
        for quest in data:
            name = data[quest]["title"]
            completed = data[quest]["data"]["completed"]
            claimed = data[quest]["data"]["claimed"]
            add_completion = data[quest]["data"]["add_completion"]

            file[server]["multiple_rewards_progress"]["quests"][name]["completed"] = completed
            file[server]["multiple_rewards_progress"]["quests"][name]["claimed"] = claimed
            if add_completion:
                file[server]["multiple_rewards_progress"]["completed_quests"] += 1
        file[server]["multiple_rewards_progress"]["save_time"] = save_time
        return file
