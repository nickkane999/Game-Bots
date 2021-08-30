import pyautogui
import time
import re
import sys
import os
import cv2
import numpy as np

from templates.MapTemplate import MapTemplate
from templates.TowerTemplate import TowerTemplate


class MonkeyMedow(MapTemplate):
    # Initializing Object
    def __init__(self):
        super(ServerSwapSaveHelper, self).__init__()
        self.tower_data = TowerTemplate()
        self.towers = self.loadTowerPlacements()

    def loadTowerPlacements(self):
        towers = {

        }
