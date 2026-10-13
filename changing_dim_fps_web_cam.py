import cv2
import time
print(cv2.__version__)
width = 640
height = 320
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) # basically 1 in this is like the port at which the camera is present CAP_DSHOW stands for CAP is for capture and DSHOW is for direct show
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) # it is used to set the width of the video output 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) # it is used to set the height of the video output 
myCam.set(cv2.CAP_PROP_FPS,30) # it is used to set the frame rate of the video output 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) # this is basically setting the codec or the compression of the video 
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    _,frame=myCam.read()
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    time.sleep(1)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()

# fps does not work it depends on the camera hardware and the driver it if it is not compatible it will completely ignore it 
# to fix this we can use time.sleep(1) basically it will halt for 1 second