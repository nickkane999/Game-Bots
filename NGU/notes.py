import pyautogui
import time

def startProgram():
    gear_pos = (1025, 200)
    inv_pos = (1515, 675)
    inv_start_pos = (765, 600)
    counter = 0

    positions = {
        (-75, 0),
        (-75, 75),
        (-75, 150),
        (0, 75),
        (75, 75),
        (0, 150),
        (0, 225)
    }

    inv_positions = {
        (-150, 150),
        (-75, 150),
        (0, 150),
        (75, 150),
        (-75, 0),
        (-75, -75),
        (-75, 75),
        (0, 0),
        (0, 75),
        (0, -75),
        (75, 0),
        (75, 75),
        (75, -75),        
        (-150, 0),
        (-150, -75),
        (-150, 75),
        (-225, 0),
        (-225, -75),
        (-225, 75),
        (-300, 0),
        (-300, -75),
        (-300, 75),
    }

    inv_start_positions = {
        (0, 0),
        (75, 0),
        (150, 0),
        (225, 0),
        (300, 0),
        (375, 0),
        (0, 75),
        (75, 75),
        (150, 75),
        (225, 75),
        (300, 75),
        (375, 75),
        (0, 150),
        (75, 150),
        (150, 150),
        (225, 150),
        (300, 150),
        (375, 150),
    }
    
    while True:
        counter = counter + 1
        modifyGear('a', gear_pos, positions, True)
        modifyGear('a', inv_pos, inv_positions)
        modifyGear('d', gear_pos, positions)
        modifyGear('d', inv_pos, inv_positions)
        if counter % 1000 == 0:
            modifyGear('ctrl', inv_start_pos, inv_start_positions)
        print("I upgraded gear. Sleeping")
        time.sleep(10)

def modifyGear(key, start_pos, points, multiple_clicks = False):
    start_x = start_pos[0]
    start_y = start_pos[1]
    pyautogui.moveTo(start_x, start_y)
    pyautogui.keyDown(key)
    time.sleep(0.5)
    if multiple_clicks:
        for x in range(0, 5):
            for point in points:
                pyautogui.click(start_x + point[0], start_y + point[1])
                time.sleep(0.3)
    else:
        for point in points:
            pyautogui.click(start_x + point[0], start_y + point[1])
            time.sleep(0.3)
    time.sleep(1)
    pyautogui.keyUp(key)


# unsure on resolution

time.sleep(5)
print("Starting program")
startProgram()
