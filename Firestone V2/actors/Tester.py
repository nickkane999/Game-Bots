import pyautogui
import time
import re
import sys
import os

import easyocr
import pytesseract


class Tester:
    # Variables
    rotationsAfterBoss = 0
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Initializing Object
    def __init__(self):
        self.reader = easyocr.Reader(['en'])
        self.temp = "123"

    # Major object functions
    def testClick(self, points):
        cordX = points["x"]
        cordY = points["y"]

        pyautogui.moveTo(point["x"], point["y"])
        pyautogui.click(cordX, cordY)

    def performTestMap(self, actor):
        # actor.processMissionMap()
        # actor.mission_start.sortMissions()
        '''
        data = actor.game_bot.db.data
        print(data)
        options = data["server_1"]["map_progress"]["missions"]["items"]
        sorted_options = sorted(
            options.items(), key=lambda option: option[1]["slot"])
        print(sorted_options)
        '''
        # img = actor.mission_start.mission_images["mission_time_region"]
        # time = actor.game_bot.screenshot_helper.getScreenshotTime(img)
        # print(time)

        # actor.mission_claim.processMissionClaim()
        # actor.mission_start.processMissionMap()

    def performTestMultipleRewards(self, actor):
        print("Testing")
        actor.startMultipleRewardsDuties()

    def performTestFirestone(self, actor):
        pyautogui.click(400,400)
        time.sleep(0.4)
        actor.firestone2.runFirestoneCheck()
        '''
        print("Testing")
        actor.game_bot.db.refreshData()
        db = actor.game_bot.db
        instructions = actor.game_bot.queue_processor.verifyQueueLibrary(db)
        '''
        #actor.startLibraryDuties()

    def runIdleLoop(self, actors, base_path = None):
        self.base_path = base_path
        game_bot = actors["Guild"].game_bot
        while True:
            game_bot.click({"x":400, "y":400})
            print("Running Loop in 5 seconds ")
            time.sleep(5)

            self.runFirestoneLoop(actors["Library"])
            self.closeMenu(game_bot)
            print("firestone done")
            time.sleep(0.5)
            self.runExpeditionLoop(actors["Guild"])
            print("expedition done")
            self.runMapLoop(actors["Map"])
            print("missions done")
            self.runMagicQuarterLoop(actors["MagicQuarter"])
            print("magic quarter done")

            print("sleeping for 3 minutes")
            time.sleep(150)
            print("sleeping for 30 seconds")
            time.sleep(25)

    def closeMenu(self, bot):
        close_button_active = [(255, 77, 5), (255, 88, 16)]
        print("in close menu")
        time.sleep(1)
        print(bot.get_pixel_color(1840,80))
        while bot.get_pixel_color(1840,80) in close_button_active:
            print("I was closed")
            bot.click({"x": 1840, "y": 50})
            time.sleep(1)


    def runFirestoneLoop(self, actor):
        actor.game_bot.click({"x":400, "y":400})
        time.sleep(0.4)
        actor.firestone2.runFirestoneCheck()
        self.closeMenu(actor.game_bot)

    def runExpeditionLoop(self, actor):
        actor.game_bot.click({"x":400, "y":400})
        time.sleep(0.4)
        actor.guild2.runExpeditionCheck()
        self.closeMenu(actor.game_bot)
        """
        pyautogui.click(400,400)
        print("Running Loop in 5 seconds ")
        time.sleep(5)
        pyautogui.click(400,400)
        print("sleeping for 3 minutes")
        pyautogui.click(1840,50)
        time.sleep(175)
        """

    def runMapLoop(self, actor):
        actor.game_bot.click({"x":400, "y":400})
        time.sleep(0.4)
        actor.map2.runMapCheck(self.base_path)
        self.closeMenu(actor.game_bot)

    def runMagicQuarterLoop(self, actor):
        actor.game_bot.click({"x":400, "y":400})
        time.sleep(0.4)
        actor.magicquarter2.runMagicQuarterCheck()
        self.closeMenu(actor.game_bot)

    def performTestGuild(self, actor):
        actor.startDuties()

    def performTestCampaign(self, actor):
        actor.startDuties()

    def performTestMagicQuarter(self, actor):
        actor.startDuties()

    def performTestMultipleRewards(self, actor):
        actor.startDuties()

    def performTestSingleReward(self, actor):
        actor.startDuties()

    def performTestServerSwap(self, actor):
        actor.startDuties()

    def performActorTest(self, actor):
        actor.startDuties()

    def performTestExpeditions(self, actor):
        area = {'region': (1030, 140, 150, 40), 'image': 'C:\\Users\\nickk\\Dropbox\\Portfolio\\Game Bots\\Firestone\\data\\imgs\\guild\\expedition_renew.png',
                'type': 'guild-expedition-time', 'msg': 'Test data'}
        actor.game_bot.screenshot_helper.getScreenshotTimeNoScreenshot(area)

    def performTest2(self, temp):
        #string = pytesseract.image_to_string(temp)
        reader = easyocr.Reader(['en'], gpu=False)
        string = reader.readtext(temp)
        print(string[0][1])

    def performTest3(self, actor):
        #string = pytesseract.image_to_string(temp)
        actor.getMagicTrainTime()

    def replace_chars(self, text):
        """
        Replaces all characters instead of numbers from 'text'.

        :param text: Text string to be filtered
        :return: Resulting number
        """
        list_of_numbers = re.findall(r'\d+', text)
        result_number = ''.join(list_of_numbers)
        return result_number
