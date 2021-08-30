import pyautogui
import time
import re
import sys
import os

import pytesseract
import cv2
import numpy as np
import easyocr
from PIL import Image

class ScreenHelper:

    # Package for converting text to string
    # EXE download path: https://github.com/UB-Mannheim/tesseract/wiki
    # Youtube video: https://www.youtube.com/watch?v=pZ7_qHAx1nE
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Initializing Object

    def __init__(self):
        self.zone = "123"
        self.reader = easyocr.Reader(['en'], gpu=False)
        self.action_map_text = {
            'victory': self.verifyMsg,
            'continue': self.verifyMsg,
        }

    def getScreenshotText(self, info):
        area = info["area"]
        img_path = info["img_path"]
        dps_type = info["type"]

        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(img_path)
        img_text = self.convertImageToText(img_path, dps_type)
        print(img_text)
        return img_text

    def verifyMsg(self, info, verified_word):
        area = info["area"]
        img_path = info["img_path"]
        dps_type = info["type"]
        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(img_path)

        string = pytesseract.image_to_string(img_path)
        string = string.replace(",", ".").lower()
        # print(string)
        if verified_word in string:
            return True
        else:
            return False

    def checkIfImageBlack(self, info):
        area = info["area"]
        img_path = info["img_path"]
        dps_type = info["type"]
        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(img_path)

        img = Image.open(img_path)
        if not img.getbbox():
            return True
        else:
            return False

    def convertImageToText2(self, path, type):
        string = self.reader.readtext(path)
        if not string:
            return "0"
        string = string[0][1]
        action_map = self.action_map_text2
        return action_map[type](string)

    def convertEnemyString(self, string):
        string = string[0:-2]
        if (len(string) <= 4):
            return "bad string" if "e" not in string else "starting"
        else:
            return string[0:-3]

    def covnertFirestoneString(self, string):
        string = string[1:-3]
        string = self.removeLetters(string)
        return string

    def convertBattleDps(self, string):
        return string[5:-2]

    def convertTime(self, string):
        # print("Firestone time: " + string)
        string = string[0:-2].split(":")
        sections = {
            0: 1,  # second
            1: 60,  # seconds
            2: 3600,  # seconds in hour
            3: 86400  # seconds in day
        }
        section = 0
        upgrade_time = 0
        for timed_section in reversed(string):
            print(string)
            print(timed_section)
            upgrade_time = upgrade_time + \
                (sections[section] * int(timed_section))
            section = section + 1
            # print(upgrade_time)
        #print(str(upgrade_time) + "---------")
        # print(time.time())
        return str(upgrade_time)

    def convertTime2(self, string):
        string = string.replace("I", "1").replace(
            "o", "0").replace("O", "0").replace("+", ":").replace(';', ':').replace('s', '5').replace('S', '5')
        string = string.replace(".", ":").split(":")
        sections = {
            0: 1,  # second
            1: 60,  # seconds
            2: 3600,  # seconds in hour
            3: 86400  # seconds in day
        }
        section = 0
        upgrade_time = 0
        for timed_section in reversed(string):
            upgrade_time = upgrade_time + \
                (sections[section] * int(timed_section))
            section = section + 1
            # print(upgrade_time)
        #print(str(upgrade_time) + "---------")
        # print(time.time())
        return str(upgrade_time)

    def convertTimeMapReset(self, string):
        if "New missions in: " in string:
            string = string[17:]
        else:
            string = "5:59:59"

        string = self.convertTime2(string)
        return string

    def convertTimeGuildExpeditions(self, string):
        print("Guild tester time: " + string)
        if ":" not in string and "." not in string:
            return "0"
        else:
            return self.convertTime2(string)

    def removeLetters(self, string):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for ch in letters:
            if ch in string:
                string = string.replace(ch, "")
        return string

    def getImageMatches(self, taken_image, pass_image):
        w, h = pass_image.shape[0], pass_image.shape[1]

        res = cv2.matchTemplate(taken_image, pass_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        match_index = 0
        matches = []
        for pt in zip(*loc[::-1]):
            if not matches or (self.isNewPoint(pt, matches)):
                print(pt)
                matches.append([pt[0], pt[1]])
                cv2.rectangle(taken_image, pt,
                              (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

        # self.showAsImage(taken_image)
        return matches

    def confirmImageMatch(self, info):
        screenshot = pyautogui.screenshot(region=info["area"])
        screenshot.save(info["taken_img"])
        taken_image = cv2.imread(info["taken_img"])
        pass_image = cv2.imread(info["template_img"])

        w, h = pass_image.shape[0], pass_image.shape[1]

        res = cv2.matchTemplate(taken_image, pass_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)

        match_index = 0
        matches = []
        for pt in zip(*loc[::-1]):
            if not matches or (self.isNewPoint(pt, matches)):
                matches.append([pt[0], pt[1]])
                cv2.rectangle(taken_image, pt,
                              (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

        # self.showAsImage(taken_image)
        if matches:
            return True
        else:
            return False

    def isNewPoint(self, point, matches):
        return abs(matches[-1][0] - point[0]) >= 10 or abs(matches[-1][1] - point[1]) >= 10

    def showAsImage(self, taken_image):
        taken_image = cv2.resize(taken_image, (800, 600))
        cv2.imshow("result", taken_image)
        cv2.waitKey(10000)

    def getScreenshotText2(self, info):
        area = info["area"]
        img_path = info["img_path"]
        dps_type = info["type"]

        screenshot = pyautogui.screenshot(region=area)
        screenshot.save(img_path)
        img_text = self.convertImageToText2(img_path, dps_type)
        # print(img_text)
        return img_text

    def getScreenshotText3(self, info):
        img_path = info["img_path"]
        dps_type = info["type"]
        img_text = self.convertImageToText2(img_path, dps_type)
        print(img_text)
        return img_text

    def convertText(self, string):
        return string

    def convertTextMerchantTitle(self, string):
        string = string.replace("0", "o")
        return string

    def convertTextMerchantQuantity(self, string):
        string = string.replace("o", "0")
        string = string.replace("[", "")
        string = string.replace("]", "")
        string = string.replace("(", "")
        string = string.replace(")", "")
        return string

    def getScreenshotTime(self, data):
        upgrade_info = {
            "area": data["region"],
            "img_path": data["image"],
            "type": data["type"]
        }
        # print(upgrade_info)
        text = self.getScreenshotText2(upgrade_info)
        print(data["msg"] + text)
        return text

    def getScreenshotTimeNoScreenshot(self, data):
        upgrade_info = {
            "area": data["region"],
            "img_path": data["image"],
            "type": data["type"]
        }
        print(upgrade_info)
        text = self.getScreenshotText3(upgrade_info)
        print(data["msg"] + text)
        return text
