import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.save_helper.SaveHelperTemplate import SaveHelperTemplate


class SingleRewardSaveHelper(SaveHelperTemplate):
    # Initializing Object
    def __init__(self, bot):
        super(SingleRewardSaveHelper, self).__init__(bot)
        self.saveActions = [
            self.saveDataSingleReward,
            self.resetMultipleRewardDailies
        ]

    def resetMultipleRewardDailies(self, file):
        server = self.getServerString()
        quests = file[server]["multiple_rewards_progress"]["quests"]

        for quest in quests:
            file[server]["multiple_rewards_progress"]["quests"][quest]["completed"] = False
            file[server]["multiple_rewards_progress"]["quests"][quest]["claimed"] = False
        file[server]["multiple_rewards_progress"]["performed_dailies"] = False
        file[server]["multiple_rewards_progress"]["completed_quests"] = 0

        campaign_progress = file[server]["campaign_progress"]
        for daily in campaign_progress["dailies"]["liberation"]:
            if daily != "locked":
                file[server]["campaign_progress"]["dailies"]["liberation"][daily] = False

        return file

    def saveDataSingleReward(self, file):
        server = self.getServerString()
        data = self.data

        reset_time = data["reset_time"]
        current_time = time.time()

        file[server]["general"]["reset_time"] = reset_time
        file[server]["general"]["current_time"] = current_time
        file[server]["multiple_rewards_progress"]["completed_quests"] = 0

        file[server] = self.resetCampaignDailies(file[server])

        return file

    def resetCampaignDailies(self, file):
        for zone in file["campaign_progress"]["dailies"]:
            print(zone)
            for mission in file["campaign_progress"]["dailies"][zone]:
                print(mission)
                print(file["campaign_progress"]["dailies"])
                if file["campaign_progress"]["dailies"][zone][mission] != "locked":
                    file["campaign_progress"]["dailies"][zone][mission] = False
        return file
