import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np
from abc import ABC, abstractmethod


class MenuDataTemplate(ABC):
    # Initializing Object
    def __init__(self):
        self.test = "123"

    @abstractmethod
    def getOptions(self):
        pass
