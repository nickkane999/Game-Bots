import pyautogui
import time
import re
import sys
import os
import copy

from actors.utilities.queue_instructions.QueueHelperTemplate import QueueHelperTemplate


class MapQueueHelper(QueueHelperTemplate):
    # Initializing Object
    def __init__(self):
        self.temp = "123"

    def getInstructions(self):
        results = {
            "mission_claim": {},
            "mission_start": {},
        }
        results["mission_claim"] = self.getMissionClaimInstructions()
        results["mission_start"] = self.getMissionStartInstructions()

        # print(results)
        return results

    def getMissionClaimInstructions(self):
        server = self.db.getServerString()
        mission_data = self.db.data[server]["map_progress"]
        items = mission_data["missions"]["in_progress"]
        save_time = mission_data["stats"]["save_time"]
        total_claims = 0
        unclaimed_missions = []
        index = 0

        for mission in items:
            print(mission)
            mission_time = mission["time"]
            needs_claim = self.hasEnoughTimePassed(mission_time, save_time)

            if needs_claim:
                total_claims += 1
            else:
                unclaimed_missions.append(mission)
                index += 1

        has_one_claim = total_claims >= 1
        results = {
            "needs_claim": has_one_claim,
            "mission_claim_count": total_claims,
            "mission_unclaimed_list": unclaimed_missions,
        }
        # print("Showing instructions for mission claim")
        # print(results)
        return results

    def getMissionStartInstructions(self):
        server = self.db.getServerString()
        map_data = self.db.data[server]["map_progress"]

        max_squads = map_data["stats"]["squad_count"]
        used_squads = map_data["missions"]["total_squads"]
        open_missions = map_data["missions"]["available"]
        available_squads = max_squads - used_squads

        open_missions_count = len(open_missions)

        needs_mission_start = True if available_squads > 0 and open_missions_count > 0 else False
        has_open_missions = True if open_missions else False

        # print(map_data)
        # print(map_data["stats"])
        save_time = map_data["stats"]["save_time"]
        reset_time = map_data["stats"]["reset_time"]
        passed_time = time.time() - save_time
        missions_have_reset = passed_time >= reset_time
        # print("passed_time")
        # print(passed_time)
        # print("reset_time")
        # print(reset_time)

        results = {
            "needs_mission_start": needs_mission_start,
            "available_squads": available_squads,
            "has_open_missions": has_open_missions,
            "open_missions": open_missions,
            "missions_have_reset": missions_have_reset
        }

        # print(results)
        #print("show mission start instructions, then quit")
        # sys.exit()

        return results
