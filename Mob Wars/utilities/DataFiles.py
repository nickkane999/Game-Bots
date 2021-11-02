import pyautogui
import time
import re
import sys
import os
import json


class DataFiles:

    def pullData(self, path):
        with open(path) as json_file:
            data = json.load(json_file)
            json_file.close()
            return data

    def pullTextData(self, path):
        with open(path) as file:
            data = file.read()
            return data

    def saveDataFile(self):
        db_file = self.db_file
        dictionary = self.data
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def saveDataFileRaw(self, dictionary):
        db_file = self.db_file
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def getServerString(self):
        return "server_" + self.data["general"]["current_server"]
