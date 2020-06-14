import sys
sys.path.insert(1,"src")
import time
from datetime import datetime
import shutil
from coordinates import client,game,clientCoords,gameCoords,computerWidth,computerHeight
import cv2 as cv
import numpy as np
from directInputController import setPos,click,rightClick,getPixel,pressKey,holdKey,releaseKey
from windowcapture import WindowCapture
from directInputController import keyboardButton
import random

def log(x):
    print(datetime.now().strftime("%H:%M:%S -"),x)
def changeSettings():
    shutil.copyfile("src\\settings\\changeSettings\\game.cfg","C:\\Riot Games\\League of Legends\\Config\\game.cfg")
    shutil.copyfile("src\\settings\\changeSettings\\PersistedSettings.json","C:\\Riot Games\\League of Legends\\Config\\PersistedSettings.json")
def changeSettingsBack():
    shutil.copyfile("src\\settings\\changeSettingsBack\\game.cfg","C:\\Riot Games\\League of Legends\\Config\\game.cfg")
    shutil.copyfile("src\\settings\\changeSettingsBack\\PersistedSettings.json","C:\\Riot Games\\League of Legends\\Config\\PersistedSettings.json")
def name(img):
    return "src\\images\\"+img+".PNG"
def locate(img,screenshot,threshold=0.9):
    img=name(img)
    img=cv.imread(img)
    img=img[...,:3]
    img=np.ascontiguousarray(img)
    result=cv.matchTemplate(screenshot,img,cv.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    if(max_val>=threshold):
        max_loc=(max_loc[0]+clientCoords[0],max_loc[1]+clientCoords[1])
        return max_loc
    else:
        return None
def locateGame(img,screenshot,lower_range=np.array([0,0,0]),upper_range=np.array([255,255,255]),threshold=0.9):
    img=name(img)
    img=cv.imread(img)
    img=img[...,:3]
    img=np.ascontiguousarray(img)

    img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    img=cv.inRange(img,lower_range,upper_range)
    background=cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
    background=cv.inRange(background,lower_range,upper_range)

    result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
    min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
    if(max_val>=threshold):
        max_loc=(max_loc[0]+gameCoords[0],max_loc[1]+gameCoords[1])
        return max_loc
    else:
        return None
def chooseChamp():
    log("Calling lane...")
    click(client.chatButton)
    time.sleep(0.5)
    pressKey(keyboardButton.M)
    pressKey(keyboardButton.I)
    pressKey(keyboardButton.D)
    pressKey(keyboardButton.Enter)
    time.sleep(0.5)
    log("Choosing champion...")
    for x in range(755-448,1166-448,82):
        for y in range(430-294,731-294,75):
            click((x+clientCoords[0],y+clientCoords[1]))
            time.sleep(0.2)
    time.sleep(1)
    click(client.searchButton)
    time.sleep(0.5)
    pressKey(keyboardButton.S)
    pressKey(keyboardButton.I)
    pressKey(keyboardButton.V)
    pressKey(keyboardButton.I)
    pressKey(keyboardButton.R)
    time.sleep(1)
    click(client.champButton)
    time.sleep(1)
    click(client.lockInButton)
    time.sleep(1)
def startBuy():
    log("Buying starter items...")
    pressKey(keyboardButton.P)
    time.sleep(1)
    rightClick(game.potion)
    time.sleep(0.2)
    rightClick(game.dBlade)
    time.sleep(0.2)
    time.sleep(1)
    pressKey(keyboardButton.Escape)
    time.sleep(5)
def buyItems():
    log("Buying items...")
    pressKey(keyboardButton.P)
    time.sleep(1)
    rightClick(game.potion)
    time.sleep(0.2)
    rightClick(game.item1)
    time.sleep(0.2)
    rightClick(game.item2)
    time.sleep(0.2)
    rightClick(game.item3)
    time.sleep(0.2)
    rightClick(game.item4)
    time.sleep(0.2)
    rightClick(game.item5)
    time.sleep(0.2)
    rightClick(game.item6)
    time.sleep(0.2)
    rightClick(game.item7)
    time.sleep(0.2)
    rightClick(game.item8)
    time.sleep(0.2)
    rightClick(game.item9)
    time.sleep(0.2)
    time.sleep(1)
    pressKey(keyboardButton.Escape)
    time.sleep(5)
def a():
    log("Changing League of Legends settings...")
    changeSettings()
    log("Getting into Lobby...")
    click(client.playButton)
    time.sleep(2)
    click(client.coopButton)
    time.sleep(2)
    click(client.beginnerButton)
    time.sleep(2)
    click(client.confirmButton)
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
                log("Finding a match...")
                click(client.findMatchButton)
            if(locate("acceptButton",screenshot)!=None):
                log("Waiting for champ select...")
                click(client.acceptButton)
        if(locate("chooseChampion",screenshot)!=None):
            chooseChamp()
    log("Waiting for game window...")
    time.sleep(15)
def c():
    log("Game window found.")
    wincap=WindowCapture('League of Legends (TM) Client')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("minimap",screenshot)!=None):
            log("Game started.")
            break
        else:
            log("Waiting for game to start...")
            click((computerWidth/2,computerHeight/2))
