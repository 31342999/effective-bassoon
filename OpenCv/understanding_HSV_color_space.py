import cv2
import time
import numpy as np
def mouseClick(event,xPos,yPos,flags,parms):
    global xVal
    global yVal
    global evt
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xPos
        yVal = yPos
        evt = event
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        evt = event
print(cv2.__version__)
width = 640
height = 360
xVal = 0
yVal = 0
evt = 0
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("My web CAM")
cv2.setMouseCallback("My web CAM", mouseClick) 
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    if evt == 1:
        x = np.zeros([250,250,3],dtype = np.uint8)
        y = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr = y[yVal][xVal]
        print(clr)
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow("Color Space", x)
        cv2.moveWindow("Color Space",width,0)
        evt = 0
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()