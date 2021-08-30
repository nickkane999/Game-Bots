import pyautogui
import time
import re
import sys
import os


from actors.Bot import Bot
from utilities.QueueProcessor import QueueProcessor
from utilities.testing.Tester import Tester


def runLoopTest():
    tester = Tester()
    tests = tester.tests
    selected_tests = [
        "GameLoopTest"
    ]

    for test_class in tests:
        if test_class in selected_tests:
            tests[test_class].runTest()


def runTests():
    tester = Tester()
    tests = tester.tests
    selected_tests = [
        "MenuTest"
    ]

    for test_class in tests:
        if test_class in selected_tests:
            tests[test_class].runTest()

    '''
    bot = Bot()
    print("My bot loaded")
    tower_selector = bot.tower_selector
    tower_selector.selectTower("dart monkey")
    sys.exit()
    '''


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
