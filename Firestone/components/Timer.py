import pyautogui
import time
import re
import sys
import os


class Timer:
    # Initializing Object
    def __init__(self, data):
        self.data = data
        self.start_time = time.time()

    def startTimer(self):
        self.start_time = time.time()

    def getCurrentTime(self):
        return (time.time() - self.start_time)
