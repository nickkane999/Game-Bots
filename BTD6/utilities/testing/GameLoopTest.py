import pyautogui
import time
import re
import sys
import os

import easyocr
import pytesseract

from utilities.menus.MenuNavigator import MenuNavigator
from utilities.ScreenHelper import ScreenHelper
from utilities.TowerSelector import TowerSelector

from templates.TestTemplate import TestTemplate
from actors.Bot import Bot


class GameLoopTest(TestTemplate):
    # Initializing Object
    def __init__(self):
        super(GameLoopTest, self).__init__()
        self.menu_navigator = MenuNavigator()
        self.screenshot_helper = ScreenHelper()
        self.tests = self.getTests()
        self.bot = Bot()
        self.tower_selector = TowerSelector()
        self.current_trophies = 11
        self.extra_turrets = {
            "monkey village": {
                "point": {"x": 880, "y": 580}
            },
            "super monkey": {
                "point": {"x": 770, "y": 500}
            }
        }
        '''        
        self.extra_turrets = {
            "alchemist": {
                "point": {"x": 130, "y": 520}
            },
            "druid": {
                "point": {"x": 280, "y": 520}
            }
        }
        '''

    def getTests(self):
        return [
            self.runMapLoop
        ]

    def runMapLoop(self):
        menus = self.menu_navigator.menus
        home_menu = menus["1"]["home"]
        map_menu = menus["2"]["maps"]
        play_button = menus["2"]["maps"]

        self.runTestGameLoop()

    def runTestGameLoop(self):
        sh = self.screenshot_helper
        finish_info = {
            "area": (900, 880, 120, 70),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\BTD6\data\img\map_victory.png',
            "type": "victory"
        }
        play_info = {
            "area": (1800, 975, 70, 80),
            "taken_img": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\BTD6\data\img\map_play.png',
            "template_img": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\BTD6\data\img\play_button.png',
        }
        menus = self.menu_navigator.menus
        game_menu = menus["5"]["gamemap"]
        current_trophies = self.current_trophies

        start_time = time.time()

        for x in range(1000):
            if current_trophies >= 20:
                print("Done")
                break
            finished_process = False
            print("Starting Loop again")
            self.enterMapSelection()
            self.setTurrets()
            self.bot.click(game_menu["next_wave"])
            self.bot.click(game_menu["next_wave"])

            while (not finished_process):
                has_finished = sh.verifyMsg(finish_info, "next")
                if has_finished:
                    print("Map has finished")
                    self.exitMap()
                    finished_process = True
                    finish_time = time.time()
                    print("Total Passed time")
                    print(str(finish_time - start_time))
                    current_trophies += 1
                else:
                    sh.confirmImageMatch(play_info)
                    has_play_button = sh.confirmImageMatch(play_info)
                    if has_play_button:
                        self.bot.click(game_menu["level_accept"])
                        self.bot.click(game_menu["level_accept"])
                        time.sleep(0.5)
                        self.bot.click(game_menu["next_wave"])
                        self.bot.click(game_menu["empty_space"])
                    time.sleep(3)

    def clickOnDarkScreenIcons(self):
        info2 = {
            "area": (830, 930, 260, 140),
            "img_path": r'C:\Users\nickk\Dropbox\Portfolio\Game Bots\BTD6\data\img\map_continue.png',
            "type": "victory"
        }
        '''
        has_finished = sh.verifyMsg(info2, "continue")
        is_black = sh.checkIfImageBlack(info)
        print(is_black)
        print("Exiting")
        sys.exit()
        '''

    def exitMap(self):
        menus = self.menu_navigator.menus
        game_menu = menus["5"]["gamemap"]
        victory_next = game_menu["victory_next"]
        victory_home = game_menu["victory_home"]
        self.bot.click(victory_next)
        self.bot.click(victory_home)
        print("Finished map")

        # sleep while loading home menu
        time.sleep(5)

    def setTurrets(self):
        menus = self.menu_navigator.menus
        game_menu_upgrades = menus["5"]["gamemap"]["upgrade_slots"]

        self.setExtraTurrets()
        self.setTurretsCornMap()

        '''
        tower_point = {"x": 480, "y": 520}
        self.tower_selector.placeTower("hero", tower_point)

        tower_point = {"x": 470, "y": 390}
        self.tower_selector.placeTower("monkey village", tower_point)
        self.bot.click(tower_point)
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_3"])
        self.bot.click(game_menu_upgrades["slot_3"])

        tower_point = {"x": 650, "y": 380}
        self.tower_selector.placeTower("super monkey", tower_point)
        self.bot.click(tower_point)
        self.bot.click(game_menu_upgrades["slot_1"])
        self.bot.click(game_menu_upgrades["slot_1"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        '''

    def setTurretsCornMap(self):
        menus = self.menu_navigator.menus
        game_menu_upgrades = menus["5"]["gamemap"]["upgrade_slots"]["left"]

        tower_point = self.extra_turrets["monkey village"]["point"]
        self.bot.click(tower_point)
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_3"])
        self.bot.click(game_menu_upgrades["slot_3"])

        tower_point = self.extra_turrets["super monkey"]["point"]
        self.bot.click(tower_point)
        self.bot.click(game_menu_upgrades["slot_1"])
        self.bot.click(game_menu_upgrades["slot_1"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        self.bot.click(game_menu_upgrades["slot_2"])
        tower_point = {"x": 760, "y": 590}
        self.tower_selector.placeTower("hero", tower_point)

    def setExtraTurrets(self):
        extra_turrets = self.extra_turrets
        for turret in extra_turrets:
            self.tower_selector.placeTower(
                turret, extra_turrets[turret]["point"])

    def enterMapSelection(self):
        home_menu = self.menu_navigator.menus["1"]["home"]
        self.bot.click(home_menu["play"])
        time.sleep(1)

        '''
        settings = {
            "map": "monkey meadow",
            "stage_difficulty": "beginner",
            "mode_difficulty": "easy",
            "mode_option": "deflation"
        }
        '''
        settings = {
            "map": "cargo",
            "stage_difficulty": "advanced",
            "mode_difficulty": "easy",
            "mode_option": "deflation"
        }
        self.selectMap(settings)
        print("I entered map")
        # sys.exit()

    def selectMap(self, settings):
        stage_difficulty = settings["stage_difficulty"]
        mode_difficulty = settings["mode_difficulty"]
        map_button = settings["map"]
        mode = settings["mode_option"]

        map_menu = self.menu_navigator.menus["2"]["maps"]
        difficulty_menu = self.menu_navigator.menus["3"]["difficulty"]
        options_menu = self.menu_navigator.menus["4"][mode_difficulty]
        game_menu = self.menu_navigator.menus["5"]["gamemap"]

        self.resetMapOptions(stage_difficulty)
        self.bot.click(map_menu["next_arrow"])
        self.bot.click(map_menu[stage_difficulty][map_button])
        self.bot.click(difficulty_menu[mode_difficulty])
        self.bot.click(options_menu[mode])
        self.bot.click(options_menu["overrite_save"])

        # sleep while loading map
        time.sleep(5)
        if mode == "deflation":
            self.bot.click(game_menu["deflation_ok"])
        self.bot.click(options_menu["overrite_save"])
        self.bot.click(options_menu["overrite_save"])
        time.sleep(2)

    def resetMapOptions(self, current_difficulty):
        map_menu = self.menu_navigator.menus["2"]["maps"]
        difficulties = ["beginner", "intermediate", "advanced", "expert"]
        for mode in difficulties:
            if mode is not current_difficulty:
                self.bot.click(map_menu["navigation"][mode])
                break
        self.bot.click(map_menu["navigation"][current_difficulty])

    def getMenuOneTowers(self):
        towers = {
            "hero": {"x": 1710, "y": 220},
            "dart monkey": {"x": 1820, "y": 220},
            "boomerang monkey": {"x": 1710, "y": 350},
            "bomb shooter": {"x": 1820, "y": 350},
            "tack shooter": {"x": 1710, "y": 500},
            "ice monkey": {"x": 1820, "y": 500},
            "glue gunner": {"x": 1710, "y": 620},
            "sniper monkey": {"x": 1820, "y": 620},
            "monkey sub": {"x": 1710, "y": 750},
            "monkey buccaneer": {"x": 1820, "y": 750},
            "monkey ace": {"x": 1710, "y": 900},
            "heli pilot": {"x": 1820, "y": 900},
        }
        return towers
