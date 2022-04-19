import pyautogui
import time
import re
import sys
import os

os.startfile(
    "C:/Program Files (x86)/Steam/steamapps/common/AdVenture Communist/adventure-communist.exe")
time.sleep(2)
pyautogui.press('enter')


class Bot:
	# Variables
	rotationsAfterBoss = 0

	# Initializing Object
	def __init__(self, clickTime):
		self.clickTime = clickTime
		self.bossLost = False
		# self.screenWidth = screenWidth
		# self.screenHeight = screenHeight

	# Major object functions
	def upgradePeople(self):
		coins = list(pyautogui.locateAllOnScreen(
		    'images/coin.png', region=(0, 0, 300, 400)))
		if coins:														# Checks if people upgrades exist
			for item in coins:											# Clicks on each available people upgrade in order
				# for x in range(0, 3):									# Clicks earlier upgrade 3 times before progressing (earlier upgrades are better)
				self.clickItem(item)

	def killEnemies(self):
		tempTime = time.time() + self.clickTime
		while time.time() < tempTime:									# Clicks on center of screen for set amount of time
			pyautogui.click(self.screenWidth, self.screenHeight)

	def checkStatus(self):
		self.checkSpecialization()
		self.checkAutoRun()
		self.useSpecials()

	# checkStatus Helper Functions

	def checkSpecialization(self):
		# Check if specialization screen is active
		if pyautogui.locateOnScreen('images/specialization.png') is not None:
			self.addSpecialization()

	def checkAutoRun(self):
		autoButton = pyautogui.locateOnScreen('images/stopAutoProgress.png')
		if autoButton is not None:
			self.clickItem(autoButton)

	def useSpecials(self):
		pyautogui.typewrite('123456789')

	# checkSpecialization Helper Function
	# Temp solution: Need to add process for understanding/selecting upgrades depending on different people

	def addSpecialization(self):
		buttons = list(pyautogui.locateAllOnScreen(
		    'images/selectSpecialization.png'))
		self.clickItem(buttons[0])

	def tempUpgrade(self):
		if pyautogui.locateOnScreen('images/specialization.png', region=(520, 80, 325, 72) is not None:
			print("Specialization Title Fund")
			if pyautogui.locateOnScreen('images/troops/Celeste.png', region=(755, 230, 165, 30) is not None:
				print("Specific person found"


	# General Helper Functions
	def clickItem(self, button):
		cordX, cordY=pyautogui.center(button)
		pyautogui.click(cordX, cordY)

# Extra: If bot program changes folders
# file_path = "C:/Users/Nick Kane/Dropbox/Work/Projects/Personal Projects/CMS Uploading/Functions" # File path holding Upload CMS program
# sys.path.insert(0, file_path)
# folder_name = "../Data/chromedriver.exe"
# Get file path from parent	for user info and driver
# dir = os.path.dirname(__file__)
# all_people_filename = os.path.join(dir, user_filename)
