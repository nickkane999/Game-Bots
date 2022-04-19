import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class CampaignSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(CampaignSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveCampaignProgress
        ]

    def saveCampaignProgress(self, file):
        data = self.data
        server = data["server"]
        claim_time = int(data["campaign_claim_time"])

        file[server]["campaign_progress"]["campaign_claim_time"] = claim_time
        file[server]["campaign_progress"]["save_time"] = data["current_time"]

        return file
