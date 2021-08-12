import cv2
import numpy as np
import pyautogui

im1 = pyautogui.screenshot()
im1.save(r"C:\Users\nickk\Dropbox\Portfolio\Game Bots\Firestone\zTests\map_image.png")
taken_image = cv2.imread('map_image.png')

# load pass_image
pass_image = cv2.imread('map_small_mission.png')

# read height and width of pass_image image
w, h = pass_image.shape[0], pass_image.shape[1]

res = cv2.matchTemplate(taken_image, pass_image, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(taken_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
    print(str(pt[0]) + ", " + str(pt[1]))

taken_image = cv2.resize(taken_image, (800, 600))
cv2.imshow("result", taken_image)
cv2.waitKey(10000)
