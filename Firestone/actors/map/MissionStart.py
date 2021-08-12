import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np


class MissionStart:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.map_screen = bot.data["map"]

        self.squads = 1
        self.vertical_map_movement = 0
        self.mission_images = bot.screenshot_data.data["missions"]

    def resetMissionMap(self):
        pyautogui.click(50, 500)
        pyautogui.dragTo(1000, 970, 1, button='left')
        pyautogui.click(400, 200)
        pyautogui.dragTo(1000, 900, 1, button='left')
        pyautogui.click(400, 200)
        pyautogui.dragTo(1000, 900, 1, button='left')
        pyautogui.click(400, 200)
        pyautogui.dragTo(1000, 900, 1, button='left')
        time.sleep(2)

    def moveToMissionSlotOne(self):
        pyautogui.click(1860, 550)
        pyautogui.dragTo(1150, 550, 1, button='left')
        pyautogui.click(1150, 550)
        pyautogui.dragTo(1150, 80, 1, button='left')

    def moveToMissionSlotTwo(self):
        pyautogui.click(1000, 900)
        pyautogui.dragTo(1000, 390, 1, button='left')
        self.vertical_map_movement = 484

    def moveBackToMissionSlotOne(self):
        pyautogui.click(1000, 390)
        pyautogui.dragTo(1000, 900, 1, button='left')

    def assignData(self, instructions):
        self.instructions = instructions
        self.squads = instructions["available_squads"]

    def processMissionStart(self, instructions):
        self.assignData(instructions)
        needs_mission_start = instructions["needs_mission_start"]

        if needs_mission_start:
            self.resetMissionMap()
            select_points = self.getMapPoints()
            found_missions = self.selectMissions(select_points)
            print("found missions")
            print(found_missions)

            data = {
                "found_missions": found_missions
            }
            self.saveMissionsData(data)

    def getMapPoints(self):
        map_points = self.captureAllMapPoints()
        # print("Map points before filter")
        # print(map_points)
        map_points = self.condenseMapPoints(map_points)
        # print("Map points after filter")
        # print(map_points)
        return map_points

    def captureAllMapPoints(self):
        img_path_1 = self.mission_images["map_screenshots"]["screenshot_slot_1"]
        img_path_2 = self.mission_images["map_screenshots"]["screenshot_slot_2"]

        self.moveToMissionSlotOne()
        map_points_1 = self.getMapIconCoordinates(img_path_1)

        self.moveToMissionSlotTwo()
        map_points_2 = self.getMapIconCoordinates(img_path_2)

        map_points_all = {
            "map_1": map_points_1,
            "map_2": map_points_2,
        }
        self.moveBackToMissionSlotOne()
        return map_points_all

    def condenseMapPoints(self, map_points_all):
        self.condensed_point_data = self.assignCondensedPointsData(
            map_points_all)

        self.assignIconPointsToMissions()
        self.removeDuplicateMissionPoints()
        # self.appendBothMapsToCondensedPoints()

        condensed_points = self.condensed_point_data["condensed_points"]
        # print(condensed_points)
        # sys.exit()
        return condensed_points

    def selectMissions(self, point_data):
        screenshot_helper = self.game_bot.screenshot_helper
        img = self.mission_images["mission_time_region"]
        mission_costs = {
            "mission_1": 1,
            "mission_2": 1,
            "mission_3": 1,
            "mission_4": 2,
        }
        selected_missions = {}
        available_squads = self.squads
        ok_button = self.map_screen["icons"]["start_ok"]
        empty_space = self.map_screen["icons"]["empty_space"]

        for screen_area in point_data:
            if (screen_area == "map_screenshot_2"):
                self.moveToMissionSlotTwo()
            for mission in point_data[screen_area]:
                mission_times_count = 0
                for point in point_data[screen_area][mission]:
                    if (available_squads - mission_costs[mission]) >= 0:
                        if mission in selected_missions:
                            selected_missions[mission]["count"] += 1
                            mission_times_count += 1
                        else:
                            selected_missions[mission] = {"count": 1}
                            selected_missions[mission]["times"] = []

                        mission_coordinate = point_data[screen_area][mission][point]
                        self.game_bot.click(mission_coordinate)
                        mission_time = screenshot_helper.getScreenshotTime(img)
                        selected_missions[mission]["times"].append(
                            int(mission_time))

                        self.game_bot.click(ok_button)
                        self.game_bot.click(empty_space)
                        time.sleep(1)
                        #print("Found a mission to start: ")
                        # print(mission_coordinate)
                        available_squads -= mission_costs[mission]

        return selected_missions

    def saveMissionsData(self, point_data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveMissionsStarted(
            point_data, file)
        self.game_bot.db.saveDataFile()
        return True

    def assignIconPointsToMissions(self):
        available_missions = self.condensed_point_data["available_missions"]
        index = self.condensed_point_data["cp_index"]

        condensed_points = self.condensed_point_data["condensed_points"]
        remove_index_map_1 = self.condensed_point_data["remove_index_map_1"]
        remove_index_map_2 = self.condensed_point_data["remove_index_map_2"]
        map_1 = self.condensed_point_data["map_1"]
        map_2 = self.condensed_point_data["map_2"]

        #print("points before assignment:")
        # print(map_1)
        # print(map_2)

        for mission in available_missions:
            condensed_points["map_screenshot_1"][mission] = {}
            remove_index_map_1[mission] = []
            remove_index_map_2[mission] = []
            for point in map_1[mission]:
                index = 0
                evaluated_point = map_1[mission][point]
                # print(evaluated_point)
                # print(map_2[mission])
                found_point = self.matchesOtherMapPoint(
                    evaluated_point, map_2[mission])
                if found_point is not None or found_point == 0:
                    #print("found match")
                    remove_index_map_2[mission].append(found_point)
                    remove_index_map_1[mission].append(point)
                    condensed_points["map_screenshot_1"][mission][index] = map_1[mission][point]
                    index += 1

        self.condensed_point_data["condensed_points"] = condensed_points
        self.condensed_point_data["remove_index_map_1"] = remove_index_map_1
        self.condensed_point_data["remove_index_map_2"] = remove_index_map_2
        self.condensed_point_data["map_1"] = map_1
        self.condensed_point_data["map_2"] = map_2

        # print(remove_index_map_1)
        # print(remove_index_map_2)

    def removeDuplicateMissionPoints(self):
        available_missions = self.condensed_point_data["available_missions"]
        condensed_points = self.condensed_point_data["condensed_points"]

        remove_index_map_1 = self.condensed_point_data["remove_index_map_1"]
        remove_index_map_2 = self.condensed_point_data["remove_index_map_2"]
        map_1 = self.condensed_point_data["map_1"]
        map_2 = self.condensed_point_data["map_2"]

        #print("removing duplicate missions")
        # print(map_1)
        # print(map_2)

        for mission in remove_index_map_1:
            for index in remove_index_map_1[mission]:
                del map_1[mission][index]
        for mission in remove_index_map_2:
            # print(mission)
            for index in remove_index_map_2[mission]:
                del map_2[mission][index]

        #print("new maps")
        # print(map_1)
        # print(map_2)
        # print("condensed_points")
        # print(condensed_points)

        # Logic for # --- self.appendBothMapsToCondensedPoints ---
        new_points_to_add = {
            "map_screenshot_1": map_1,
            "map_screenshot_2": map_2
        }

        for area in new_points_to_add:
            for mission in available_missions:
                mission_size = len(condensed_points[area][mission])
                for new_point in new_points_to_add[area][mission]:
                    condensed_points[area][mission][mission_size] = new_points_to_add[area][mission][new_point]
                    mission_size += 1
        self.condensed_point_data["condensed_points"] = condensed_points

    def getMapIconCoordinates(self, path_map_screenshot):
        map_data = self.readMapIconImages(path_map_screenshot)

        coordinates = {}
        point_index = 0
        for mission in map_data["missions_found"]:
            coordinates[mission] = {}
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
                        coordinates[mission][point_index] = point
                        point_index += 1
                else:
                    coordinates[mission][point_index] = point
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
                "mission_1": cv2.imread(mission_images["type_1"]["map"]),
                "mission_2": cv2.imread(mission_images["type_2"]["map"]),
                "mission_3": cv2.imread(mission_images["type_3"]["map"]),
                "mission_4": cv2.imread(mission_images["type_4"]["map"]),
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

    def matchesOtherMapPoint(self, evaluated_point, map_2_points):
        veritcal_diff = self.vertical_map_movement

        evaluated_point
        if map_2_points:
            for point in map_2_points:
                current_x = map_2_points[point]["x"]
                current_y = map_2_points[point]["y"]

                # Can only use 5 px buffer, because icons can be as close as 10-15 px next to each other on the map
                # rasing this to 15 will cause crashes if the game has icons that are too close to eachother
                x_cord_match = abs(evaluated_point["x"] - current_x) <= 5
                y_cord_match = abs(
                    evaluated_point["y"] - current_y) - veritcal_diff <= 5
                points_are_identical = x_cord_match and y_cord_match

                if points_are_identical:
                    return point
        return None

    def assignCondensedPointsData(self, map_points_all):
        condensed_points_data = {
            "map_1": map_points_all["map_1"],
            "map_2": map_points_all["map_2"],
            "remove_index_map_1": {},
            "remove_index_map_2": {},
            "condensed_points": {
                "map_screenshot_1": {
                    "mission_1": {},
                    "mission_2": {},
                    "mission_3": {},
                    "mission_4": {},
                },
                "map_screenshot_2": {
                    "mission_1": {},
                    "mission_2": {},
                    "mission_3": {},
                    "mission_4": {},
                },
            },
            "cp_index": 0,
            "available_missions": {"mission_1", "mission_2", "mission_3", "mission_4"}
        }
        return condensed_points_data


'''
    def startMissionDuties(self):
        game_bot = self.game_bot
        guild_coordinates = self.guild_screen["icons"]

        self.enterGuildZone()
        self.performExpedition(guild_coordinates)
        self.returnToBattleScreen(guild_coordinates)

    def processedFinished(self):
        self.game_bot.db.refreshData()
        data = self.game_bot.db.data
        server = "server_" + data["general"]["current_server"]
        map_data = data[server]["map_progress"]
        missions = map_data["missions"]

        for index in list(missions):
            mission = missions[str(index)]
            mission_finish_time = int(
                mission["mission_time"]) + map_data["save_time"]
            current_time = time.time()
            print("Current time: " + str(current_time) +
                  ". Mission finish time: " + str(mission_finish_time))
            if (current_time >= mission_finish_time):
                print(self.game_bot.db.data[server]
                      ["map_progress"]["missions"])
                print("Processing new missions")
                self.claimMission(mission)
                self.game_bot.db.data[server]["map_progress"]["missions"].pop(
                    str(index), None)
                self.game_bot.db.data[server]["map_progress"]["missions"] = self.resortMissions(
                )
                print(self.game_bot.db.data[server]
                      ["map_progress"]["missions"])

        print(self.game_bot.db.data)
        self.game_bot.db.saveDataFile()

        # self.processMission(mission)

    def claimMission(self, mission):
        bot = self.game_bot
        coordinates = self.map_screen["icons"]
        slot = str(mission["map_slot"])

        bot.click(coordinates["claim_" + slot])
        bot.click(coordinates["claim_ok_side"])

    def resortMissions(self):
        data = self.game_bot.db.data
        server = "server_" + data["general"]["current_server"]

        for index in data[server]["map_progress"]["missions"]:
            self.game_bot.db.data[server]["map_progress"]["missions"][str(
                index)]["map_slot"] -= 1

    def enterMapZone(self):
        bot = self.game_bot

        bot.click(self.battle_screen["icons"]["town"])
        bot.click(self.town_screen["icons"]["map"])

    def performExpedition(self, coordinates):
        bot = self.game_bot

        print(coordinates)

        bot.click(coordinates["expeditions"])
        bot.click(coordinates["expedition_1"])
        bot.click(coordinates["expedition_ok"])
        bot.click(coordinates["expedition_1"])
        bot.click(coordinates["expedition_x_icon"])

    def returnToBattleScreen(self, coordinates):
        bot = self.game_bot

        bot.click(coordinates["x_icon"])
        bot.click(coordinates["x_icon"])

    def startMission(self):
        return True
'''
