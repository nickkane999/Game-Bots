import pyautogui
import time

import cv2
import numpy as np
import operator

from actors.Bot import Bot
from utilities.QueueProcessor import QueueProcessor
from utilities.testing.Tester import Tester
from utilities.functions.MainFunctions import *

pyautogui.PAUSE = 0.3


# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------


device = "desktop"
actors = ["MultipleRewards"]
runLoopTest()
# runTests()

# runUIDesktop(device)
# runUILaptop(device)
# runNormalDesktop(device)
# runNormalLaptop(device)

# runTestMap(device)
# runTestMultipleRewards(device)
# runTestFirestone(device)
# runTestGuild(device)
# runTestCampaign(device)
# runTestMagicQuarter(device)
# runTestSingleReward(device)
# runTestServerSwap(device)
# runActorTest(device, actors)
'''

'''


temp = 123


'''
# Set pause time between clicks/mouse movements
pyautogui.PAUSE = 0.05

# Allow time to enter "Idle Champions" interface
time.sleep(2.5)

# Set Parameters
sessionTime = time.time() + 300 # In seconds
bot = Bot(30)

# while time.time() < sessionTime:
    # bot.checkStatus()
# bot.upgradePeople()
    # bot.killEnemies()
'''


'''
time_settings = TimeSettings(actors)
time_settings_data = time_settings.data
timer = Timer(time_settings_data)
game_bot.setData(actors, timer)


# game_bot.start()
game_bot.startQueue()


tester = Tester()
tester.performTest(actors["map"])
'''

'''
db = DataHelper()
config = Config()
db.saveDataFileRaw(config.data)
'''

r'''
FOR MAP SELECTING IMAGES
IMPORTANT TO USE TO SAVE TIME

im1 = pyautogui.screenshot()
im1.save(r"C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\zTests\map_image.png")
taken_image = cv2.imread('zTests/map_image.png')

# load pass_image
pass_image = cv2.imread('zTests/map_small_mission.png')


# read height and width of pass_image image
matches = screenshot_helper.getImageMatches(taken_image, pass_image)

if matches:
    for point in matches:
        pyautogui.click(point[0], point[1])
        time.sleep(1)
        pyautogui.click(960, 960)
        time.sleep(1)
'''


'''
db = DataHelper()
sample_data = {
    "server_1": {
        "max_wave": 333
    },
    "server_5": {
        "max_wave": 268
    },
}

sample_data["server_1"]["max_wave"] = 340
sample_data["server_1"]["completed_green"] = True
db.saveDataFile(sample_data)
'''

# battle.assignParty()
# battle.startHeroFighter()

# guild = Guild(game_bot)
# guild.startGuildDuties()


# library = Library(game_bot)
# library.firestone.moveFirestoneMenuSlightLeft()
# library.startLibraryDuties()


'''
# Some tests
town_icon = game_coordinates["battle_screen"]["map"]
tester.testClick(town_icon)
tester = Tester()

'''
