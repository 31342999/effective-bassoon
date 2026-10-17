import cv2
import time
print(cv2.__version__)
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
        pnt = (xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
    if event==cv2.EVENT_RBUTTONDOWN:
        print("Mouse event was", event)
        print("Pos : ", xPos,yPos)
        evt = event
width = 640
height = 360
evt = 0
pnt = 0
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
    if evt == 1 or evt == 4:
        cv2.circle(frame,pnt,25,(255,0,0),2)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()