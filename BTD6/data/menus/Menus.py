from data.menus.menu1.HomeMenu import HomeMenu
from data.menus.menu2.MapMenu import MapMenu
from data.menus.menu3.DifficultyMenu import DifficultyMenu
from data.menus.menu4.EasyMenu import EasyMenu
from data.menus.menu5.GameMapMenu import GameMapMenu


class Menus:
    # Initializing Object
    def __init__(self):
        self.data = self.loadMenus()

    # Major object functions
    def loadMenus(self):
        menus = {
            "1": {
                "home": HomeMenu().options
            },
            "2": {
                "maps": MapMenu().options,
            },
            "3": {
                "difficulty": DifficultyMenu().options
            },
            "4": {
                "easy": EasyMenu().options
            },
            "5": {
                "gamemap": GameMapMenu().options
            }
        }
        return menus
