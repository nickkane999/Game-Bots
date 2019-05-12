import pyautogui
import time
from Bot import Bot

# Set pause time between clicks/mouse movements
pyautogui.PAUSE = 0.05

# Allow time to enter "Idle Champions" interface
time.sleep(2.5)

# Set Parameters
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
sessionTime = time.time() + 300 # In seconds
bot = Bot(30, int(screenWidth/2), int(screenHeight/2))

# while time.time() < sessionTime:
	# bot.checkStatus()
bot.upgradePeople()
	# bot.killEnemies()