def d():
    rightClick((computerWidth/2,computerHeight/2))
    time.sleep(1)
    q=False
    w=False
    e=False
    startBuy()
    time.sleep(1)
    log("Locking screen...")
    pressKey(keyboardButton.n0)
    wincap=WindowCapture('League of Legends (TM) Client')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        
        if(getPixel(game.recallButton)==(80, 187, 238)):
            #checking health
            if(getPixel(game.healthBar)==(1,12,7)):
                rightClick(game.base)
                rightClick(game.base)
                pressKey(keyboardButton.D)
                pressKey(keyboardButton.F)
                pressKey(keyboardButton.n1)
                flag=True
                for i in range(8):
                    flag=getPixel(game.healthBar)==(1,12,7)
                    rightClick(game.base)
                    time.sleep(1)
                    if(flag==False):
                        break
                if flag:
                    pressKey(keyboardButton.B)
                    flag2=True
                    for i in range(9):
                        flag2=getPixel(game.healthBar)==(1,12,7)
                        time.sleep(1)
                        if(flag2==False):
                            break
                    if flag2:
                        buyItems()
                        pressKey(keyboardButton.n4)
            else:
                max_loc=locateGame("casterMinion",screenshot,np.array([111,167,81]),np.array([121,215,130]),0.5)
                if(max_loc!=None):
                    setPos(max_loc)  
                    pressKey(keyboardButton.Space)
                    #finding champ
                    maxChamp_loc=locateGame("champHealth",screenshot,np.array([2,204,165]),np.array([4,204,166]),0.5)
                    #checking tower range
                    max_loc=locateGame("tower",screenshot,np.array([49,0,135]),np.array([100,40,166]),0.5)
                    #checking if theres a enemy champion
                    if(maxChamp_loc!=None):
                        #checking if you are not in tower range
                        if(max_loc==None):
                            pressKey(keyboardButton.T)
                            maxChamp_loc=(maxChamp_loc[0]+50,maxChamp_loc[1]+75)
                            setPos(maxChamp_loc)
                            pressKey(keyboardButton.E)
                            pressKey(keyboardButton.R)
                            pressKey(keyboardButton.Q)
                            pressKey(keyboardButton.W)
                            pressKey(keyboardButton.Space)
                            pressKey(keyboardButton.T)
                            time.sleep(0.5)
                    else:
                        pressKey(keyboardButton.W)
                else:
                    x=random.randint(-25,25)
                    rightClick((game.tower[0]+x,game.tower[1]-x))
                    
                #levelling up
                if(locate("levelUpButton",screenshot)!=None):
                    holdKey(keyboardButton.Lctrl)
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
                    pressKey(keyboardButton.E)
                    releaseKey(keyboardButton.Lctrl)
        else:
            buyItems()
    log("Game has ended.")
def e():
    log("Waiting for client...")
    time.sleep(30)
    wincap = WindowCapture('League of Legends')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("playButton",screenshot)!=None):
            log("Restarting.")
            break
        if(locate("honor",screenshot)!=None):
            log("Honoring teammate...")
            click(client.honorButton)
            time.sleep(1)
        if(locate("dailyPlay",screenshot,0.8)!=None):
            log("Choosing reward...")
            click(client.dailyPlayButton)
            time.sleep(1)
        if(locate("okButton",screenshot,0.8)!=None):
            log("Choosing reward...")
            click(locate("okButton",screenshot,0.8))
            time.sleep(1)
        if(locate("xButton",screenshot,0.8)!=None):
            log("Exiting lobby...")
            click(locate("xButton",screenshot,0.8))
            time.sleep(1)
def main():
    for i in range(5,0,-1):
        log("Starting in "+str(i))
        time.sleep(1)
    log("Starting in 0")

    startTime=time.time()
    while True:
        a()
        b()
        c()
        d()
        e()
        if(time.time()-startTime>=(12*60*60)):
            log("Taking a random break...")
            time.sleep((random.randint(15,45)*60))
            startTime=time.time()
main()
