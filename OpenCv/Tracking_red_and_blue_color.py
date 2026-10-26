import cv2
import time
import numpy as np

def myCallBack1(val):
    global LowHuered
    print("Low Hue = ",val)
    LowHuered = val
def myCallBack2(val):
    global HighHuered
    print("High Hue = ",val)
    HighHuered = val
def myCallBack3(val):
    global LowSatred
    print("Low Sat = ",val)
    LowSatred = val
def myCallBack4(val):
    global HighSatred
    print("High Sat = ",val)
    HighSatred = val
def myCallBack5(val):
    global LowValred
    print("Low Val = ",val)
    LowValred = val
def myCallBack6(val):
    global HighValred
    print("High Val = ",val)
    HighValred = val

def myCallBack7(val):
    global LowHueblue
    print("Low Hue = ",val)
    LowHueblue = val
def myCallBack8(val):
    global HighHueblue
    print("High Hue = ",val)
    HighHueblue = val
def myCallBack9(val):
    global LowSatblue
    print("Low Sat = ",val)
    LowSatblue = val
def myCallBack10(val):
    global HighSatblue
    print("High Sat = ",val)
    HighSatblue = val
def myCallBack11(val):
    global LowValblue
    print("Low Val = ",val)
    LowValblue = val
def myCallBack12(val):
    global HighValblue
    print("High Val = ",val)
    HighValblue = val


print(cv2.__version__)
width = 640
height = 360

LowHuered  = 10
HighHuered = 20
LowSatred  = 10
HighSatred = 250
LowValred  = 10
HighValred = 250
LowHueblue  = 10
HighHueblue = 20
LowSatblue  = 10
HighSatblue = 250
LowValblue  = 10
HighValblue = 250
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
cv2.namedWindow("myTrackbars red")
cv2.resizeWindow("myTrackbars red",400,240)
cv2.moveWindow("myTrackbars red",0,550)
cv2.createTrackbar("Low Hue", "myTrackbars red",LowHuered,180,myCallBack1)
cv2.createTrackbar("High Hue", "myTrackbars red",HighHuered,180,myCallBack2)
cv2.createTrackbar("Low Sat", "myTrackbars red",LowSatred,255,myCallBack3)
cv2.createTrackbar("High Sat", "myTrackbars red",HighSatred,255,myCallBack4)
cv2.createTrackbar("Low Val", "myTrackbars red",LowValred,255,myCallBack5)
cv2.createTrackbar("High Val", "myTrackbars red",HighValred,255,myCallBack6)
cv2.namedWindow("myTrackbars1")
cv2.resizeWindow("myTrackbars1",400,240)
cv2.moveWindow("myTrackbars1",width,550)
cv2.createTrackbar("Low Hue", "myTrackbars1",LowHueblue,180,myCallBack7)
cv2.createTrackbar("High Hue", "myTrackbars1",HighHueblue,180,myCallBack8)
cv2.createTrackbar("Low Sat", "myTrackbars1",LowSatblue,255,myCallBack9)
cv2.createTrackbar("High Sat", "myTrackbars1",HighSatblue,255,myCallBack10)
cv2.createTrackbar("Low Val", "myTrackbars1",LowValblue,255,myCallBack11)
cv2.createTrackbar("High Val", "myTrackbars1",HighValblue,255,myCallBack12)
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    frameHSVred = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBoundred = np.array([LowHuered,LowSatred,LowValred])
    upperBoundred = np.array([HighHuered,HighSatred,HighValred])
    myMaskred = cv2.inRange(frameHSVred,lowerBoundred,upperBoundred)
    mysmallMaskred = cv2.resize(myMaskred,(int(width/2),int(height/2)))
    # myMaskred = cv2.bitwise_not(myMaskred)
    myObjectred = cv2.bitwise_and(frame,frame,mask=myMaskred)
    mysmallObjectred = cv2.resize(myObjectred,(int(width/2),int(height/2)))
    cv2.imshow("My MASK red",mysmallMaskred)
    cv2.moveWindow('My MASK red',0,height)
    cv2.imshow("My Object red",mysmallObjectred)
    cv2.moveWindow('My Object red',int(width/2),height)

    frameHSVblue = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBoundblue = np.array([LowHueblue,LowSatblue,LowValblue])
    upperBoundblue = np.array([HighHueblue,HighSatblue,HighValblue])
    myMaskblue = cv2.inRange(frameHSVblue,lowerBoundblue,upperBoundblue)
    mysmallMaskblue = cv2.resize(myMaskblue,(int(width/2),int(height/2)))
    myObjectblue = cv2.bitwise_and(frame,frame,mask=myMaskblue)
    mysmallObjectblue = cv2.resize(myObjectblue,(int(width/2),int(height/2)))
    cv2.imshow("My MASK blue",mysmallMaskblue)
    cv2.moveWindow('My MASK blue',width,height)
    cv2.imshow("My Object blue",mysmallObjectblue)
    cv2.moveWindow('My Object blue',int(width*1.5),height)

    myMask = cv2.bitwise_or(myMaskblue,myMaskred)
    myObject = cv2.bitwise_and(frame,frame,mask=myMask)
    cv2.imshow("My Object",myObject)
    cv2.moveWindow('My Object',width,0)

    # myMask = cv2.bitwise_not(myMask)
    # myObject = cv2.bitwise_and(frame,frame,mask=myMask)
    # mysmallObject = cv2.resize(myObject,(int(width/2),int(height/2)))
    # cv2.imshow("My MASK",mysmallMask)
    # cv2.moveWindow('My MASK',0,height)
    # cv2.imshow("My Object",mysmallObject)
    # cv2.moveWindow('My Object',int(width/2),height)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()