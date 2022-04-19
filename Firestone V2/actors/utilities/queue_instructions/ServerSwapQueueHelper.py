import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class ServerSwapQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        server = self.db.getServerString()
        server_swap_data = self.db.data["general"]["server_swap_progress"]

        swap_time = server_swap_data["swap_options"]["short"]
        save_time = server_swap_data["last_swap_time"]
        needs_swap = self.hasEnoughTimePassed(swap_time, save_time)

        results = {"needs_swap": needs_swap, }
        print("Time since last swap: " + str(time.time() - save_time))

        results = {
            "server_swap": {
                "needs_swap": needs_swap,
            }
        }

        # print(results)
        return results
