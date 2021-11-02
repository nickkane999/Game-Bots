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

# from commonFunctions import *
# from SegmentedData import *


class Bot:
    # Initializing Object
    def __init__(self, data):
        self.instructions = data['instructions']
        self.browser = data['browser']
        self.driver = data['browser'].driver
        self.save_data = data['save_data']
        

    def clickElement(self, xpath):
        driver = self.driver

        try:
            div = driver.find_element_by_xpath(xpath)
            div.click()
            time.sleep(0.33)
            return True
        except Exception as e:
            print("Xpath for click couldnt be processed")
            # print(traceback.format_exc())
            return False

    def getValue(self, xpath):
        driver = self.driver
        element = driver.find_element_by_xpath(xpath)

        try:
            return element.text
        except Exception as e:
            print("Xpath for text couldnt be processed")
            # print(traceback.format_exc())
            return False
    
    def getCSSAttribute(self, xpath, name):
        driver = self.driver

        try:
            element = driver.find_element_by_xpath(xpath)
            return element.value_of_css_property(name)
        except Exception as e:
            print("Xpath for css property couldnt be processed")
            # print(traceback.format_exc())
            return False

    def getAttributeValue(self, xpath, name):
        # name = "onclick"
        # xpath = "'//*[@id=\"chat-msgs-box\"]/div[50]/div[2]/span[1]'"
        driver = self.driver

        try:
            element = driver.find_element_by_xpath(xpath)
            return element.get_attribute(name)
        except Exception as e:
            print("Xpath for attribute " + name + " couldnt be processed")
            # print(traceback.format_exc())
            return False
        

    def switchToIFrame(self):
        iframe = self.driver.find_element_by_xpath('//*[@id="gamefilearea"]//iframe')
        self.driver.switch_to.frame(iframe)

        # iframe = driver.find_element_by_xpath(xpath)
        # self.driver.switch_to.frame(iframe)

        # //*[@id="main_menu_div"]/div/table/tbody/tr/td[4]/a

    def pullMobs(self):
        data = self.save_data.db
        self.xpaths = data["xpaths"]
        # self.filterJobPosts()
        self.pullMobsFromPost()

    def addMobs(self, mob_add_scripts):
        data = self.save_data.db
        self.xpaths = data["xpaths"]
        for script in mob_add_scripts:
            self.driver.execute_script(script)
            time.sleep(0.5)



    def filterJobPosts(self):
        xpaths = self.xpaths
        shop = xpaths["side_menu"]["shop"]
        job = xpaths["side_menu"]["job"]

        shop.click()
        job.click()

    def pullMobsFromPost(self):
        xpaths = self.xpaths
        add_scripts = []
        for message in range(0, 50):
            add_link = xpaths["mobs"]["add_member_post"].replace("NNN", str(message))
            name = self.getAttributeValue(add_link, "onclick")
            if name and "add_friend" in name:
                # self.driver.execute_script(name)
                print(name)
                add_scripts.append(name)

        print("My scripts")
        print("--------")
        print("--------")
        print("--------")
        print(add_scripts)


    def addMobsRecommended(self):
        data = self.save_data.db
        self.xpaths = data["xpaths"]
        xpaths = self.xpaths
        print(data)
        xpath = xpaths["mobs"]["recruit_tab"]
        self.clickElement(xpath)
        for person in range(0, 100):
            xpath = xpaths["mobs"]["add_member_recommended"].replace("NNN", str(person))
            clicked = self.clickElement(xpath)
            if not clicked:
                print("Couldn't find any more mob members to invite")
                break;
        
        print("Finished processing adding mobs")


    def runFights(self, risk_information):
        data = self.save_data.db
        self.xpaths = data["xpaths"]
        print(data)
        for rounds in range(1, 100):
            if risk_information:
                self.startFight(risk_information)
                round_limit = risk_information['rounds']
                if rounds > round_limit:
                    print("Finished fights with risk")
                    break;
        
        print("Finished processing fights")


    def runFightsLoop(self, risk_information):
        while True:
            self.runFights(risk_information)
            print("Finished fight Loop, waiting 1 minute")
            time.sleep(60)

    def startFight(self, risk_information):
        xpaths = self.xpaths
        mob_size_limit = risk_information['mob_count']

        for x in range(2, 17):
            xpath = xpaths["fight"]["mob_menu"]["mob_count"].replace("NNN", str(x))
            # print(xpath)
            mobs = self.getValue(xpath)
            print("Mobs: ")
            print(mobs)
            xpath = xpaths["fight"]["mob_menu"]["health"].replace("NNN", str(x))
            # print(xpath)
            health = self.getCSSAttribute(xpath, 'width')
            if health:
                health = float(health.replace('px', ''))

            if not mobs:
                print("No mobs found")


            if mobs and int(mobs) < mob_size_limit and health >= 152:
                print("Mobs found")
                xpath = xpaths["fight"]["mob_menu"]["attack"].replace("NNN", str(x))
                print(xpath)
                self.clickElement(xpath)
                self.finishFight()
                print("restart fights loop")
                break;

            if x == 15:
                print("Loading new fights")
                fights = xpaths["main_menu"]["fight"]
                self.clickElement(fights)
                break;

        
        print("Finished startFights")

    
    def finishFight(self):
        xpaths = self.xpaths
        
        xpath = xpaths["fight"]["fight_menu"]["result"]
        value = self.getValue(xpath)
        if value == 'WON':
            attack = xpaths["fight"]["fight_menu"]["attack"]
            self.clickElement(attack)
            self.continueFight()

        fights = xpaths["main_menu"]["fight"]
        self.clickElement(fights)
        print("finished fight")

    def continueFight(self):
        xpaths = self.xpaths
        attack = xpaths["fight"]["fight_menu"]["attack"]
        if attack:
            clicked = self.clickElement(attack)
            if clicked:
                self.continueFight()
        



    ############################################
    # Old Functions
    ############################################


