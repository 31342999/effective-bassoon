import cv2
import time
print(cv2.__version__)
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    global pnt1x
    global pnt1y
    global pnt2x
    global pnt2y
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
        pnt1x = xPos
        pnt1y = yPos
    if event==cv2.EVENT_LBUTTONUP:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
        pnt2x = xPos
        pnt2y = yPos
    if event==cv2.EVENT_RBUTTONDOWN:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
width = 640
height = 360
evt = 0
pnt = 0
pnt1x = 0
pnt1y = 0
pnt2x = 0
pnt2y = 0
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow("My web CAM")
cv2.setMouseCallback("My web CAM",mouseClick)

print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    if evt == 4:
        frameROI = frame[pnt1y:pnt2y,pnt1x:pnt2x]
        cv2.imshow("My ROI CAM",frameROI)
        cv2.moveWindow('My ROI CAM',650,0)
    if evt == 2:
        cv2.destroyWindow("My ROI CAM")
        evt = 0
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()