import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np
from abc import ABC, abstractmethod


class TestTemplate(ABC):
    # Initializing Object
    def __init__(self):
        self.class_name = self.getClass()

    @abstractmethod
    def getTests(self):
        pass

    def runTest(self):
        for test in self.getTests():
            test()

    def getClass(self):
        # print(type(self).__name__)
        return type(self).__name__
