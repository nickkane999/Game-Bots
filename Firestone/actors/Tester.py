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

    def performTest(self, actor):
        actor.processMissionMap()
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
