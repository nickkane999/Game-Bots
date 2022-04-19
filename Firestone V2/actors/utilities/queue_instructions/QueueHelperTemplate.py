import time

from abc import ABC, abstractmethod


class QueueHelperTemplate(ABC):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    @abstractmethod
    def getInstructions(self):
        pass

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
