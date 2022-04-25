import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np
import copy

from actors.map.MissionStart import MissionStart
from actors.map.MissionClaim import MissionClaim


class Map2:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.battle_screen = bot.data["battle"]
        self.town_screen = bot.data["town"]
        self.map_screen = bot.data["map"]
        # self.map_regions = bot.screenshot_data.data["map"]
        self.screen_width = 1800

        self.status = {
            "map_active": (255, 255, 255),
            "battles_active": [(255, 255, 255), (247, 4, 0)],
            "campaign_active": [(255, 255, 255), (247, 4, 0)],
            "campaign_daily_active": [(255, 255, 255), (247, 4, 0)],
            "mission_cancel": (231, 88, 79),
            "mission_claim": (239, 218, 189),
            "mission_claim_confirm": (12, 158, 8),
            "mission_start": (13, 161, 5),
            "no_missions_available": (239, 218, 189),
            "mission_claim_2": [(253, 177, 71), (252, 177, 71)],
            "campaign_daily_mission_unavailable": [(192, 145, 101), (173, 130, 90), (237, 217, 188)],
            "campaign_mission_completed": [(11, 160, 8), (11, 159, 8), (22, 188, 22), (22, 188, 21)]
        }

        self.locations = {
            "mission_cancel": [730, 905],
            "mission_claim": [960, 875],
            "mission_claim_confirm": [950, 450],
            "mission_start": [1000, 925],
            "mission_exit": [50, 950],
            "mission_claim_2": [960, 895],
            "map_active": [1900, 290],
            "battles_active": [435, 270],
            "battles_select": [310, 200],
            "campaign_active": [920, 335],
            "campaign_select": [700, 420],
            "campaign_claim": [60, 990],
            "campaign_daily_active": [1880, 980],
            "campaign_daily_select": [1780, 1020],
            "campaign_liberation": [600, 800],
            "campaign_mission_completed": [880, 770],
        }

        self.claim_points = [
            {"x": 200, "y": 225},
        ]

        self.vertical_map_movement = 0
        base_path = r"C:\Users\nickk\Music\Portfolio\Game-Bots\Firestone V2"
        self.mission_images = self.buildMissions(base_path)

        self.mission_claim = MissionClaim(bot)
        self.mission_start = MissionStart(bot)


    def runMapCheck(self, base_path = None):
        print("I'm in the map check")
        if self.checkMapChange():
            in_menu = self.menuCheck("Map", self.game_bot)
            if in_menu:
                if base_path:
                    self.mission_images = self.buildMissions(base_path)

                # Claim missions
                # self.claimMissions()

                # Start missions
                self.startMissions()
            else:
                print("Did not find map menu")


    def runCampaignCheck(self):
        bot = self.game_bot
        print("I'm in the campaign check")
        if self.checkCampaignChange():
            in_menu = self.menuCheck("Campaign", self.game_bot)
            if in_menu:
                print("Found campaign menu")
                bot.click({"x": self.locations["campaign_claim"][0], "y": self.locations["campaign_claim"][1]})
                time.sleep(0.5)
                bot.click({"x": self.locations["campaign_claim"][0], "y": self.locations["campaign_claim"][1]})
                time.sleep(0.5)
                if self.checkCampaignDailyChange():
                    print("Found campaign daily")
                    bot.click({"x": self.locations["campaign_daily_select"][0], "y": self.locations["campaign_daily_select"][1]})
                    time.sleep(0.5)
                    bot.click({"x": self.locations["campaign_liberation"][0], "y": self.locations["campaign_liberation"][1]})
                    time.sleep(0.5)
                    self.selectDailyMissions()
                    bot.click({"x": 30, "y": 30})
                    time.sleep(0.5)
                    return True
            else:
                print("Did not find campaign menu")

    def selectDailyMissions(self):
        bot = self.game_bot
        height = 775
        for x in range(200, self.screen_width + 200, 200):
            if bot.get_pixel_color(x, height) not in self.status["campaign_daily_mission_unavailable"]:
                bot.click({"x": x, "y": height})
                time.sleep(0.5)
                bot.click({"x": 30, "y": 30})
                time.sleep(0.5)
                print("Waiting for battle to end")
                while bot.get_pixel_color(self.locations["campaign_mission_completed"][0], self.locations["campaign_mission_completed"][1]) not in self.status["campaign_mission_completed"]:
                    time.sleep(3)
                bot.click({"x": self.locations["campaign_mission_completed"][0], "y": self.locations["campaign_mission_completed"][1]})
                time.sleep(0.5)
        bot.click({"x": 30, "y": 30})
        time.sleep(0.5)

    def checkMapChange(self):
        if self.game_bot.get_pixel_color(self.locations["map_active"][0], self.locations["map_active"][1]) == self.status["map_active"]:
            print("Map is active")
            pyautogui.press("m")
            time.sleep(0.5)
            return True
        else:
            return False

    def checkCampaignChange(self):
        bot = self.game_bot
        pyautogui.press("t")
        time.sleep(0.5)
        if self.game_bot.get_pixel_color(self.locations["battles_active"][0], self.locations["battles_active"][1]) in self.status["battles_active"]:
            bot.click({"x": self.locations["battles_select"][0], "y": self.locations["battles_select"][1]})
            time.sleep(0.5)
            if self.game_bot.get_pixel_color(self.locations["campaign_active"][0], self.locations["campaign_active"][1]) in self.status["campaign_active"]:
                bot.click({"x": self.locations["campaign_select"][0], "y": self.locations["campaign_select"][1]})
                time.sleep(0.5)
                return True
            else:
                bot.click({"x": 30, "y": 30})
                print("Battles does not show campaign as active")
        
        return False

    def checkCampaignDailyChange(self):
        if self.game_bot.get_pixel_color(self.locations["campaign_daily_active"][0], self.locations["campaign_daily_active"][1]) in self.status["campaign_daily_active"]:
            return True
        else:
            return False

    def startMissions(self):
        print("Finding missions")
        img_path_1 = self.mission_images["map_screenshot"]
        map_points = self.getMapIconCoordinates(img_path_1)
        print(map_points)

        for mission_type in map_points:
            for point in map_points[mission_type]:
                self.processPoint(point)

        print("Finished viewing missions")

    def getMapIconCoordinates(self, path_map_screenshot):
        map_data = self.readMapIconImages(path_map_screenshot)

        coordinates = {}
        point_index = 0
        for mission in map_data["missions_found"]:
            coordinates[mission] = []
            image_processing_data = {
                "map_data": map_data,
                "mission": mission
            }

            loc = self.getFoundMissionPointLocations(image_processing_data)
            for pt in zip(*loc[::-1]):
                point = {"x": pt[0], "y": pt[1]}
                if coordinates[mission]:
                    prev_pt = coordinates[mission][point_index - 1]
                    if abs(prev_pt["x"] - point["x"]) >= 20 or abs(prev_pt["y"] - point["y"]) >= 20:
                        coordinates[mission].append(point)
                        point_index += 1
                else:
                    coordinates[mission].append(point)
                    point_index += 1
            point_index = 0

        return coordinates

    def readMapIconImages(self, img_path):
        mission_images = self.mission_images
        im1 = pyautogui.screenshot()
        im1.save(img_path)

        map_data = {
            "map_path": img_path,
            "missions_found": {
                "type_1": cv2.imread(mission_images["type_1"]["map"]),
                "type_2": cv2.imread(mission_images["type_2"]["map"]),
                "type_3": cv2.imread(mission_images["type_3"]["map"]),
                "type_4": cv2.imread(mission_images["type_4"]["map"]),
            },
        }
        return map_data

    def getFoundMissionPointLocations(self, img_data):
        mission = img_data["mission"]
        map_data = img_data["map_data"]

        img_path = map_data["map_path"]
        pass_image = cv2.imread(img_path)
        taken_image = map_data["missions_found"][mission]
        res = cv2.matchTemplate(
            taken_image, pass_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        return loc


    def claimMissions(self):
        for point in self.claim_points:
            self.processPoint(point)

    def processPoint(self, point):
        bot = self.game_bot
        bot.click(point)
        time.sleep(1)
        if bot.get_pixel_color(self.locations["mission_cancel"][0], self.locations["mission_cancel"][1]) == self.status["mission_cancel"]:
            print("Mission in progress")
            bot.click({"x": self.locations["mission_exit"][0], "y": self.locations["mission_exit"][1]})
            time.sleep(0.5)
        elif bot.get_pixel_color(self.locations["mission_start"][0], self.locations["mission_start"][1]) == self.status["mission_start"]:
            print("Mission start")
            bot.click({"x": self.locations["mission_start"][0], "y": self.locations["mission_start"][1]})
            time.sleep(0.5)
            bot.click({"x": 50, "y": 950})
            time.sleep(0.5)
        elif bot.get_pixel_color(self.locations["mission_claim_2"][0], self.locations["mission_claim_2"][1]) in self.status["mission_claim_2"] or \
        bot.get_pixel_color(self.locations["mission_claim_confirm"][0], self.locations["mission_claim_confirm"][1]) == self.status["mission_claim_confirm"]:
            print("Mission complete")
            bot.click({"x": self.locations["mission_claim_2"][0], "y": self.locations["mission_claim_2"][1]})
            time.sleep(0.5)
            bot.click({"x": self.locations["mission_claim_confirm"][0], "y": self.locations["mission_claim_confirm"][1]})
            time.sleep(0.5)
        elif bot.get_pixel_color(self.locations["mission_claim"][0], self.locations["mission_claim"][1]) == self.status["mission_claim"] and \
        bot.get_pixel_color(self.locations["mission_cancel"][0], self.locations["mission_cancel"][1]) != self.status["mission_cancel"]:
            print("Not enough squads")
            bot.click({"x": self.locations["mission_claim"][0], "y": self.locations["mission_claim"][1]})
            time.sleep(0.5)
            bot.click({"x": 50, "y": 950})
            time.sleep(0.5)


    def buildMissions(self, base_path):
        missions = {
            "type_1": {
                "map": base_path + r'\data\imgs\map\map_type_1.png',
                "side_menu": base_path + r'\data\imgs\maps\side_menu_1.png',
            },
            "type_2": {
                "map": base_path + r'\data\imgs\map\map_type_2.png',
                "side_menu": base_path + r'\data\imgs\map\side_menu_2.png',
            },
            "type_3": {
                "map": base_path + r'\data\imgs\map\map_type_3.png',
                "side_menu": base_path + r'\data\imgs\map\side_menu_3.png',
            },
            "type_4": {
                "map": base_path + r'\data\imgs\map\map_type_4.png',
                "side_menu": base_path + r'\data\imgs\maps\side_menu_4.png',
            },
            "map_screenshot": base_path + r'\data\imgs\map\map_save_mission_1.png',
            "mission_time_region": {
                "region": (1030, 860, 150, 50),
                "image": base_path + r'\data\imgs\map\mission_timer.png',
                "type": "map-mission-timer",
                "msg": "mission timer text: ",
            }
        }

        return missions


############################################################ Old Code

    def resetMissionMap(self):
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        pyautogui.click(300, 270)
        pyautogui.dragTo(1630, 970, 1, button='left')
        time.sleep(2)

    def getClaimInstructions(self):
        self.game_bot.db.refreshData()
        db = self.game_bot.db
        queue_processor = self.game_bot.queue_processor

        instructions = queue_processor.verifyQueueInstructionsMissionClaim(db)
        print("Claim instructions")
        print(instructions)
        return instructions

    def getMissionStartInstructions(self):
        self.game_bot.db.refreshData()
        db = self.game_bot.db
        queue_processor = self.game_bot.queue_processor

        instructions = queue_processor.verifyQueueInstructionsMissionStart(db)
        print("Mission start instructions")
        print(instructions)
        return instructions

    def processMissionMap(self):
        game_bot = self.game_bot
        map_coordinates = self.map_screen["icons"]

        claim_instructions = self.getClaimInstructions()
        needs_claim = claim_instructions["needs_claim"]

        if needs_claim:
            self.enterMapZone()
            print("Entered map")

            self.mission_claim.processMissionClaim(claim_instructions)

        start_instructions = self.getMissionStartInstructions()
        needs_mission_start = start_instructions["needs_mission_start"]
        missions_have_reset = start_instructions["missions_have_reset"]

        if needs_mission_start or missions_have_reset:
            if not needs_claim:
                self.enterMapZone()

            print("Entered map. Starting mission select / refresh")
            self.game_bot.db.refreshData()
            self.mission_start.processMissionStart(start_instructions)

    def enterMapZone(self):
        self.game_bot.click(self.battle_screen["icons"]["map"])
        time.sleep(1)

    def returnToBattleScreen(self):
        self.game_bot.click(self.town_screen["icons"]["x_icon"])
