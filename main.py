import sys
sys.path.insert(1,"src")
import time
import shutil
from coordinates import client,game,clientCoords,gameCoords,computerWidth,computerHeight
import cv2 as cv
import numpy as np
from directInputController import setPos,click,rightClick,getPixel,pressKey,holdKey,releaseKey
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
    click(client.chatButton)
    time.sleep(0.5)
    pressKey(keyboardButton.M)
    pressKey(keyboardButton.I)
    pressKey(keyboardButton.D)
    pressKey(keyboardButton.Enter)
    time.sleep(0.5)
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
def buyItems():
    pressKey(keyboardButton.P)
    time.sleep(1)
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
    time.sleep(1)
    pressKey(keyboardButton.Escape)
    time.sleep(5)
def a():
    changeSettings()
    click(client.playButton)
    time.sleep(2)
    click(client.coopButton)
    time.sleep(2)
    click(client.intermediateButton)
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
                click(client.findMatchButton)
            if(locate("acceptButton",screenshot)!=None):
                click(client.acceptButton)
        if(locate("chooseChampion",screenshot)!=None):
            chooseChamp()
    time.sleep(5)
def c():
    wincap=WindowCapture('League of Legends (TM) Client')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("minimap",screenshot)!=None):
            break
def d():
    print("Now in game")
    rightClick((computerWidth/2,computerHeight/2))
    time.sleep(1)
    q=False
    w=False
    e=False
    pressKey(keyboardButton.Y)
    buyItems()
    wincap=WindowCapture('League of Legends (TM) Client')
    looptime=time.time()
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        
        if(getPixel(game.recallButton)!=(64, 85, 95)):
            #checking health
            if(getPixel(game.healthBar)==(1,13,7)):
                rightClick(game.base)
                rightClick(game.base)
                pressKey(keyboardButton.D)
                pressKey(keyboardButton.F)
                x=0
                flag=True
                for i in range(8):
                    flag=getPixel(game.healthBar)==(1,13,7)
                    rightClick(game.base)
                    time.sleep(1)
                    if(flag==False):
                        break
                if flag:
                    pressKey(keyboardButton.B)
                    time.sleep(9)
                    buyItems()
            else:
                #finding casters
                # lower_range=np.array([111,167,81])
                # upper_range=np.array([121,215,130])
                # img=name("casterMinion")
                # img=cv.imread(img)
                # img=img[...,:3]
                # img=np.ascontiguousarray(img)
                # img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                # img=cv.inRange(img,lower_range,upper_range)
                # background=cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
                # background=cv.inRange(background,lower_range,upper_range)
                # result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
                max_loc=locateGame("casterMinion",screenshot,np.array([111,167,81]),np.array([121,215,130]),0.5)
                if(max_loc!=None):
                    setPos(max_loc)  
                    pressKey(keyboardButton.Space)
                else:
                    rightClick(game.tower)

                #finding champ
                lower_range=np.array([2,204,165])
                upper_range=np.array([4,204,166])
                img=name("champHealth")
                img=cv.imread(img)
                img=img[...,:3]
                img=np.ascontiguousarray(img)
                img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                img=cv.inRange(img,lower_range,upper_range)
                background=cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
                background=cv.inRange(background,lower_range,upper_range)
                result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
                minChamp_val,maxChamp_val,minChamp_loc,maxChamp_loc=cv.minMaxLoc(result)

                #checking tower range
                lower_range=np.array([49,0,135])
                upper_range=np.array([100,40,166])
                img=name("tower")
                img=cv.imread(img)
                img=img[...,:3]
                img=np.ascontiguousarray(img)
                img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
                img=cv.inRange(img,lower_range,upper_range)
                background=cv.cvtColor(screenshot,cv.COLOR_BGR2HSV)
                background=cv.inRange(background,lower_range,upper_range)
                result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
                min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
                
                #checking if theres a enemy champion
                if(maxChamp_val>=0.5):
                    #checking if you are not in tower range
                    if(max_val<=0.5):
                        pressKey(keyboardButton.T)
                        maxChamp_loc=(maxChamp_loc[0]+gameCoords[0]+50,maxChamp_loc[1]+gameCoords[1]+75)
                        setPos(maxChamp_loc)
                        pressKey(keyboardButton.E)
                        pressKey(keyboardButton.R)
                        pressKey(keyboardButton.Q)
                        pressKey(keyboardButton.W)
                        pressKey(keyboardButton.Space)
                        pressKey(keyboardButton.T)
                else:
                    pressKey(keyboardButton.W)
                    
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
                    pressKey(keyboardButton.E )
                    releaseKey(keyboardButton.Lctrl)
        else:
            buyItems()
        print("fps:",(1/(time.time()-looptime)))
        looptime=time.time()
