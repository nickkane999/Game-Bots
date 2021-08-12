import pyautogui
import time
import tkinter
root = tkinter.Tk()

def keyevent(event):
        # Check if pressed key has code 67 (character 'c')
        if event.keycode == 67:
                for x in range(1, 20):
                        pyautogui.mouseDown();
                        time.sleep(0.33);
                        pyautogui.mouseUp();
                        time.sleep(0.33);

root.bind("<Control - Key>", keyevent) # You press Ctrl and a key at the same time   

root.mainloop()

pyautogui.mouseDown();
time.sleep(0.33);
pyautogui.mouseUp();
time.sleep(0.33);