''' 
    def openTemplateFile(self):
        actionComplete = self.openTemplate();
        time.sleep(1);
        result = True if actionComplete else False;
        return result;

    def changeImageLogo(self, position, imgSize):
        actionComplete = self.deleteImage()
        actionComplete = self.openImage() if actionComplete else self.log.writeError('Image was not oppened successfully') 
        time.sleep(1)
        actionComplete = self.scaleImage(imgSize) if actionComplete else self.log.writeError('Image was not scaled successfully') 
        time.sleep(1)
        actionComplete = self.offsetImage(position) if actionComplete else self.log.writeError('Image was not offset successfully') 
        return actionComplete

    def changeHeaderText(self, newText):
        section = self.SegmentedData.headlineTextData

        areaSelected = self.clickIcon(section['layerIconData'])
        if areaSelected:
            time.sleep(0.2)
            areaSelected = self.clickIcon(section['editTextData'])
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.write(newText)
            time.sleep(0.2)
            pyautogui.press('esc')
        return areaSelected

    def changeBackgroundColor(self, newColor):
        section = self.SegmentedData.backgroundColorData

        areaSelected = self.clickIcon(section['layerIconData'])
        if areaSelected:
            backgroundToolPosition = self.storePosition(section['backgroundColorToolData'])
            areaSelected = self.clickIcon(section['backgroundColorToolData'])
        if areaSelected:
            areaSelected = self.clickIcon(section['textCodeIconData'])
            pyautogui.write(newColor)
        if areaSelected:
            areaSelected = self.clickIcon(section['okButtonBackgroundColorData'])
            pyautogui.press('enter')
            time.sleep(0.5)
        if areaSelected:
            pyautogui.hotkey('shift', 'b')
            areaSelected = self.clickIcon(section['pictureBackgroundColorData'])

        if areaSelected:
            pos = backgroundToolPosition
            print(pos)
            pyautogui.click(pos[0]+2, pos[1]+2)
            areaSelected = self.clickIcon(section['textCodeIconData'])
            pyautogui.write(self.themeColor)
            time.sleep(0.2)
            if areaSelected:
                areaSelected = self.clickIcon(section['okButtonBackgroundColorData'])
                pyautogui.press('enter')
                time.sleep(0.5)

        return areaSelected

    def saveEditedFile(self):
        pyautogui.hotkey('ctrl', 'shift', 's')
        self.saveImage();
        pyautogui.hotkey('ctrl', 'shift', 'e')
        time.sleep(0.3)
        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(4)
        pyautogui.press('enter')        

    ############################################
    # General Functions
    ############################################
    def openTemplate(self):
        iconDirectory = self.SegmentedData.openTemplateData['openTemplateData']
        pyautogui.hotkey('ctrl', 'o')
        time.sleep(0.2)
        print(iconDirectory)
        confidence = self.itemInfo["confidence"]

        for index, item in enumerate(iconDirectory):
            if (index) == 0:
                itemPosition = pyautogui.locateOnScreen(item, grayscale=True, confidence=confidence)
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':0, 'offsetY':0})
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':200, 'offsetY':0})
            else:
                pyautogui.write(item)
                pyautogui.press('enter')
                time.sleep(0.1)
        return areaSelected


    def deleteImage(self):
        section = self.SegmentedData.deleteImageData

        areaSelected = self.clickIcon(section['layerIconData'])
        if areaSelected: areaSelected = self.clickIcon(section['deleteLayerData'])
        return areaSelected


    def openImage(self):
        iconDirectory = self.SegmentedData.openImageData['openImageData']
        pyautogui.hotkey('ctrl', 'alt', 'o')
        time.sleep(0.2)
        print(iconDirectory)
        confidence = self.itemInfo["confidence"]

        for index, item in enumerate(iconDirectory):
            if (index) == 0:
                itemPosition = pyautogui.locateOnScreen(item, grayscale=True, confidence=confidence)
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':0, 'offsetY':0})
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':200, 'offsetY':0})
                time.sleep(0.5)
            else:
                pyautogui.write(item)
                time.sleep(0.5)
                pyautogui.press('enter')
                time.sleep(0.5)
        return areaSelected


    def saveImage(self):
        iconDirectory = self.SegmentedData.saveImageData['saveImageData']
        time.sleep(0.2)
        confidence = self.itemInfo["confidence"]

        for index, item in enumerate(iconDirectory):
            if (index) == 0:
                pyautogui.write(item)
                time.sleep(0.1)
            elif (index) == 1:
                itemPosition = pyautogui.locateOnScreen(item, grayscale=True, confidence=confidence)
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':0, 'offsetY':0})
                areaSelected = clickImage(itemPosition, data={'sleepTime':0.3, 'clicks':2, 'offsetX':200, 'offsetY':0})             
            else:
                pyautogui.write(item)
                pyautogui.press('enter')
                time.sleep(0.1)

        pyautogui.press('enter')
        pyautogui.press('enter')
        time.sleep(0.5)

        return areaSelected


    def scaleImage(self, width=None):
        if width is not None:
            section = self.SegmentedData.scaleImageData

            areaSelected = self.clickIcon(section['layerIconData'])
            if areaSelected:
                areaSelected = self.clickIcon(section['scaleLayerStartData'])
                pyautogui.write(str(width))
            if areaSelected: areaSelected = self.clickIcon(section['scaleLayerScaleButtonData'])
            return areaSelected


    def offsetImage(self, position):
        section = self.SegmentedData.offsetImageData
        areaSelected = self.clickIcon(section['layerIconData'])

        if areaSelected: areaSelected = self.clickIcon(section['editLayerStartData'])
        if areaSelected: 
            areaSelected = self.clickIcon(section['offsetXButtonData'])
            pyautogui.write(str(position[0]))
        if areaSelected:
            areaSelected = self.clickIcon(section['offsetYButtonData'])
            pyautogui.write(str(position[1]))
        if areaSelected:
            areaSelected = self.clickIcon(section['editLayerCompleteData'])
            pyautogui.press('enter')
        return areaSelected


    ############################################
    # Component Functions
    ############################################
    def clickIcon(self, section):
        self.SegmentedData.updatePosition(section)
        return self.selectArea(data=section)


    def selectArea(self, data):
        return self.callAction(data)

    def callAction(self, data):
        if data['position']:
            pyautogui.moveTo(data['position'][0], data['position'][1])
            time.sleep(0.2)
        return data['action'](data['position'], data['clickParams'])

    def gimpLocateOnScreen(self, data):
        pyautogui.locateOnScreen(icon, grayscale=True, confidence=gimpBot.confidence, region=layerRegion)

    def storePosition(self, section):
        self.SegmentedData.updatePosition(section)
        return [section['position'][0], section['position'][1]]
        
'''