def e():
    time.sleep(20)
    wincap = WindowCapture('League of Legends')
    while(True):
        try:
            screenshot = wincap.get_screenshot()
        except:
            break
        if(locate("playButton",screenshot)!=None):
            break
        if(locate("honor",screenshot)!=None):
            click(client.honorButton)
        if(locate("dailyPlay",screenshot,0.8)!=None):
            click(client.dailyPlayButton)
        if(locate("okButton",screenshot,0.8)!=None):
            click(locate("okButton",screenshot,0.8))
        if(locate("xButton",screenshot,0.8)!=None):
            click(locate("xButton",screenshot,0.8))
# # def nothing(x):
# #     pass
# # cv.namedWindow("Tracking")
# # cv.createTrackbar("LH","Tracking",0,255,nothing)
# # cv.createTrackbar("LS","Tracking",0,255,nothing)
# # cv.createTrackbar("LV","Tracking",0,255,nothing)
# # cv.createTrackbar("UH","Tracking",255,255,nothing)
# # cv.createTrackbar("US","Tracking",255,255,nothing)
# # cv.createTrackbar("UV","Tracking",255,255,nothing)
# def f():
# #     lh=cv.getTrackbarPos("LH","Tracking")
# #     ls=cv.getTrackbarPos("LS","Tracking")
# #     lv=cv.getTrackbarPos("LV","Tracking")
# #     uh=cv.getTrackbarPos("UH","Tracking")
# #     us=cv.getTrackbarPos("US","Tracking")
# #     uv=cv.getTrackbarPos("UV","Tracking")

#     looptime=time.time()
#     while True:
#         wincap=WindowCapture('League of Legends (TM) Client')
#         try:
#             screenshot = wincap.get_screenshot()
#         except:
#             break
#         # lower_range=np.array([lh,ls,lv])
#         # upper_range=np.array([uh,us,uv])
#         lower_range=np.array([49,0,135])
#         upper_range=np.array([100,40,166])
#         img=name("tower")
#         img=cv.imread(img)
#         img=img[...,:3]
#         img=np.ascontiguousarray(img)
#         img=cv.cvtColor(img,cv.COLOR_BGR2HSV)
#         img=cv.inRange(img,lower_range,upper_range)

#         background=name("test")
#         background=cv.imread(background)
#         background=background[...,:3]
#         background=np.ascontiguousarray(background) 
#         background=screenshot
#         background=cv.cvtColor(background,cv.COLOR_BGR2HSV)
#         background=cv.inRange(background,lower_range,upper_range)
        


#         result=cv.matchTemplate(background,img,cv.TM_CCOEFF_NORMED)
#         min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)

#         print(max_val)
        
#         result=cv.bitwise_and(background,background,result)
#         cv.rectangle(result,max_loc,(max_loc[0]+50,max_loc[1]+50),color=(255,255,255),thickness=2)

#         cv.imshow("result",result)
#         cv.waitKey(1)
#         #4,161,600 ->
#         # print("fps",(1/(time.time()-looptime)))
#         # looptime=time.time()
def main():
    while True:
        a()
        b()
        c()
        d()
        e()

d()