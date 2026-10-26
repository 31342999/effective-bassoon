import cv2
import time
def myCallBack1(val):
    global xPos
    print("xPos = ",val)
    xPos = val
def myCallBack2(val):
    global yPos
    print("yPos = ",val)
    yPos = val
def myCallBack3(val):
    global Size
    print("Size = ",val)
    Size = val
print(cv2.__version__)
width = 640
height = 360
xPos = 0
yPos = 0
Size = 5
oldSize = 5
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
print(myCam.get(cv2.CAP_PROP_FPS))
cv2.namedWindow("myTrackbars")
cv2.resizeWindow("myTrackbars",400,150)
cv2.moveWindow("myTrackbars",width,0)
cv2.createTrackbar("Size", "myTrackbars",Size,50,myCallBack3)
cv2.createTrackbar("xPos", "myTrackbars",xPos,640,myCallBack1)
cv2.createTrackbar("yPos", "myTrackbars",yPos,360,myCallBack2)
while True:
    ignore, frame=myCam.read()
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',xPos,yPos)
    if oldSize != Size:
        myCam.set(cv2.CAP_PROP_FRAME_WIDTH,int(width*Size/16))
        myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,int(height*Size/9)) 
        oldSize = Size
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()
