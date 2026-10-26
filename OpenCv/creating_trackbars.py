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
    global rad
    print("Raduis = ",val)
    rad = val
def myCallBack4(val):
    global Thickness
    print("Thickness = ",val)
    Thickness = val-1
print(cv2.__version__)
width = 640
height = 360
xPos = 320
yPos = 180
rad = 25
Thickness = 3
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
print(myCam.get(cv2.CAP_PROP_FPS))
cv2.namedWindow("myTrackbars")
cv2.resizeWindow("myTrackbars",400,150)
cv2.moveWindow("myTrackbars",width,0)
cv2.createTrackbar("xPos", "myTrackbars",xPos,640,myCallBack1)
cv2.createTrackbar("yPos", "myTrackbars",yPos,360,myCallBack2)
cv2.createTrackbar("Raduis", "myTrackbars",rad,180,myCallBack3)
cv2.createTrackbar("Thick", "myTrackbars",Thickness,50,myCallBack4)
while True:
    _,frame=myCam.read()
    cv2.circle(frame,(xPos,yPos),rad,(255,0,0),Thickness)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()
