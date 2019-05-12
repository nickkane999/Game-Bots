import pyautogui
import time

time.sleep(1)


# print(pyautogui.locateOnScreen('../Images/check.png', region=(1294, 3, 66, 64)))
print(pyautogui.locateOnScreen('../Images/allButton.png'))
print(pyautogui.locateOnScreen('../Images/allButton.png', region=(7, 389, 231, 52)))

print(pyautogui.locateCenterOnScreen('../Images/daily.PNG', region=(550, 600, 300, 100)))
x, y = pyautogui.locateCenterOnScreen('../Images/daily.PNG', region=(550, 600, 300, 100))
print(str(x) + ", " + str(y))

x, y = pyautogui.locateCenterOnScreen('../Images/allButton.png', region=(7, 389, 231, 52))
for z in range(0, 100):
	pyautogui.click(x, y)
# pyautogui.press('esc')

# pyautogui.click(550,600)
# pyautogui.click(750,660)