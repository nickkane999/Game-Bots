import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class MultipleRewardsQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        server = self.db.getServerString()
        multiple_rewards_data = self.db.data[server]["multiple_rewards_progress"]

        reset_time = multiple_rewards_data["check_interval"]
        save_time = multiple_rewards_data["save_time"]
        needs_visit = self.hasEnoughTimePassed(reset_time, save_time)
        performed_dailies = multiple_rewards_data["performed_dailies"]

        completed_quests_amount = multiple_rewards_data["completed_quests"]
        total_quest_amount = multiple_rewards_data["total_quests"]
        if completed_quests_amount >= total_quest_amount:
            needs_visit = False
        else:
            performed_dailies = False

        results = {
            "multiple_rewards": {
                "needs_visit": needs_visit,
                "performed_dailies": performed_dailies,
                "upgrade_info": "tbd",
                "server": server,
                "times_checked": 3
            }
        }

        # print(results)
        return results
