import pyautogui
import time
import re
import sys
import os
import json


class DataHelper:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.db_file = 'C:\\Users\\nickk\\Dropbox\\Portfolio\\Game Bots\\Firestone\\data\\files\\database.json'
        self.image_directory = r"C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\data\files\images"
        self.data = ""

    def refreshData(self):
        db_file = self.db_file
        with open(db_file) as json_file:
            self.data = json.load(json_file)
            json_file.close()

    def saveDataFile(self):
        db_file = self.db_file
        dictionary = self.data
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def saveDataFileRaw(self, dictionary):
        db_file = self.db_file
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def getServerString(self):
        return "server_" + self.data["general"]["current_server"]

    # ---------------------------
    # Save Data functions for other class files
    #----------------------------
    def saveDataSingleReward(self, data, file):
        server = self.getServerString()
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

    def saveFirestone(self, data, file):
        server = self.getServerString()
        save_time = data["save_time"]
        previous_run_save_time = file[server]["firestone_progress"]["upgrades_in_progress"]["save_time"]
        passed_time = save_time - previous_run_save_time

        items = data["items"]
        current_items = file[server]["firestone_progress"]["upgrades_in_progress"]["items"]
        option_data = file[server]["firestone_progress"]["options"]
        item_count = 0
        new_items = {}

        for current_item in current_items:
            current_items[current_item] = current_items[current_item] - passed_time
            print("Remaining time for " + current_item +
                  ": " + str(current_items[current_item]))
            if current_items[current_item] > 0:
                new_items[current_item] = current_items[current_item]
                item_count += 1
        for item in items:
            new_items[item] = items[item]
            print("This item has been added to queue: " + item)
            file[server]["firestone_progress"]["upgrades_in_progress"]["save_time"]
            item_count += 1
            for option in option_data:
                if option_data[option]["name"] == item:
                    option_data[option]["current_level"] += 1
                    if option_data[option]["current_level"] >= option_data[option]["max_level"]:
                        option_data[option]["completed"] = True
            new_items[item] = items[item]
            print("This item has been added to queue: " + item)

        file[server]["firestone_progress"]["upgrades_in_progress"]["save_time"] = save_time
        file[server]["firestone_progress"]["upgrades_in_progress"]["items"] = new_items
        file[server]["firestone_progress"]["upgrades_in_progress"]["count"] = item_count
        file[server]["firestone_progress"]["options"] = option_data

        return file

    def saveMultipleDuties(self, data, file):
        server = data["server"]
        save_time = time.time()

        del data["server"]
        for quest in data:
            name = data[quest]["title"]
            completed = data[quest]["data"]["completed"]
            claimed = data[quest]["data"]["claimed"]
            add_completion = data[quest]["data"]["add_completion"]

            file[server]["multiple_rewards_progress"]["quests"][name]["completed"] = completed
            file[server]["multiple_rewards_progress"]["quests"][name]["claimed"] = claimed
            if add_completion:
                file[server]["multiple_rewards_progress"]["completed_quests"] += 1
        file[server]["multiple_rewards_progress"]["save_time"] = save_time
        return file

    def saveExpeditions(self, data, file):
        server = data["server"]
        save_time = data["current_time"]
        renew_time = data["expedition_reset_time"]
        current_expedition_time = data["expedition_1_time"]
        has_renewed = data["has_renewed"]

        file[server]["guild_progress"]["expeditions"]["save_time"] = save_time
        file[server]["guild_progress"]["expeditions"]["renew_time"] = renew_time
        file[server]["guild_progress"]["expeditions"]["upgrade_time"] = current_expedition_time
        if has_renewed:
            file[server]["guild_progress"]["expeditions_remaining"] = 5

        return file

    def saveServerSwap(self, data, file):
        server = data["current_server"]
        current_time = data["current_time"]

        file["general"]["current_server"] = server
        file["general"]["server_swap_progress"]["last_swap_time"] = current_time

        return file

    def saveMissionsClaimed(self, data, file):
        server = self.getServerString()
        active_missions = data["remaining_missions"]
        new_missions = []

        used_squads = 0
        current_missions = 0

        save_time = file[server]["map_progress"]["stats"]["save_time"]
        current_time = time.time()
        passed_time = current_time - save_time

        if active_missions:
            for mission in active_missions:
                current_missions += 1
                used_squads += mission["squad_cost"]
                mission["time"] = mission["time"] - passed_time

                new_missions.append(mission)

        print("saved active missions")
        print(new_missions)
        file[server]["map_progress"]["missions"]["total_missions"] = current_missions
        file[server]["map_progress"]["missions"]["total_squads"] = used_squads
        file[server]["map_progress"]["missions"]["in_progress"] = new_missions
        file[server]["map_progress"]["stats"]["save_time"] = current_time

        return file

    def saveMissionsStarted(self, data, file):
        server = self.getServerString()
        new_missions_points = data["new_available_points"]
        new_missions = data["missions_selected"]
        used_missions = file[server]["map_progress"]["missions"]["total_missions"]
        used_squads = file[server]["map_progress"]["missions"]["total_squads"]

        current_time = time.time()
        save_time = file[server]["map_progress"]["stats"]["save_time"]
        reset_time = file[server]["map_progress"]["stats"]["reset_time"]
        passed_time = current_time - save_time
        reset_time = reset_time - passed_time

        file[server]["map_progress"]["missions"]["available"] = new_missions_points

        index = 0
        for mission in file[server]["map_progress"]["missions"]["in_progress"]:
            mission_time = file[server]["map_progress"]["missions"]["in_progress"][index]["time"]
            file[server]["map_progress"]["missions"]["in_progress"][index]["time"] = mission_time - passed_time
            index += 1
        for mission in new_missions:
            file[server]["map_progress"]["missions"]["in_progress"].append(
                mission)
            print("adding to mission size:" + str(used_missions))
            print("adding to mission cost:" + str(used_squads))
            used_missions += 1
            used_squads += mission["squad_cost"]
            print("added to mission size:" + str(used_missions))
            print("added to mission cost:" + str(used_squads))

        file[server]["map_progress"]["stats"]["reset_time"] = reset_time
        file[server]["map_progress"]["stats"]["save_time"] = current_time
        file[server]["map_progress"]["missions"]["total_missions"] = used_missions
        file[server]["map_progress"]["missions"]["total_squads"] = used_squads

        print("Mission start data")
        print(file[server]["map_progress"])
        return file

    def saveMissionsPoints(self, data, file):
        server = self.getServerString()
        new_missions = data["found_missions"]
        reset_time = int(data["reset_time"])
        current_time = time.time()

        file[server]["map_progress"]["missions"]["available"] = new_missions
        file[server]["map_progress"]["stats"]["reset_time"] = reset_time
        file[server]["map_progress"]["stats"]["save_time"] = current_time
        return file
