import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class MagicQuarterQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        data = self.db.data
        server = self.db.getServerString()
        magic_quarter_data = data[server]["magic_quarter_progress"]
        guardian = magic_quarter_data["priority_guardian"]
        last_upgrade_time = magic_quarter_data["upgrade_time"]

        current_time = time.time()
        save_time = data[server]["magic_quarter_progress"]["save_time"]
        passed_time = current_time - save_time
        needs_upgrade = False
        if (passed_time > int(last_upgrade_time)):
            needs_upgrade = True

        results = {
            "magic_quarter": {
                "needs_upgrade": needs_upgrade,
                "upgrade_info": {
                    "guardian_slot": "guardian_" + str(guardian)
                },
                "server": server
            }
        }

        # print(results)
        return results
