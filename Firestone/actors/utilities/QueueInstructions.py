import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np


class QueueInstructions:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.zone = ""

    def assignActorActions(self, actors):
        for k, v in actors.items():
            actors[k].game_bot = None

        self.actors = actors
        self.defineQueueActions()

    def defineQueueActions(self):
        actors = self.actors
        self.actions = {
            "startup": actors["startup"].runStartup,
            "guild": actors["guild"].startGuildDuties,
            "library": actors["library"].startLibraryDuties,
            "campaign": actors["campaign"].startCampaignDuties,
            "temple": actors["temple"].startTempleDuties,
            "battle": actors["battle"].startBattleDuties,
        }

    def getQueueInstructionsFirestone(self, firestone):
        data = self.data
        server = "server_" + data["general"]["current_server"]
        active_upgrades = data[server]["firestone_progress"]["upgrades_in_progress"]["count"]
        items = data[server]["firestone_progress"]["upgrades_in_progress"]["items"]
        tier = data[server]["firestone_progress"]["current_tier"]

        current_time = time.time()
        save_time = data[server]["firestone_progress"]["upgrades_in_progress"]["save_time"]
        passed_time = current_time - save_time

        upgrade_limit = 2
        upgrades_available = upgrade_limit - active_upgrades
        needs_upgrade = False
        upgrade_info = None

        if active_upgrades > 0:
            for item, last_upgrade_time in items.items():
                if (passed_time > int(last_upgrade_time)):
                    needs_upgrade = True
                    upgrades_available += 1
        if upgrades_available > 0:
            needs_upgrade = True
            upgrade_info = firestone.getUpgradeInstructions(upgrades_available)

        results = {
            "needs_upgrade": needs_upgrade,
            "upgrade_info": upgrade_info,
            "upgrade_amount": upgrades_available,
            "tier": tier,
            "server": server
        }

        return results

    def getQueueInstructionsMagicQuarter(self, magic_quarter):
        data = self.data
        server = "server_" + data["general"]["current_server"]
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
            "needs_upgrade": needs_upgrade,
            "upgrade_info": {
                "guardian_slot": "guardian_" + str(guardian)
            },
            "server": server
        }

        return results

    def getQueueInstructionsExpeditions(self, guild):
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
            "needs_visit": needs_visit,
            "has_renewed": has_renewed,
            "upgrade_info": "tbd",
            "server": server
        }

        # print(results)
        return results

    def getQueueInstructionsCampaign(self, campaign):
        data = self.data
        server = "server_" + data["general"]["current_server"]
        campaign_data = data[server]["campaign_progress"]
        last_claim_time = campaign_data["campaign_claim_time"]
        save_time = campaign_data["save_time"]

        needs_visit = self.hasEnoughTimePassed(last_claim_time, save_time)
        results = {
            "needs_visit": needs_visit,
            "upgrade_info": "tbd",
            "server": server
        }

        # print(results)
        return results

    def getQueueInstructionsMultipleRewards(self, multiple_rewards):
        server = self.db.getServerString()
        multiple_rewards_data = self.db.data[server]["multiple_rewards_progress"]

        reset_time = multiple_rewards_data["check_interval"]
        save_time = multiple_rewards_data["save_time"]
        needs_visit = self.hasEnoughTimePassed(reset_time, save_time)
        performed_dailies = multiple_rewards_data["performed_dailies"]

        completed_quests_amount = multiple_rewards_data["completed_quests"]
        total_quest_amount = multiple_rewards_data["total_quests"]
        if completed_quests_amount >= total_quest_amount:
            needs_visit = False
        else:
            performed_dailies = False

        results = {
            "needs_visit": needs_visit,
            "performed_dailies": performed_dailies,
            "upgrade_info": "tbd",
            "server": server,
            "times_checked": 3
        }

        return results

    def getQueueInstructionsSingleReward(self):
        server = self.db.getServerString()
        single_reward_data = self.db.data[server]["general"]
        reset_time = single_reward_data["reset_time"]
        save_time = single_reward_data["current_time"]
        needs_visit = self.hasEnoughTimePassed(reset_time, save_time)

        results = {"needs_visit": needs_visit, }
        return results

    def getQueueInstructionsServerSwap(self):
        server = self.db.getServerString()
        server_swap_data = self.db.data["general"]["server_swap_progress"]

        swap_time = server_swap_data["swap_options"]["short"]
        save_time = server_swap_data["last_swap_time"]
        needs_swap = self.hasEnoughTimePassed(swap_time, save_time)

        results = {"needs_swap": needs_swap, }
        print("Time since last swap: " + str(time.time() - save_time))
        return results

    def getQueueInstructionsMissionClaim(self):
        server = self.db.getServerString()
        mission_data = self.db.data[server]["map_progress"]
        items = mission_data["missions"]["in_progress"]
        save_time = mission_data["stats"]["save_time"]
        total_claims = 0
        unclaimed_missions = []
        index = 0

        for mission in items:
            print(mission)
            mission_time = mission["time"]
            needs_claim = self.hasEnoughTimePassed(mission_time, save_time)

            if needs_claim:
                total_claims += 1
            else:
                unclaimed_missions.append(mission)
                index += 1

        has_one_claim = total_claims >= 1
        results = {
            "needs_claim": has_one_claim,
            "mission_claim_count": total_claims,
            "mission_unclaimed_list": unclaimed_missions,
        }
        print("Showing instructions for mission claim")
        print(results)
        return results

    '''
    def adjustQueueInstructionsMissionStart(self, unclaimed_missions):
        server = self.db.getServerString()
        mission_data = self.db.data[server]["map_progress"]
        print("mission data")
        print(unclaimed_missions)
        slot = 1
        sorted_missions = []

        if len(unclaimed_missions) > 1:
            for mission in unclaimed_missions:
                sorted_missions.append(unclaimed_missions[mission])
            sorted_missions = sorted(
                sorted_missions, reverse=False, key=lambda item: item["time"])

        print(len(unclaimed_missions))

        sys.exit()
    '''

    def getQueueInstructionsMissionStart(self):
        server = self.db.getServerString()
        map_data = self.db.data[server]["map_progress"]

        max_squads = map_data["stats"]["squad_count"]
        used_squads = map_data["missions"]["total_squads"]
        open_missions = map_data["missions"]["available"]
        available_squads = max_squads - used_squads

        open_missions_count = len(open_missions)

        needs_mission_start = True if available_squads > 0 and open_missions_count > 0 else False
        has_open_missions = True if open_missions else False

        print(map_data)
        print(map_data["stats"])
        save_time = map_data["stats"]["save_time"]
        reset_time = map_data["stats"]["reset_time"]
        passed_time = time.time() - save_time
        missions_have_reset = passed_time >= reset_time

        results = {
            "needs_mission_start": needs_mission_start,
            "available_squads": available_squads,
            "has_open_missions": has_open_missions,
            "open_missions": open_missions,
            "missions_have_reset": missions_have_reset
        }
        '''
        print(results)
        print("show mission start instructions, then quit")
        sys.exit()
        '''
        return results

    def hasEnoughTimePassed(self, action_time, save_time):
        current_time = time.time()
        passed_time = current_time - save_time
        if (passed_time > action_time):
            return True
        else:
            return False

    def setData(self, data):
        self.data = data

    def setDatabase(self, db):
        self.db = db
