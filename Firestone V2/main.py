import pyautogui
import time

import cv2
import numpy as np
import operator
import win32gui

from actors.Bot import Bot
from actors.Tester import Tester

from actors.battle.Battle import Battle
from actors.campaign.Campaign import Campaign
from actors.engineer.Engineer import Engineer
from actors.guild.Guild import Guild
from actors.library.Library import Library
from actors.map.Map import Map
from actors.single_reward.SingleReward import SingleReward
from actors.multiple_rewards.MultipleRewards import MultipleRewards
from actors.tavern.Tavern import Tavern
from actors.temple.Temple import Temple
from actors.merchant.Merchant import Merchant
from actors.magic_quarter.MagicQuarter import MagicQuarter
from actors.inventory.Inventory import Inventory
from actors.sleeper.Sleeper import Sleeper
from actors.utilities.GameStartup import GameStartup
from actors.utilities.ServerSwap import ServerSwap
from actors.utilities.ConditionManager import ConditionManager
from actors.utilities.QueueProcessor import QueueProcessor
from actors.utilities.GameUI import GameUI

from components.Timer import Timer
from components.ScreenHelper import ScreenHelper

from data.Zones import Zones
from data.TimeSettings import TimeSettings
from data.DataHelper import DataHelper
from data.Config import Config
from data.ScreenshotData import ScreenshotData


from actors.utilities.queue_instructions.GuildQueueHelper import GuildQueueHelper

pyautogui.PAUSE = 0.3


# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------

def createGameBot(device):
    zones = Zones()
    zones_data = zones.data
    conditions = ConditionManager()
    screenshot_helper = ScreenHelper()
    screenshot_data = ScreenshotData()
    db = DataHelper()
    queue_processor = QueueProcessor()

    info = {
        "zones_data": zones_data,
        "conditions": conditions,
        "db": db,
        "screenshot_helper": screenshot_helper,
        "screenshot_data": screenshot_data,
        "queue_processor": queue_processor,
    }

    bot = Bot(info)
    server_swap = ServerSwap(bot, device)
    bot.assignSeverSwap(server_swap)
    return bot


def createActors(bot, device):
    actors = {
        "Battle": Battle(bot),
        "Guild": Guild(bot),
        "Library": Library(bot),
        "Temple": Temple(bot),
        "Campaign": Campaign(bot),
        "Map": Map(bot),
        "MagicQuarter": MagicQuarter(bot),
        "MultipleRewards": MultipleRewards(bot),
        "SingleReward": SingleReward(bot),
        "Tavern": Tavern(bot),
        "Merchant": Merchant(bot),
        "inventory": Inventory(bot),
        "ServerSwap": ServerSwap(bot, device),
        "Sleeper": Sleeper(bot, device)
    }

    return actors


def assignActors(game_bot, actors):
    game_bot.queue_processor.assignActorActions(actors)
    return game_bot

# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------
# --------------------------------------------


def runFirestoneLoop(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestFirestone(actors["Library"])

def runUIDesktop(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    ui = GameUI(game_bot)
    ui.startMenu()


def runUILaptop(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    ui = GameUI(game_bot)
    ui.startMenu()


def runNormalDesktop(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    game_bot.startQueue()


def runNormalLaptop(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    game_bot.startQueue()


def runTestMap(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestMap(actors["Map"])


def runTestMultipleRewards(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestMultipleRewards(actors["MultipleRewards"])


def runTestFirestone(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestFirestone(actors["Library"])


def runTestGuild(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestGuild(actors["Guild"])


def runTestCampaign(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestCampaign(actors["Campaign"])


def runTestMagicQuarter(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestMagicQuarter(actors["MagicQuarter"])


def runTestSingleReward(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestSingleReward(actors["SingleReward"])


def runTestServerSwap(device):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    tester.performTestServerSwap(actors["ServerSwap"])


def runActorTest(device, input_actors):
    game_bot = createGameBot(device)
    actors = createActors(game_bot, device)
    tester = Tester()
    game_bot = assignActors(game_bot, actors)
    for actor in input_actors:
        tester.performActorTest(actors[actor])


device = "desktop"
actors = ["MultipleRewards"]
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