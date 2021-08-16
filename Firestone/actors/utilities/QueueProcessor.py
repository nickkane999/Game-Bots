import pyautogui
import time
import re
import sys
import os

from actors.utilities.QueueInstructions import QueueInstructions


class QueueProcessor:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self):
        self.zone = ""
        self.queue_instructions = QueueInstructions()

    def assignActorActions(self, actors):
        # Breaks Program, do not keep
        '''
        for k, v in actors.items():
            actors[k].game_bot = None
        '''

        self.actors = actors
        self.defineQueueActions()

    def defineQueueActions(self):
        actors = self.actors
        self.actions = {
            "guild": actors["guild"].startGuildDuties,
            "library": actors["library"].startLibraryDuties,
            "map": actors["map"].processMissionMap,
            "campaign": actors["campaign"].startCampaignDuties,
            "temple": actors["temple"].startTempleDuties,
            "battle": actors["battle"].startBattleDuties,
            "magic_quarter": actors["magic_quarter"].startMagicDuties,
            "single_reward": actors["single_reward"].getDailyRewardTimer,
            "multiple_rewards": actors["multiple_rewards"].startMultipleRewardsDuties,
            "server_swap": actors["server_swap"].startServerSwapDuties,
        }

    def verifyQueueLibrary(self, data):
        self.queue_instructions.setData(data)
        firestone = self.actors["library"].firestone
        # meteorite = self.actors["meteorite"]
        queue_instructions = self.queue_instructions
        results = {
            "meteorite": {},
            "firestone": {}
        }

        results["firestone"] = queue_instructions.getQueueInstructionsFirestone(
            firestone)
        results["meteorite"] = {
            "needs_upgrade": False,
            "upgrade_info": None
        }
        return results

    def verifyQueueMagicQuarter(self, data):
        self.queue_instructions.setData(data)
        magic_quarter = self.actors["magic_quarter"]
        queue_instructions = self.queue_instructions
        results = {
            "magic_quarter": {},
        }

        results["magic_quarter"] = queue_instructions.getQueueInstructionsMagicQuarter(
            magic_quarter)
        return results

    def verifyQueueGuild(self, db):
        self.queue_instructions.setDatabase(db)
        guild = self.actors["guild"]
        queue_instructions = self.queue_instructions
        results = {
            "expeditions": {},
        }

        results["expeditions"] = queue_instructions.getQueueInstructionsExpeditions(
            guild)
        return results

    def verifyQueueCampaign(self, data):
        self.queue_instructions.setData(data)
        campaign = self.actors["campaign"]
        queue_instructions = self.queue_instructions
        results = {
            "campaign": {},
        }

        results["campaign"] = queue_instructions.getQueueInstructionsCampaign(
            campaign)
        return results

    def verifyQueueMultipleRewards(self, db):
        self.queue_instructions.setDatabase(db)
        multiple_rewards = self.actors["multiple_rewards"]
        queue_instructions = self.queue_instructions
        results = {
            "multiple_rewards": {},
        }

        results["multiple_rewards"] = queue_instructions.getQueueInstructionsMultipleRewards(
            multiple_rewards)
        return results

    def verifyQueueSingleRewards(self, db):
        self.queue_instructions.setDatabase(db)
        queue_instructions = self.queue_instructions
        results = {
            "single_reward": {},
        }

        results["single_reward"] = queue_instructions.getQueueInstructionsSingleReward()
        return results

    def verifyQueueServerSwap(self, db):
        self.queue_instructions.setDatabase(db)
        queue_instructions = self.queue_instructions
        results = {
            "server_swap": {},
        }

        results["server_swap"] = queue_instructions.getQueueInstructionsServerSwap()
        return results

    def verifyQueueInstructionsMap(self, db):
        self.queue_instructions.setDatabase(db)
        queue_instructions = self.queue_instructions
        results = {
            "mission_claim": {},
            "mission_start": {},
        }

        results["mission_claim"] = queue_instructions.getQueueInstructionsMissionClaim()
        # unclaimed_missions = results["mission_claim"]["mission_unclaimed_list"]
        # queue_instructions.adjustQueueInstructionsMissionStart(unclaimed_missions)
        results["mission_start"] = queue_instructions.getQueueInstructionsMissionStart()
        sys.exit()
        return results

    def verifyQueueInstructionsMissionClaim(self, db):
        self.queue_instructions.setDatabase(db)
        results = self.queue_instructions.getQueueInstructionsMissionClaim()
        return results

    def verifyQueueInstructionsMissionStart(self, db):
        self.queue_instructions.setDatabase(db)
        results = self.queue_instructions.getQueueInstructionsMissionStart()
        return results
