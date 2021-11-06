from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import selenium
import time
import os
import glob
import shutil
from time import sleep
import json
import sys
from actors.GameUI import GameUI



class BattleRoyale:
    # Initializing Object
    def __init__(self, bot):
        self.bot = bot
        self.GameUI = GameUI(bot)
        self.reset()

    def reset(self):
        self.stats = {
            "players_left": 50,
            "hp": 500,
            "vitality": 50,
            "kills": 0,
            "attack_counter": 0,
            "heal_boosts": 5,
            "vitality_boosts": 3,
        }
        self.xpaths = self.bot.save_data.db["xpaths"]
        self.style = "passive"
        self.heal_limit = 80
        self.style_data = {
            "passive": {
                "attack_health": 24
            },
            "aggressive": {
                "attack_health": 45
            },
            "hyper_aggressive": {
                "attack_health": 60
            },
            "no_restriction": {
                "attack_health": 300
            }
        }

    def setEquipment(self):
        self.setWeapon();
        self.setArmor();
        self.aidPlayer();

    def setWeapon(self):
        found_best_weapon = False
        best_weapon_stat = 0

        for weapon_slot in range(0, 4):
            weapon_strength_xpath = self.xpaths["battle_royale"]["weapon_slot_strength"].replace("NNN", str(weapon_slot))
            weapon_strength = self.bot.getValue(weapon_strength_xpath)
            if weapon_strength:
                print("Weapon slot " +str(weapon_slot)+ " power: " + weapon_strength)
            if weapon_strength and int(weapon_strength) > best_weapon_stat:
                best_weapon = self.xpaths["battle_royale"]["weapon_slot"].replace("NNN", str(weapon_slot))
                best_weapon_stat = int(weapon_strength)
                found_best_weapon = True
            self.aidPlayer();
        
        if found_best_weapon:
            print("I'm the best weapon slot: " + best_weapon)
            self.bot.clickElement(best_weapon)
        else:
            print("No weapon acquired yet")
                
    def setArmor(self):
        found_best_armor = False
        best_armor_stat = 0
        for armor_slot in range(0, 4):
            armor_strength_xpath = self.xpaths["battle_royale"]["armor_slot_strength"].replace("NNN", str(armor_slot))
            armor_strength = self.bot.getValue(armor_strength_xpath)
            if armor_strength:
                print("Armor slot " +str(armor_slot)+ " power: " + armor_strength)
            if armor_strength and int(armor_strength) > best_armor_stat:
                best_armor = self.xpaths["battle_royale"]["armor_slot"].replace("NNN", str(armor_slot))
                best_armor_stat = int(armor_strength)
                found_best_armor = True
                self.aidPlayer();
        
        if found_best_armor:
            print("I'm the best armor slot: " + best_armor)
            self.bot.clickElement(best_armor)
        else:
            print("No armor acquired yet")



    def setStrategy(self):
        player_count = self.getPlayerCount()
        if not player_count:
            self.style = "passive"
        if player_count and player_count <= 5:
            print("No restrictions strategy")
            if self.haveMoreVitality() or player_count <= 2:
                self.style = "no_restriction"
            else:
                self.style = "hyper_aggressive"
        elif player_count < 30:
            if self.stats["vitality"] >= 50 or self.haveMoreVitality():
                self.style = "hyper_aggressive"    
            else:
                self.style = "aggressive"
        else:
            self.style = "passive"

        if player_count and player_count >= 35:
            self.heal_limit = 110
        else:
            self.heal_limit = 80

    def haveMoreVitality(self):
        self.pullBoostCounts()
        heal_boosts = self.stats["heal_boosts"]
        vitality_boosts = self.stats["vitality_boosts"]

        if vitality_boosts > heal_boosts:
            return True
        else:
            return False

    def pullBoostCounts(self):
        heal_boosts = self.xpaths["battle_royale"]["heal_boost_count"]
        vitality_boosts = self.xpaths["battle_royale"]["vitality_boost_count"]

        heal_text = self.bot.getValue(heal_boosts)
        vitality_text  = self.bot.getValue(vitality_boosts)

        if heal_text:
            self.stats["heal_boosts"] = int(heal_text.replace(' Med Kits', ''))
        if vitality_text:
            self.stats["vitality_boosts"] = int(vitality_text.replace(' Vitality Boosts', ''))


    def getPlayerCount(self):
        players_left = self.xpaths["battle_royale"]["player_count"]
        players_left = self.bot.getValue(players_left)
        if players_left:
            players_left = int(players_left.replace(' / 50', ''))
        else:
            players_left = False

        return players_left


    def healSelfLoop(self, loop_time):
        start_time = time.time()
        passed_time = time.time() - start_time
        time_left = loop_time - passed_time

        print("Total game time: " + str(time_left))
        loop_count = 0

        while time_left > 0:
            time.sleep(0.2)
            self.aidPlayer()
            passed_time = time.time() - start_time
            time_left = loop_time - passed_time
            loop_count = loop_count + 1
            if loop_count % 5 == 0:
                print("Time left: " + str(time_left))

    def aidPlayer(self):
        print ("Aiding self")
        self.healPlayer()
        self.boostPlayerVitality()


    def healPlayer(self):
        heal_limit = self.heal_limit

        health_element = self.xpaths["battle_royale"]["health"]
        current_health = self.bot.getValue(health_element)
        if current_health:
            current_health = int(current_health.replace('/500', ''))

        if current_health and current_health < heal_limit:
            heal_button = self.xpaths["battle_royale"]["heal"]
            clicked = self.bot.clickElement(heal_button)
            if clicked:
                print("Healing player")
            self.stats["hp"] = 500
        else:
            # print("Waiting to heal player")
            self.stats["hp"] = current_health
        self.stats["hp"] = current_health

    def boostPlayerVitality(self):
        vitality_element = self.xpaths["battle_royale"]["vitality"]
        current_vitality = self.bot.getValue(vitality_element)
        if current_vitality:
            current_vitality = int(current_vitality)

        if current_vitality and current_vitality < 10:
            vitality_button = self.xpaths["battle_royale"]["vitality_boost"]
            clicked = self.bot.clickElement(vitality_button)
            if clicked:
                print("Boosted player vitality")
                self.stats["vitality"] = 35
        else:
            # print("Waiting to boost vitality player")
            self.stats["vitality"] = current_vitality        




    def attackEnemiesLoop(self, loop_time):
        start_time = time.time()
        passed_time = time.time() - start_time
        time_left = loop_time - passed_time

        print("Total game time: " + str(time_left))
        loop_count = 0

        while time_left > 0:
            time.sleep(0.2)
            self.attackEnemies()
            self.setEquipment()
            self.checkMenu()
            passed_time = time.time() - start_time
            time_left = loop_time - passed_time
            loop_count = loop_count + 1
            if loop_count % 5 == 0:
                self.setStrategy()
                print("Time left: " + str(time_left))

    def checkMenu(self):
        game_id = self.xpaths["battle_royale"]["game_id"]
        game_id_text = self.bot.getValue(game_id)
        if not game_id_text:
            print("Not in game")
            print(asdasd)


    def attackEnemies(self):
        bot = self.bot
        driver = self.bot.driver
        strategy = self.style
        health_limit = self.style_data[strategy]["attack_health"]

        for x in range(2, 50):
            # print("Looking at player " + str(x))
            health = self.getEnemyHealth(x)
            # if not health:
                # print("Did not find player " + str(x))
            if health and health <= health_limit:
                print("Attacking health=" + str(health) + ", player=" + str(x))
                self.aidPlayer()
                self.attackPlayer(x)
            if x % 5 == 0:
                self.aidPlayer()

    def attackPlayer(self, player_id):
        xpath = self.xpaths["battle_royale"]["attack"].replace("NNN", str(player_id))
        strategy = self.style
        health_limit = self.style_data[strategy]["attack_health"]

        clicked = self.bot.clickElement(xpath)
        if clicked:
            print ("Clicking player " + str(player_id))
            health = self.getEnemyHealth(player_id)
            if health and health < health_limit:
                print("My health limit " + str(health_limit))
                time.sleep(0.2)
                self.aidPlayer()
                self.stats["attack_counter"] += 1
                if self.stats["attack_counter"] % 10 == 0:
                    self.setEquipment()
                    
                self.attackPlayer(player_id)
                # self.healPlayer()
                # self.boostPlayerVitality()

        self.aidPlayer()


    def getEnemyHealth(self, player_id):
        xpath = self.xpaths["battle_royale"]["enemy_health"].replace("NNN", str(player_id))
        name = self.bot.getCSSAttribute(xpath, 'width')
        if name:
            health = float(name.replace('px', ''))
            print ("Getting health:" + str(health))
        else:
            health = False

        return health

