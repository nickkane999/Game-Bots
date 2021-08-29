import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class CampaignQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        data = self.db.data
        server = self.db.getServerString()
        campaign_data = data[server]["campaign_progress"]
        last_claim_time = campaign_data["campaign_claim_time"]
        save_time = campaign_data["save_time"]

        needs_visit = self.hasEnoughTimePassed(last_claim_time, save_time)
        results = {
            "campaign": {
                "needs_visit": needs_visit,
                "upgrade_info": "tbd",
                "server": server
            }
        }

        # print(results)
        return results
