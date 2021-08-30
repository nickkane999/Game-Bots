import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np
from abc import ABC, abstractmethod

from actors.Bot import Bot
from data.Zones import Zones


class MapTemplate(ABC):
    # Initializing Object
    def __init__(self):
        self.class_name = self.getClass()
        self.game_bot = bot
        self.conditions = bot.conditions

        zones_data = Zones().data
        self.coordinates = {
            "Guild": zones_data["guild"]["icons"],
            "Campaign": zones_data["campaign"]["icons"],
            "MagicQuarter": zones_data["magic_quarter"]["icons"],
            "MultipleRewards": zones_data["quests"]["icons"],
            "SingleReward": zones_data["shop"]["icons"],
            "ServerSwap": zones_data["shop"]["icons"],
        }

    def loadMapPoints(self):
        self.loadTowerPlacements()

    @abstractmethod
    def loadTowerPlacements(self):
        pass

    def saveProgress(self, data):
        self.save_helper.data = data
        self.save_helper.saveProgress()
        print("Finished saving progress " + self.class_name)

    def assignQueueData(self, coordinates, instructions):
        self.coordinates = coordinates
        self.instructions = instructions

    def loadData(self):
        instructions = self.loadInstructions()
        coordinates = self.getCoordinates()
        self.assignQueueData(coordinates, instructions)

    def loadInstructions(self):
        self.game_bot.db.refreshData()
        game_bot = self.game_bot
        queue_instructions = game_bot.queue_processor.queue_instructions

        db = game_bot.db
        class_name = self.class_name
        instructions = queue_instructions.getQueueInstructions(db, class_name)
        print("Done")
        return instructions

    def getClass(self):
        # print(type(self).__name__)
        return type(self).__name__

    def getCoordinates(self):
        class_name = self.class_name
        return self.coordinates[class_name]
