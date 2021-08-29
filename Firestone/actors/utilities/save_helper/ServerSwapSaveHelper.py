import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class ServerSwapSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(ServerSwapSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveServerSwap
        ]

    def saveServerSwap(self, file):
        data = self.data
        server = data["current_server"]
        current_time = time.time()

        file["general"]["current_server"] = server
        file["general"]["server_swap_progress"]["last_swap_time"] = current_time

        return file
