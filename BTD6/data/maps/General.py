import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np

from templates.MapTemplate import MapTemplate
from templates.TowerTemplate import TowerTemplate


class General(MapTemplate):
    # Initializing Object
    def __init__(self):
        super(ServerSwapSaveHelper, self).__init__()
        self.tower_data = TowerTemplate()
        self.options = self.getMapOptions()

    def getMapOptions(self):
        options = {
            "victory next": {"x": 960, "y": 900},
        }
