import pyautogui
import time
import re
import sys
import os


class MultipleRewards:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.conditions = bot.conditions
        self.quest_regions = bot.screenshot_data.data["quests"]

        self.battle_screen = bot.data["battle"]
        self.profile_screen = bot.data["profile"]
        self.quests_screen = bot.data["quests"]
        self.mission_status = True

    def moveMenuUp(self):
        pyautogui.click(1610, 300)
        pyautogui.dragTo(1610, 900, 1, button='left')
        pyautogui.click(1610, 300)
        pyautogui.dragTo(1610, 900, 1, button='left')
        time.sleep(2)

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def startMultipleRewardsDuties(self):
        self.game_bot.db.refreshData()
        print("Short sleep before starting multiple rewards")
        time.sleep(3)
        game_bot = self.game_bot
        queue_processor = game_bot.queue_processor

        quest_coordinates = self.quests_screen["icons"]
        db = game_bot.db
        instructions = queue_processor.verifyQueueMultipleRewards(db)

        needs_visit = instructions["multiple_rewards"]["needs_visit"]
        performed_dailies = instructions["multiple_rewards"]["performed_dailies"]
        times_checked = instructions["multiple_rewards"]["times_checked"]

        print(instructions)
        '''
        print("Needs Visit:")
        print(needs_visit)
        '''
        if (not performed_dailies and needs_visit):
            self.assignQueueData(quest_coordinates, instructions)

            print("Quest Dailies Instructions: ")
            print(instructions)

            if needs_visit:
                for x in range(times_checked):
                    self.enterQuestZone()
                    if x == 0:
                        self.moveMenuUp()

                    quest_queue = self.buildQuestQueue()
                    if quest_queue:
                        self.processQuestQueue(quest_queue)
                self.game_bot.click(self.coordinates["x_icon"])

        if not self.mission_status:
            self.game_bot.click(self.coordinates["x_icon"])

    def enterQuestZone(self):
        self.game_bot.click(self.battle_screen["icons"]["profile"])
        self.game_bot.click(self.profile_screen["icons"]["quests"])
        time.sleep(2)

    def processQuestQueue(self, quest_queue):
        instructions = self.instructions["multiple_rewards"]
        server = instructions["server"]
        quest_images = self.quest_regions
        screenshot_helper = self.game_bot.screenshot_helper

        quest_1_claim_text = screenshot_helper.getScreenshotTime(
            quest_images["quest_1_claim_data"])
        run_needed = quest_1_claim_text != "claim"

        if (run_needed):
            self.assignMissions()
            for quest in quest_queue:
                data = self.processQuestRequest(quest_queue[quest])
                print("Finished Quest: " + quest_queue[quest]["title"])
                quest_queue[quest]["data"] = data

            quest_queue["server"] = server
            self.saveCurrentProgress(quest_queue)

    def assignMissions(self):
        actors = self.game_bot.queue_processor.actors
        self.mission_actions = {
            "Conqueror": None,
            "Trainer": None,
            "Expeditioner": None,
            "Gamer": actors["tavern"].completeQuest,
            "Collector": actors["inventory"].completeQuest,
            "Merchant": actors["merchant"].completeQuest,
            "Liberator": actors["campaign"].completeQuest,
            "Miner": actors["guild"].completeMinerQuest,
        }

    def processQuestRequest(self, quest):
        bot = self.game_bot
        mission_actions = self.mission_actions
        title = quest["title"]
        result_text = quest["claim"]
        icon = "quest_" + str(quest["icon"])
        icon = "quest_1"
        coordinates = self.coordinates

        quest_results = {
            "completed": False,
            "claimed": False,
            "add_completion": False
        }

        if(result_text == "Claim"):
            bot.click(coordinates[icon])
            bot.click(coordinates["x_icon"])
            quest_results["completed"] = True
            quest_results["claimed"] = True
            quest_results["add_completion"] = True
        elif (result_text == "Claimed"):
            print("I was claimed")
            quest_results["completed"] = True
            quest_results["claimed"] = True
            self.restartMenu()
        elif (result_text != "Claimed" and mission_actions[title] is not None):
            print("I was not claimed and not a mission action")
            times_completed = self.getCompletedTimes(result_text)

            if (title in ["Miner", "Collector"]):
                self.restartMenu()
            else:
                self.game_bot.click(self.coordinates["x_icon"])

            time.sleep(1)
            mission_actions[title](times_completed)
            quest_results["completed"] = True
        else:
            print(
                "Mission wasn't found in 1st 6 options, or not created yet for the name: " + quest["title"])
            self.mission_status = False

        print("Mission Results:")
        print(quest_results)
        return quest_results

    def getCompletedTimes(self, string):
        index = string.find('1')
        if index == 1:
            print(string)
            string = string[:index] + "/" + string[index + 1:]
            print(string)
        string = string.split("/")
        print(string)
        return int(string[0])

    def restartMenu(self):
        self.game_bot.click(self.coordinates["x_icon"])
        self.enterQuestZone()

    def returnToBattleScreen(self):
        bot = self.game_bot
        profile_coordinates = self.profile_screen["icons"]
        bot.click(profile_coordinates["x_icon"])

    def saveCurrentProgress(self, data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveMultipleDuties(data, file)
        self.game_bot.db.saveDataFile()

    def buildQuestQueue(self):
        time.sleep(1)
        screenshot_helper = self.game_bot.screenshot_helper
        server = self.game_bot.db.getServerString()
        quest_images = self.quest_regions
        time.sleep(1)

        quest_1_claim_text = screenshot_helper.getScreenshotTime(
            quest_images["quest_1_claim_data"])
        run_needed = quest_1_claim_text != "claim"

        if (run_needed):
            quest_queue = {
                "quest_6": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_6_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_6_claim_data"]),
                    "icon": 6
                },
                "quest_5": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_5_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_5_claim_data"]),
                    "icon": 5
                },
                "quest_4": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_4_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_4_claim_data"]),
                    "icon": 4
                },
                "quest_3": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_3_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_3_claim_data"]),
                    "icon": 3
                },
                "quest_2": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_2_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_2_claim_data"]),
                    "icon": 2
                },
                "quest_1": {
                    "title": screenshot_helper.getScreenshotTime(quest_images["quest_1_title_data"]),
                    "claim": screenshot_helper.getScreenshotTime(quest_images["quest_1_claim_data"]),
                    "icon": 1
                },
            }
            return quest_queue
        else:
            return False
