import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np
import copy


class MissionStart:
    # Variables
    rotationsAfterBoss = 0

    # Initializing Object
    def __init__(self, bot):
        self.zone = "123"
        self.game_bot = bot
        self.map_screen = bot.data["map"]
        self.claim_regions = bot.screenshot_data.data["mission-claim"]

        self.squads = 1
        self.vertical_map_movement = 0
        self.mission_images = bot.screenshot_data.data["missions"]
        self.map_stats = {
            "level_1": {
                "type_1": 3,
                "type_2": 1,
                "type_3": 1,
            },
            "level_2": {
                "type_1": 4,
                "type_2": 2,
                "type_3": 2,
            },
            "level_3": {
                "type_1": 5,
                "type_2": 2,
                "type_3": 3,
            },
            "level_4": {
                "type_1": 6,
                "type_2": 3,
                "type_3": 5,
            },
        }

    def resetMissionMap(self):
        pyautogui.click(40, 1070)
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
        pyautogui.dragTo(1000, 550, 1, button='left')
        pyautogui.click(300, 550)
        pyautogui.dragTo(300, 80, 1, button='left')
        self.clickEmptySpot()

    def moveToMissionSlotTwo(self):
        pyautogui.click(300, 900)
        pyautogui.dragTo(300, 390, 1, button='left')
        self.vertical_map_movement = 484
        self.clickEmptySpot()

    def moveBackToMissionSlotOne(self):
        pyautogui.click(300, 390)
        pyautogui.dragTo(300, 900, 1, button='left')
        self.clickEmptySpot()

    def clickEmptySpot(self):
        empty_space = self.map_screen["icons"]["empty_space"]
        self.game_bot.click(empty_space)

    def assignData(self, instructions):
        self.instructions = instructions
        self.squads = instructions["available_squads"]

    def processMissionStart(self, instructions):
        self.assignData(instructions)
        screenshot_helper = self.game_bot.screenshot_helper
        reset_area = self.claim_regions["reset_timer"]
        needs_mission_start = instructions["needs_mission_start"]
        missions_have_reset = instructions["missions_have_reset"]
        has_open_missions = instructions["has_open_missions"]
        print("instructions for mission start")
        print(instructions)

        if missions_have_reset:
            self.resetMissionMap()
            print("Scrap map points")
            reset_time = screenshot_helper.getScreenshotTime(reset_area)
            found_missions = self.scrapeMapPoints()
            data = {
                "found_missions": found_missions,
                "reset_time": reset_time
            }
            self.saveMissionPointsData(data)
            print("new map points saved")
        if needs_mission_start and has_open_missions:
            self.resetMissionMap()
            print("Reset map position: ")
            open_missions = instructions["open_missions"]
            check_open_missions_size = self.verifyMissionsExist(open_missions)
            print("All missions queued")
            print(check_open_missions_size)
            if len(open_missions) >= 1 and not missions_have_reset and check_open_missions_size:
                print("Select Open Missions")
                print(open_missions)
                select_mission_data = self.selectMissions(
                    open_missions)  # update
                print("new mission list")
                print(select_mission_data)
                save_data = {
                    "missions_selected": select_mission_data["missions_selected"],
                    "new_available_points": select_mission_data["new_available_points"],
                    "used_squads": select_mission_data["used_squads"],
                    "total_missions": select_mission_data["total_missions"]
                }
                # print("remaining missions")
                # print(remaining_missions)
                self.saveMissionsData(save_data)
                print("Missions start have been saved")

        self.returnToBattleScreen()

    def verifyMissionsExist(self, missions):
        for area in missions:
            for mission in missions[area]:
                if len(missions[area][mission]) >= 1:
                    return True
        return False

    def scrapeMapPoints(self):
        map_points = self.captureAllMapPoints()
        print("Got both screenshots")
        # print(map_points)
        # print("Map points before filter")
        # print(map_points)
        map_points = self.condenseMapPoints(map_points)
        print("Condensed map points")
        print(map_points)
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
        print("Assigned point data")
        print(self.condensed_point_data)
        self.removeDuplicateMissionPoints()
        # self.appendBothMapsToCondensedPoints()

        condensed_points = self.condensed_point_data["condensed_points"]
        # print(condensed_points)
        # sys.exit()
        return condensed_points

    def selectMissions(self, point_data):
        screenshot_helper = self.game_bot.screenshot_helper
        img = self.mission_images["mission_time_region"]
        instructions = self.instructions
        available_squads = instructions["available_squads"]
        mission_costs = {
            "type_1": 1,
            "type_2": 1,
            "type_3": 1,
            "type_4": 2,
        }
        types = ["type_1", "type_2", "type_3", "type_4"]
        missions_selected = []
        new_available_points = copy.deepcopy(point_data)

        selected_missions = {}
        available_squads = self.squads
        ok_button = self.map_screen["icons"]["start_ok"]
        empty_space = self.map_screen["icons"]["empty_space"]
        removed_index = 0
        new_mission_index = 1
        used_squads = 0

        self.moveToMissionSlotOne()
        self.moveToMissionSlotTwo()
        while (available_squads > 0):
            for select_type in types:
                self.moveBackToMissionSlotOne()
                for map_area in point_data:
                    if map_area == "map_2":
                        self.moveToMissionSlotTwo()
                    for mission_type in point_data[map_area]:
                        if mission_type == select_type:  # Only select the one mission type at a time. After that's selected, reset the map to position 1
                            for point in point_data[map_area][mission_type]:
                                mission_cost = mission_costs[mission_type]
                                if mission_cost <= available_squads and self.verifyMissionsExist(new_available_points):
                                    print("clicking map point")
                                    print(point)
                                    print(point_data[map_area])
                                    print(point_data)
                                    print(new_available_points)
                                    new_available_points[map_area][mission_type].remove(
                                        point)
                                    self.game_bot.click(point)
                                    time.sleep(1)
                                    img_time = screenshot_helper.getScreenshotTime(
                                        img)
                                    self.game_bot.click(ok_button)
                                    self.game_bot.click(empty_space)

                                    # Mission time needs buffer, otherwise uncompleted missions will register as completed
                                    # May need a more thorough explaination and solution on how this buffer bug in time is being created
                                    mission_selected_data = {
                                        "squad_cost": mission_cost,
                                        "time": int(img_time) + 200,
                                        "type": int(mission_type[-1])
                                    }
                                    new_mission_string = "mission_" + \
                                        str(new_mission_index)
                                    missions_selected.append(
                                        mission_selected_data)

                                    available_squads -= mission_cost
                                    new_mission_index += 1
                                    used_squads += mission_cost
                                else:
                                    print(
                                        "can't afford next mission, or no missions left to select")
                                    available_squads = -1
                                    break

        data = {
            "new_available_points": new_available_points,
            "missions_selected": self.sortMissions(missions_selected),
            "used_squads": used_squads,
            "total_missions": len(missions_selected)
        }

        print("New missions to save")
        print(data)

        return data

    def sortMissions(self, missions_selected):
        missions_selected
        missions_sorted = sorted(
            missions_selected, key=lambda option: option["time"])
        print("sorted mission selected")
        print(missions_sorted)
        return missions_sorted

    def saveMissionsData(self, point_data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveMissionsStarted(
            point_data, file)
        self.game_bot.db.saveDataFile()
        return True

    def saveMissionPointsData(self, point_data):
        file = self.game_bot.db.data
        self.game_bot.db.data = self.game_bot.db.saveMissionsPoints(
            point_data, file)
        self.game_bot.db.saveDataFile()
        return True

    def assignIconPointsToMissions(self):
        #print("condensesd data:")
        # print(self.condensed_point_data)

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
            # print(mission)
            condensed_points["map_1"][mission] = []
            remove_index_map_1[mission] = []
            remove_index_map_2[mission] = []
            index = 0
            for point in map_1[mission]:
                evaluated_point = map_1[mission][index]
                # print("evaluationnnnnnnnn")
                # print(evaluated_point)
                # print(map_2[mission])
                found_point = self.matchesOtherMapPoint(
                    evaluated_point, map_2[mission])
                if found_point is not None or found_point == 0:
                    # print("found match")
                    # print(found_point)
                    # print(point)
                    remove_index_map_2[mission].append(found_point)
                    remove_index_map_1[mission].append(point)
                    new_point = map_1[mission][index]
                    new_point["x"] = int(new_point["x"])
                    new_point["y"] = int(new_point["y"])
                    condensed_points["map_1"][mission].append(new_point)
                    # print(condensed_points["map_1"])
                index += 1

        #print("the condenseed points:")
        # print(condensed_points)

        self.condensed_point_data["condensed_points"] = condensed_points
        self.condensed_point_data["remove_index_map_1"] = remove_index_map_1
        self.condensed_point_data["remove_index_map_2"] = remove_index_map_2
        self.condensed_point_data["map_1"] = map_1
        self.condensed_point_data["map_2"] = map_2

        #print("remove indexes")
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
            current_index = 0
            # print(mission)
            # print(len(remove_index_map_1[mission]))
            # print(remove_index_map_1)
            for x in range(len(map_1[mission])):
                if (map_1[mission][current_index] in remove_index_map_1[mission]):
                    # print("deleted")
                    del map_1[mission][current_index]
                    current_index -= 1
                current_index += 1

        #print("next map")
        for mission in remove_index_map_2:
            current_index = 0
            # print(mission)
            # print(len(remove_index_map_2[mission]))
            # print(remove_index_map_2)
            # print(map_2)
            for x in range(len(map_2[mission])):
                if (map_2[mission][current_index] in remove_index_map_2[mission]):
                    # print("deleted")
                    del map_2[mission][current_index]
                    current_index -= 1
                current_index += 1

        #print("new maps")
        # print(map_1)
        # print(map_2)

        # Logic for # --- self.appendBothMapsToCondensedPoints ---
        new_points_to_add = {
            "map_1": map_1,
            "map_2": map_2
        }

        #print("new data")
        # print(new_points_to_add)
        # print(condensed_points)

        for area in new_points_to_add:
            for mission in available_missions:
                '''
                print(mission)
                print(area)
                print(len(condensed_points[area][mission]))
                '''
                mission_type_size = 0
                for new_point in new_points_to_add[area][mission]:
                    # print(new_points_to_add[area][mission])
                    new_points_to_add[area][mission]
                    mission_point = new_points_to_add[area][mission][mission_type_size]
                    mission_point["x"] = int(mission_point["x"])
                    mission_point["y"] = int(mission_point["y"])

                    condensed_points[area][mission].append(mission_point)
                    mission_type_size += 1
                # print(condensed_points)

        #print("final result")
        # print(condensed_points)
        self.condensed_point_data["condensed_points"] = condensed_points

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

    def matchesOtherMapPoint(self, evaluated_point, map_2_points):
        veritcal_diff = self.vertical_map_movement
        index = 0

        evaluated_point
        if map_2_points:
            for point in map_2_points:
                current_x = map_2_points[index]["x"]
                current_y = map_2_points[index]["y"]

                # Can only use 5 px buffer, because icons can be as close as 10-15 px next to each other on the map
                # rasing this to 15 will cause crashes if the game has icons that are too close to eachother
                x_cord_match = abs(evaluated_point["x"] - current_x) <= 5
                y_cord_match = abs(
                    evaluated_point["y"] - current_y) - veritcal_diff <= 5
                points_are_identical = x_cord_match and y_cord_match

                if points_are_identical:
                    return point
                index += 1
        return None

    def assignCondensedPointsData(self, map_points_all):
        condensed_points_data = {
            "map_1": map_points_all["map_1"],
            "map_2": map_points_all["map_2"],
            "remove_index_map_1": {},
            "remove_index_map_2": {},
            "condensed_points": {
                "map_1": {
                    "type_1": [],
                    "type_2": [],
                    "type_3": [],
                    "type_4": [],
                },
                "map_2": {
                    "type_1": [],
                    "type_2": [],
                    "type_3": [],
                    "type_4": [],
                },
            },
            "cp_index": 0,
            "available_missions": {"type_1", "type_2", "type_3", "type_4"}
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

    '''

    def returnToBattleScreen(self):
        empty_space = self.map_screen["icons"]["empty_space"]
        x_icon = self.map_screen["icons"]["x_icon"]
        self.game_bot.click(empty_space)
        self.game_bot.click(x_icon)

    def startMission(self):
        return True
