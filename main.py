import sys
sys.path.insert(1,"src")
import pyautogui
import time
import shutil
import random
import coordinates
import cv2 as cv
import numpy as np
import directInputController
from windowcapture import WindowCapture
from directInputController import keyboardButton

def changeSettings():
    shutil.copyfile("src\\settings\\new\\game.cfg","D:\\Riot Games\\League of Legends\\Config\\game.cfg")
    shutil.copyfile("src\\settings\\new\\PersistedSettings.json","D:\\Riot Games\\League of Legends\\Config\\PersistedSettings.json")
def changeSettingsBack():
    shutil.copyfile("src\\settings\\old\\game.cfg","D:\\Riot Games\\League of Legends\\Config\\game.cfg")
    shutil.copyfile("src\\settings\\old\\PersistedSettings.json","D:\\Riot Games\\League of Legends\\Config\\PersistedSettings.json")
def name(img):
    return "src\\images\\"+img+".PNG"
def locate(img,screenshot,threshold=0.9):
    img=name(img)
    img=cv.imread(img,cv.IMREAD_UNCHANGED)
    img=img[...,:3]
    img=np.ascontiguousarray(img)
    result=cv.matchTemplate(screenshot,img,cv.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    if(max_val>=threshold):
        max_loc=(max_loc[0]+coordinates.clientCoords[0],max_loc[1]+coordinates.clientCoords[1])
        return max_loc
    else:
        return None
def click(location):
    directInputController.set_pos(location[0],location[1])
    directInputController.left_click()
def rightClick(location):
    directInputController.set_pos(location[0],location[1])
    directInputController.right_click()
def pressKey(key):
    directInputController.press_key(key)
    time.sleep(0.05)
    directInputController.release_key(key)

def changeCoords(coordinate,screen):
    if(screen=="client"):
        return (coordinate[0]+coordinates.clientCoords[0],coordinate[1]+coordinates.clientCoords[1])
    elif(screen=="game"):
        return (coordinate[0]+coordinates.gameCoords[0],coordinate[1]+coordinates.gameCoords[1])
def chooseChamp():
    for x in range(755-448,1166-448,82):
        for y in range(430-294,731-294,75):
            click(changeCoords((x,y),"client"))
            time.sleep(0.2)
    time.sleep(1)
def buyItems():
    pressKey(keyboardButton.P)
    time.sleep(1)
    rightClick(changeCoords(coordinates.game.item1,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item2,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item3,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item4,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item5,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item6,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item7,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item8,"game"))
    time.sleep(0.2)
    rightClick(changeCoords(coordinates.game.item9,"game"))
    time.sleep(1)
    pressKey(keyboardButton.Escape)
def a():
    changeSettings()
    click(changeCoords(coordinates.client.playButton,"client"))
    time.sleep(2)
    click(changeCoords(coordinates.client.coopButton,"client"))
    time.sleep(2)
    click(changeCoords(coordinates.client.beginnerButton,"client"))
    time.sleep(2)
    click(changeCoords(coordinates.client.confirmButton,"client"))
    time.sleep(2)
    time.sleep(1)
def b():
    wincap = WindowCapture('League of Legends')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("grayLockInButton",screenshot)==None):
            if(locate("findMatchButton",screenshot)!=None):
                click(changeCoords(coordinates.client.findMatchButton,"client"))
            if(locate("acceptButton",screenshot)!=None):
                click(changeCoords(coordinates.client.acceptButton,"client"))
        if(locate("chooseChampion",screenshot)!=None):
            chooseChamp()
            click(changeCoords(coordinates.client.searchButton,"client"))
            time.sleep(0.5)
            pyautogui.typewrite("sivir")
            time.sleep(1)
            click(changeCoords(coordinates.client.champButton,"client"))
            time.sleep(1)
            click(changeCoords(coordinates.client.lockInButton,"client"))
            time.sleep(1)
