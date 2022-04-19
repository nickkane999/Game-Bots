import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class SingleRewardQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        server = self.db.getServerString()
        single_reward_data = self.db.data[server]["general"]
        reset_time = single_reward_data["reset_time"]
        save_time = single_reward_data["current_time"]
        needs_visit = self.hasEnoughTimePassed(reset_time, save_time)

        results = {
            "single_reward": {
                "needs_visit": needs_visit,
            }
        }

        # print(results)
        return results
