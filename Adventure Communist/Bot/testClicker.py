import pyautogui
import time
from Bot import Bot

# Allow time to enter "Adventure Communist" interface
time.sleep(2.5)

# Set Parameters
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
pyautogui.PAUSE = 0.01 	# Pause time between clicks/mouse movements
sessionTime = time.time() + 300 # In seconds
bot = Bot(5, 5)

while time.time() < sessionTime:

os.startfile("C:/Program Files (x86)/Steam/steamapps/common/AdVenture Communist/adventure-communist.exe")
time.sleep(2)
pyautogui.press('enter')




bot.farmResources()
