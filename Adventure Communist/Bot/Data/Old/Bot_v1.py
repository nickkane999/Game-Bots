import pyautogui

# Set pause time between clicks/mouse movements
pyautogui.PAUSE = 0.01


# pyautogui.moveTo(1000, 250)
# pyautogui.click()
# pyautogui.moveRel(None, 10)

class Bot:

	def __init__(self, farmTime):
		self.farmTime = farmTime
		
	def farmResources(self):
		pyautogui.moveTo(140, 420)
		for i in range(int(self.farmTime / pyautogui.PAUSE)):
			pyautogui.click()
