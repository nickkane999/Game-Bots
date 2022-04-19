import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class GuildQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        server = self.db.getServerString()
        data = self.db.data[server]["guild_progress"]
        last_claim_time = data["expeditions"]["upgrade_time"]
        old_renew_time = data["expeditions"]["renew_time"]
        remaining_expeditions = data["expeditions_remaining"]

        current_time = time.time()
        save_time = data["expeditions"]["save_time"]
        passed_time = current_time - save_time

        claim_finished = self.hasEnoughTimePassed(last_claim_time, save_time)
        has_renewed = self.hasEnoughTimePassed(old_renew_time, save_time)
        needs_visit = claim_finished or has_renewed
        if remaining_expeditions <= 0 and not has_renewed:
            needs_visit = False

        results = {
            "expeditions": {
                "needs_visit": needs_visit,
                "has_renewed": has_renewed,
                "upgrade_info": "tbd",
                "server": server
            }
        }

        # print(results)
        return results
