import time

from abc import ABC, abstractmethod


class SaveHelperTemplate(ABC):
    # Initializing Object
    def __init__(self, bot):
        self.game_bot = bot

    def saveProgress(self):
        file = self.getRefreshedData()
        actions = self.saveActions

        for action in actions:
            self.performSaveAction(action)

    def performSaveAction(self, saveAction):
        file = self.game_bot.db.data
        self.game_bot.db.data = saveAction(file)
        self.game_bot.db.saveDataFile()

    def getRefreshedData(self):
        self.game_bot.db.refreshData()
        file = self.game_bot.db.data

    def getServerString(self):
        return "server_" + self.game_bot.db.data["general"]["current_server"]
