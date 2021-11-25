import json

from utilities.DataFiles import DataFiles

class SaveData:

    def __init__(self, data):
        self.data_files = DataFiles()

        self.database = data["data_file"]
        self.getDB()

    def getDB(self):
        db_file = self.database
        self.db = self.data_files.pullData(db_file)

    def saveDB(self):
        db_file = self.database
        dictionary = self.data
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def saveDBRaw(self, dictionary):
        db_file = self.database
        with open(db_file, 'w') as outfile:
            json.dump(dictionary, outfile, indent=4, sort_keys=True)

    def runVerificationCheck(self):
        print("I was set up correctly")