def c():
    while(pyautogui.locateCenterOnScreen(name("minimap"))==None):
        time.sleep(0.1)
    print("Now in game")
    rightClick ((coordinates.computerWidth/2,coordinates.computerHeight/2))
    time.sleep(1)
    wincap=WindowCapture('League of Legends (TM) Client')
    q=False
    w=False
    e=False
    pressKey(keyboardButton.Y)
    buyItems()
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        
        if(locate("recallButton",screenshot)==None):
            #checking health
            if(pyautogui.pixelMatchesColor(950,955,(1,13,7))):
                rightClick(changeCoords(coordinates.game.base,"game"))
                rightClick(changeCoords(coordinates.game.base,"game"))
                pressKey(keyboardButton.D)
                pressKey(keyboardButton.F)
                rightClick(changeCoords(coordinates.game.base,"game"))
                rightClick(changeCoords(coordinates.game.base,"game"))
                time.sleep(8)
                pressKey(keyboardButton.B)
                time.sleep(9)
                buyItems()
            else:
                #finding casters
                lower_range=np.array([98,155,167])
                upper_range=np.array([102,165,237])
                img=name("casterMinion")
                img=cv.imread(img,cv.IMREAD_UNCHANGED)
                img=img[...,:3]
                img=np.ascontiguousarray(img)
                img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                img=cv.inRange(img,lower_range,upper_range)
                background=cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
                background=cv.inRange(background,lower_range,upper_range)
                result=cv.matchTemplate(background,img,cv.TM_CCORR)
                min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
                if(max_val>=260000):
                    pyautogui.moveTo(changeCoords(max_loc,"game"))  
                    pressKey(keyboardButton.Space)
                else:
                    rightClick(changeCoords(coordinates.game.tower,"game"))
                
                #finding champ
                lower_range=np.array([0,132,144])
                upper_range=np.array([5,192,255])
                img=name("champion")
                img=cv.imread(img,cv.IMREAD_UNCHANGED)
                img=img[...,:3]
                img=np.ascontiguousarray(img)
                background=screenshot
                img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                background=cv.cvtColor(background,cv.COLOR_BGR2HSV)
                img=cv.inRange(img,lower_range,upper_range)
                background=cv.inRange(background,lower_range,upper_range)
                result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
                min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
                if(max_val>=0.6):
                    #checking tower range
                    lower_range=np.array([49,0,135])
                    upper_range=np.array([100,40,166])
                    img=name("tower")
                    img=cv.imread(img,cv.IMREAD_UNCHANGED)
                    img=img[...,:3]
                    img=np.ascontiguousarray(img)
                    background=screenshot
                    img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                    background=cv.cvtColor(background,cv.COLOR_BGR2HSV)
                    img=cv.inRange(img,lower_range,upper_range)
                    background=cv.inRange(background,lower_range,upper_range)
                    result=cv.matchTemplate(background,img,cv.TM_SQDIFF)
                    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
                    if(max_val>=30000000.0):
                        pressKey(keyboardButton.T)
                        max_loc=(max_loc[0]+50,max_loc[1]+75)
                        pyautogui.moveTo(changeCoords(max_loc,"game"))
                        pressKey(keyboardButton.E)
                        pressKey(keyboardButton.R)
                        pressKey(keyboardButton.Q)
                        pressKey(keyboardButton.W)
                        pressKey(keyboardButton.Space)
                        pressKey(keyboardButton.T)
                        time.sleep(0.5)
                elif(max_val>=0.4):            
                    pressKey(keyboardButton.W)
                
                #levelling up
                if(locate("levelUpButton",screenshot)!=None):
                    directInputController.press_key(keyboardButton.Lctrl)
                    time.sleep(0.05)
                    pressKey(keyboardButton.R)
                    if(q==False):
                        pressKey(keyboardButton.Q)
                        q=True
                    elif(w==False):
                        pressKey(keyboardButton.W)
                        w=True
                    elif(e==False):
                        pressKey(keyboardButton.E)
                        e=True
                    pressKey(keyboardButton.Q)
                    pressKey(keyboardButton.W)
                    pressKey(keyboardButton.E )
                    directInputController.release_key(keyboardButton.Lctrl)
        else:
            buyItems()
def d():
    wincap = WindowCapture('League of Legends')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("playButton",screenshot)!=None):
            break
        if(locate("okButton",screenshot,0.8)!=None):
            pyautogui.click(locate("okButton",screenshot,0.8))
        if(locate("xButton",screenshot,0.8)!=None):
            pyautogui.click(locate("xButton",screenshot,0.8))
# def nothing(x):
#     pass
# cv.namedWindow("Tracking")
# cv.createTrackbar("LH","Tracking",0,255,nothing)
# cv.createTrackbar("LS","Tracking",0,255,nothing)
# cv.createTrackbar("LV","Tracking",0,255,nothing)
# cv.createTrackbar("UH","Tracking",255,255,nothing)
# cv.createTrackbar("US","Tracking",255,255,nothing)
# cv.createTrackbar("UV","Tracking",255,255,nothing)
# def e():
    # lh=cv.getTrackbarPos("LH","Tracking")
    # ls=cv.getTrackbarPos("LS","Tracking")
    # lv=cv.getTrackbarPos("LV","Tracking")
    # uh=cv.getTrackbarPos("UH","Tracking")
    # us=cv.getTrackbarPos("US","Tracking")
    # uv=cv.getTrackbarPos("UV","Tracking")
    # while True:
    #     wincap=WindowCapture('League of Legends (TM) Client')
    #     try:
    #         screenshot = wincap.get_screenshot()
    #     except:
    #         break
    #     lower_range=np.array([49,0,135])
    #     upper_range=np.array([100,40,166])
    #     img=name("tower")
    #     img=cv.imread(img,cv.IMREAD_UNCHANGED)
    #     img=img[...,:3]
    #     img=np.ascontiguousarray(img)
    #     test=name("test4")
    #     test=cv.imread(test,cv.IMREAD_UNCHANGED)
    #     test=test[...,:3]
    #     test=np.ascontiguousarray(test)

    #     test=screenshot

    #     img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    #     test=cv.cvtColor(test,cv.COLOR_BGR2HSV)
    #     img=cv.inRange(img,lower_range,upper_range)
    #     test=cv.inRange(test,lower_range,upper_range)

    #     result=cv.matchTemplate(test,img,cv.TM_SQDIFF)
    #     min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    #     if(max_val>=30000000.0):
    #         print(max_loc,max_val)
            
    #     result=cv.bitwise_and(test,test,result)
    #     cv.rectangle(result,max_loc,(max_loc[0]+50,max_loc[1]+200),color=(223,82,134),thickness=2)

    #     cv.imshow("result",result)
    #     cv.waitKey(1)#40000000.0
def main():
    while True:
        a()
        b()
        c()
        time.sleep(60)
        d()

main()
 