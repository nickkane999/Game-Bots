import pyautogui
import time
import sys, os
import datetime
# import win32api
# import pywin32
def change(s):
    if s == 1:os.system('date -s "2 OCT 2006 18:00:00"')#don't forget to change it , i've used date command for linux 
    elif s == 2:
        try:
          import win32api
        except ImportError:
          print('pywin32 module is missing')
          sys.exit(1)
        pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )# fill all Parameters with int numbers
    else:print('wrong param')
def check_os():
    if sys.platform=='linux2':change(1)
    elif  sys.platform=='win32':change(2)
    else: print('unknown system')
change(1)

pyautogui.PAUSE = 0.01 	# Pause time between clicks/mouse movements

def main(loops):
	for x in range(0, loops):
		startGame()
		playGame()

# Opens game, and waits until game loading is complete
def startGame():
	# Start game parameters
	checkIconRegion = (1294, 3, 66, 64)
	checkIcon = "Images/check.PNG"

	# Opens the game by running EXE file
	os.startfile("C:/Program Files (x86)/Steam/steamapps/common/AdVenture Communist/adventure-communist.exe")
	time.sleep(2)
	pyautogui.press('enter')
	
	# Waits until check image appears; if not, exit the program
	for x in range(0, 10):
		if pyautogui.locateOnScreen(checkIcon, region=checkIconRegion) is not None:
			break
		else:
			time.sleep(1)
		if x == 10:
			sys.exit("Game was not loaded successfully")

# Clicks through game to get resources and scientists
# Closes the game after a capsule isn't grabbed for 20 click itterations
def playGame():
	# Play Game Parameters
	checkIconRegion = (1294, 3, 66, 64)
	capsuleRegion = (550, 600, 300, 100)
	resourceButtonRegion = (7, 389, 231, 52)
	capsuleButton = "Images/daily.PNG"
	resourceButton = "Images/allButton.PNG"
	checkIcon = "Images/check.PNG"
	clickItteration = 70
	doneClicking = False
	clicksWithNoCapsule = 0
	
	while not doneClicking:
		if pyautogui.locateOnScreen(resourceButton, region=resourceButtonRegion) is not None:						# Resource button is on the screen
			click(resourceButton, resourceButtonRegion, clickItteration)
		clicksWithNoCapsule = getCapsule(capsuleButton, capsuleRegion, clicksWithNoCapsule)							# Clicks on capsule button is on the screen
		if pyautogui.locateOnScreen(checkIcon, region=checkIconRegion) is None:										# Re-enters game screen if tabbed out; exits program if game screen can't be re-entered
			startGame()																								# Re-enters the game
			clicksWithNoCapsule = getCapsule(capsuleButton, capsuleRegion, clicksWithNoCapsule)
			if pyautogui.locateOnScreen(checkIcon, region=checkIconRegion) is None:
				sys.exit("Game screen cannot be read")
		if clicksWithNoCapsule >= 15:																				# Exits the game after 15 click itterations
			doneClicking = True
			endGame()

def getCapsule(button, region, loops):
	if pyautogui.locateOnScreen(button, region=region) is not None:
		click(button, region, 2)
		loops = 0
		time.sleep(2.5)
		pyautogui.click(100, 100)
		time.sleep(1)
	else:
		loops = loops + 1
		pyautogui.click(100, 100)
	return loops
	
def endGame():
	pyautogui.press('esc')

def	click(img, region, n):
	x, y = pyautogui.locateCenterOnScreen(img, region=region)
	for z in range(0, n):
		pyautogui.click(x, y)

time_tuple = ( 2017, 17, 12, 0, 38, 0, 0,) # (Month, Day, Hour, Min, Sec, MilliSec)

def changeTime(time_tuple):
	# http://timgolden.me.uk/pywin32-docs/win32api__SetSystemTime_meth.html
	# pywin32.SetSystemTime(year, month , dayOfWeek , day , hour , minute , second , millseconds )\
	dayOfWeek = datetime.datetime(time_tuple).isocalendar()[2]
	pypiwin32.SetSystemTime( time_tuple[:2] + (dayOfWeek,) + time_tuple[2:])
	time_tuple[2] = time_tuple[2] + 1
	return time_tuple

# main(1)
# changeTime(time_tuple)
