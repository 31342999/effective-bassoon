import cv2
import time
import numpy as np

def myCallBack1(val):
    global LowHue
    print("Low Hue = ",val)
    LowHue = val
def myCallBack2(val):
    global HighHue
    print("High Hue = ",val)
    HighHue = val
def myCallBack3(val):
    global LowSat
    print("Low Sat = ",val)
    LowSat = val
def myCallBack4(val):
    global HighSat
    print("High Sat = ",val)
    HighSat = val
def myCallBack5(val):
    global LowVal
    print("Low Val = ",val)
    LowVal = val
def myCallBack6(val):
    global HighVal
    print("High Val = ",val)
    HighVal = val


print(cv2.__version__)
width = 640
height = 360

LowHue  = 10
HighHue = 20
LowSat  = 10
HighSat = 250
LowVal  = 10
HighVal = 250
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
cv2.namedWindow("myTrackbars")
cv2.resizeWindow("myTrackbars",400,250)
cv2.moveWindow("myTrackbars",width,0)
cv2.createTrackbar("Low Hue", "myTrackbars",LowHue,180,myCallBack1)
cv2.createTrackbar("High Hue", "myTrackbars",HighHue,180,myCallBack2)
cv2.createTrackbar("Low Sat", "myTrackbars",LowSat,255,myCallBack3)
cv2.createTrackbar("High Sat", "myTrackbars",HighSat,255,myCallBack4)
cv2.createTrackbar("Low Val", "myTrackbars",LowVal,255,myCallBack5)
cv2.createTrackbar("High Val", "myTrackbars",HighVal,255,myCallBack6)
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound = np.array([LowHue,LowSat,LowVal])
    upperBound = np.array([HighHue,HighSat,HighVal])
    myMask = cv2.inRange(frameHSV,lowerBound,upperBound)
    mysmallMask = cv2.resize(myMask,(int(width/2),int(height/2)))
    # myMask = cv2.bitwise_not(myMask)
    myObject = cv2.bitwise_and(frame,frame,mask=myMask)
    mysmallObject = cv2.resize(myObject,(int(width/2),int(height/2)))
    cv2.imshow("My MASK",mysmallMask)
    cv2.moveWindow('My MASK',0,height)
    cv2.imshow("My Object",mysmallObject)
    cv2.moveWindow('My Object',int(width/2),height)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()