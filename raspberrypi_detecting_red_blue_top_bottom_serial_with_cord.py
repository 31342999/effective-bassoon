import numpy as np
import cv2
import serial
import time

print(cv2.__version__)
hueLow=0
hueHigh=28
satLow=167
satHigh=255
valLow=135
valHigh=255

hueLow2=103
hueHigh2=115
satLow2=119
satHigh2=255
valLow2=99
valHigh2=255
def onTrack1(val):
    global hueLow
    hueLow=val
    print('Low Hue: ',val)
def onTrack2(val):
    global hueHigh
    hueHigh=val
    print('High Hue: ',val)
def onTrack3(val):
    global satLow
    satLow=val
    print('Low Sat: ',val)
def onTrack4(val):
    global satHigh
    satHigh=val
    print('High Sat: ',val)
def onTrack5(val):
    global valLow
    valLow=val
    print('Low Val: ',val)
def onTrack6(val):
    global valHigh
    valHigh=val
    print('High Val: ',val)


def onTrack7(val):
    global hueLow2
    hueLow2=val
    print('Low Hue2: ',val)
def onTrack8(val):
    global hueHigh2
    hueHigh2=val
    print('High Hue2: ',val)
def onTrack9(val):
    global satLow2
    satLow2=val
    print('Low Sat2: ',val)
def onTrack10(val):
    global satHigh2
    satHigh2=val
    print('High sat2: ',val)
def onTrack11(val):
    global valLow2
    valLow2=val
    print('Low Val2: ',val)
def onTrack12(val):
    global valHigh2
    valHigh2=val
    print('High Val2: ',val)

def send_byte(value,xPos,yPos):
    byte_to_send = bytes([value]) 
    trash123 = xPos
    trash123 = yPos
    ser.write(byte_to_send)
    print(f"Sent raw byte: {value} ({byte_to_send})")

width = 640
height = 360
trash123=0

global y 
global y1 
global x 
global x1 
global flag
global i

y = -1
y1 = -1
x = -1
x1 = -1
flag = 0
i = -1
buffer = 10

PORT_NAME = '/dev/ttyACM0'  
BAUD_RATE = 115200
cam = cv2.VideoCapture(0) 
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
cam.set(cv2.CAP_PROP_FPS,30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
cv2.namedWindow('myTracker')
cv2.moveWindow('myTracker',width,0)
cv2.resizeWindow('myTracker',400,500)
cv2.createTrackbar('Hue Low','myTracker',0,180,onTrack1)
cv2.createTrackbar('Hue High','myTracker',28,180,onTrack2)
cv2.createTrackbar('Sat Low','myTracker',167,255,onTrack3)
cv2.createTrackbar('Sat High','myTracker',255,255,onTrack4)
cv2.createTrackbar('Val Low','myTracker',135,255,onTrack5)
cv2.createTrackbar('Val High','myTracker',255,255,onTrack6)

cv2.createTrackbar('Hue Low2','myTracker',103,180,onTrack7)
cv2.createTrackbar('Hue High2','myTracker',115,180,onTrack8)
cv2.createTrackbar('Sat Low2','myTracker',119,255,onTrack9)
cv2.createTrackbar('Sat High2','myTracker',255,255,onTrack10)
cv2.createTrackbar('Val Low2','myTracker',99,255,onTrack11)
cv2.createTrackbar('Val High2','myTracker',255,255,onTrack12)

ser = serial.Serial(
    port=PORT_NAME,
    baudrate=BAUD_RATE,
    timeout=1
)

print(f"UART Ready on {ser.name}")

while True:
    ignore,  frame = cam.read()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])

    lowerBound2=np.array([hueLow2,satLow2,valLow2])
    upperBound2=np.array([hueHigh2,satHigh2,valHigh2])

    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)

    #myMask=cv2.add(myMask,myMask2)
    #myMask=np.logical_or(myMask,myMask2)

    contours,junk = cv2.findContours(myMask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours1,junk1 = cv2.findContours(myMask2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area>=200:
            # cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    for contour in contours1:
            area = cv2.contourArea(contour)
            if area>=200:
                # cv2.drawContours(frame,[contour],0,(255,0,0),3)
                x1,y1,w1,h1=cv2.boundingRect(contour)
                cv2.rectangle(frame,(x1,y1),(x1+w1,y1+h1),(255,0,0),3)

    #myMask=cv2.bitwise_not(myMask)
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    myMask = cv2.bitwise_or(myMask,myMask2)
    mySelection=cv2.bitwise_and(frame,frame, mask=myMask)
    mySelection=cv2.resize(mySelection,(int(width/2),int(height/2)))
    cv2.imshow('My Selection', mySelection)
    cv2.moveWindow('My Selection',int(width/2),height)
    cv2.imshow('My Mask', myMaskSmall)
    cv2.moveWindow('My Mask',0,height)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',0,0)
    if(y>0 and y1>0):
        if(flag == 1):
            send_byte(i,x,y)
            if(abs(x-x1)<=buffer):
                send_byte(2,x,y)
                i = -1
                flag = 0

        if(flag == 0):
            if (y<y1):
                print("red is on top")
                print("blue cord",x, y)
                print("red cord",x1,y1)
                i = 1
                flag = 1
            if (y1<y):
                print("Blue is on top")
                print("blue cord",x, y)
                print("red cord",x1,y1)
                i = 0
                flag = 1

        y1 = -1
        y = -1
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
ser.close()