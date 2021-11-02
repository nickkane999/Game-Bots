import time

# from utilities.application.Instructions import Instructions
# from utilities.application.RecordLogger import RecordLogger
from utilities.application.Browser import Browser
from utilities.application.SaveData import SaveData
from actors.Bot import Bot

class Application:

    # Initializing Object
    # 2 --> 16
    def __init__(self, instructions):
        browser = Browser(instructions)
        self.browser = browser
        self.save_data = SaveData(instructions)

        bot_data = {
            'instructions': instructions,
            'browser': browser,
            'save_data': self.save_data
        }
        self.bot = Bot(bot_data)
