import pyautogui
import time
import re
import sys
import os
import copy

from data.actors.FirestoneData import FirestoneData


class FirestoneQueueHelper:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.data_requirements = FirestoneData()

    def assignData(self, data):
        self.data = data

    def getFirestoneInstructions(self):
        data = self.data
        upgrade_count = self.getUpgradeCount()
        if upgrade_count <= 0:
            results = {"needs_upgrade": False}
            return results

        sorted_upgrades = self.getSortedUpgrades()
        exclude_list = self.buildExcludeList()
        upgrade_priority = self.getUpgradePriority()
        upgrade_priority = self.removeExcludeListRecordsPriority(
            upgrade_priority, exclude_list)

        available_upgrades = self.removeExcludeListRecordsUpgrades(
            sorted_upgrades, exclude_list)
        selected_upgrades = self.createSelectedUpgrades(
            upgrade_priority, available_upgrades)

        available_upgrades = self.getAvailableUpgrades(sorted_upgrades)

        items = data["upgrades_in_progress"]["items"]
        tier = data["current_tier"]

        unlocked_levels = data["unlocked_levels"]
        set_upgrades = data["set_upgrades"]
        available_upgrades = []
        all_upgrades_unlocked = data["unlocked_levels"]["all_unlocked"]
        needs_upgrade = upgrade_count > 0

        results = {
            "tier": tier,
            "server": server,
            "needs_upgrade": needs_upgrade,
            "all_upgrades_unlocked": all_upgrades_unlocked,
            "upgrade_amount": upgrade_count,
            "sorted_options": sorted_options,
            "available_upgrades": available_upgrades
        }

        return results

    def getUpgradeCount(self):
        processing_upgrades = self.data["upgrades_in_progress"]["items"]
        save_time = self.data["upgrades_in_progress"]["save_time"]
        current_time = time.time()
        passed_time = current_time - save_time

        count = 0
        for upgrade in processing_upgrades:
            if processing_upgrades[upgrade] >= passed_time:
                count += 1

        return count

    def getSortedUpgrades(self):
        options = self.data["options"]
        sorted_options = sorted(options, key=lambda option: option["priority"])
        return sorted_options

    def getAvailableUpgrades(self):
        unlocked_levels = self.data["unlocked_levels"]

        sys.exit()

        return available_upgrades

    def buildExcludeList(self):
        exclude_list = self.addUnavailableSets()
        exclude_list = self.addInProgressItems(exclude_list)
        return exclude_list

    def addUnavailableSets(self):
        unlocked_levels = self.data["unlocked_levels"]
        exclude_list = []
        current_tier = "tier_" + str(self.data["current_tier"])
        set_upgrades = self.data_requirements.data["requirements"][current_tier]

        for level in unlocked_levels:
            if level != "all_unlocked" and not unlocked_levels[level]:
                for upgrade in set_upgrades[level]:
                    exclude_list.append(upgrade)

        return exclude_list

    def removeExcludeListRecordsPriority(self, upgrade_priority, exclude_list):
        if len(upgrade_priority) > 0:
            new_upgrade_priority = copy.deepcopy(upgrade_priority)
            index = 0
            for upgrade in upgrade_priority:
                if upgrade in exclude_list:
                    del new_upgrade_priority[index]
                    index -= 1
                index += 1

        return upgrade_priority

    def removeExcludeListRecordsUpgrades(self, upgrades, exclude_list):
        available_upgrades = copy.deepcopy(upgrades)
        index = 0
        for upgrade in upgrades:
            # print(upgrade["name"])
            # print(sorted_upgrades[index])
            if upgrade["name"] in exclude_list:
                #print("upgrade has been excluded")
                # print(upgrade["name"])
                del available_upgrades[index]
                index -= 1
            index += 1
        # print("New sorted upgrades")
        # print(available_upgrades)
        return available_upgrades

    def createSelectedUpgrades(self, upgrade_priority, available_upgrades):
        selected_upgrades = []

        count = 0
        for name in upgrade_priority:
            for upgrade in available_upgrades:
                if upgrade["name"] == name:
                    selected_upgrades.append(upgrade)
                    count += 1
                if count >= 2:
                    break
            if count >= 2:
                break

        return selected_upgrades

    def getUpgradePriority(self):
        current_tier = "tier_" + str(self.data["current_tier"])
        set_upgrades = self.data_requirements.data["requirements"][current_tier]
        unlocked_levels = self.data["unlocked_levels"]
        priority_upgrades = []
        count = 0
        set_priority = self.data_requirements.priority

        for level in set_priority:
            if unlocked_levels[level]:
                for upgrade in set_upgrades[level]:
                    priority_upgrades.append(upgrade)
                    count += 1

        print("New priority upgrades")
        print(priority_upgrades)

        return priority_upgrades

    def addInProgressItems(self, exclude_list):
        processing_upgrades = self.data["upgrades_in_progress"]["items"]
        save_time = self.data["upgrades_in_progress"]["save_time"]
        current_time = time.time()
        passed_time = current_time - save_time

        for upgrade in processing_upgrades:
            if processing_upgrades[upgrade] >= passed_time:
                exclude_list.append(upgrade)

        return exclude_list

    def getUnlockOrder(self):
        server = self.db.getServerString()
        data = self.db.data[server]["firestone_progress"]

        items = data["upgrades_in_progress"]["items"]
        tier = data["current_tier"]

        unlocked_levels = data["unlocked_levels"]
        set_upgrades = data["set_upgrades"]
        options = data["options"]
        sorted_options = sorted(options, key=lambda option: option["priority"])
        available_upgrades = []
        all_upgrades_unlocked = data["unlocked_levels"]["all_unlocked"]

        upgrade_order = self.getUnlockOrder()

        save_time = data["upgrades_in_progress"]["save_time"]
        passed_time = time.time() - save_time
        print("passed time")
        print(passed_time)

        exclude_list = []
        for item in items:
            print("item remaining time")
            print(items[item])
            if items[item] >= passed_time:
                exclude_list.append(item)

        if len(exclude_list) < 2:
            needs_upgrade = True
            for level in unlocked_levels:
                if unlocked_levels[level]:
                    for upgrade in set_upgrades[level]:
                        if upgrade not in exclude_list:
                            available_upgrades.append(upgrade)

        upgrades_available = 2 - len(exclude_list)
        needs_upgrade = upgrades_available > 0

        results = {
            "tier": tier,
            "server": server,
            "needs_upgrade": needs_upgrade,
            "all_upgrades_unlocked": all_upgrades_unlocked,
            "upgrade_amount": upgrades_available,
            "sorted_options": sorted_options,
            "available_upgrades": available_upgrades
        }

        return results