'''
        icon = self.icons["templates"][self.template]["layer_menu"]["header_img"]["logo"]
        layerRegion = self.regions["layer_menu"]
        layerData = {
            'icon': icon,
            'position': pyautogui.locateOnScreen(icon, grayscale=True, confidence=self.confidence, region=layerRegion),
            'action': clickImage
        }




    # checkStatus Helper Functions
    def checkSpecialization(self):
        if pyautogui.locateOnScreen('images/specialization.png')is not None: # Check if specialization screen is active
            self.addSpecialization()

    def checkAutoRun(self):
        autoButton = pyautogui.locateOnScreen('images/stopAutoProgress.png')
        if autoButton is not None:
            self.clickItem(autoButton)

    def useSpecials(self):
        pyautogui.typewrite('123456789')


    # checkSpecialization Helper Function
    # Temp solution: Need to add process for understanding/selecting upgrades depending on different people
    def addSpecialization(self):
        buttons = list(pyautogui.locateAllOnScreen('images/selectSpecialization.png'))
        self.clickItem(buttons[0])

    def tempUpgrade(self):
        if pyautogui.locateOnScreen('images/specialization.png', region=(520, 80, 325, 72) is not None:
            print("Specialization Title Fund")
            if pyautogui.locateOnScreen('images/troops/Celeste.png', region=(755, 230, 165, 30) is not None:
                print("Specific person found")
            
    
    # General Helper Functions
    def clickItem(self, button):
        cordX, cordY = pyautogui.center(button)
        pyautogui.click(cordX, cordY)
'''
