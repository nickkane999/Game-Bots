import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class MagicQuarterSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(MagicQuarterSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveMagicQuarterData,
        ]

    def saveMagicQuarterData(self, file):
        server = self.getServerString()
        data = self.data

        file[server]["magic_quarter_progress"]["upgrade_time"] = data["time_for_upgrade"]
        file[server]["magic_quarter_progress"]["save_time"] = time.time()

        return file
