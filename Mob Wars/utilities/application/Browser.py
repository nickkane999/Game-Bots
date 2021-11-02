from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
import time
import os
import glob
import shutil
from time import sleep
import json

# from commonFunctions import *
# from SegmentedData import *


class Browser:
    # Initializing Object
    def __init__(self, instructions):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.instructions = instructions
        self.url = self.getURL()

    def start(self):
        driver = self.driver
        driver.get(self.url)

    def load(self, url):
        driver = self.driver
        self.url = url
        driver.get(url)

    def pullHTML(self):
        driver = self.driver
        html = driver.page_source
        self.text = html
        return html

    def getURL(self):
        url = self.instructions["url"]
        if url:
            return url
        else:
            print("No url provided, exiting the program")
            sys.exit()

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
