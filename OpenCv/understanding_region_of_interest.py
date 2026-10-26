import cv2
import time
print(cv2.__version__)
width = 640
height = 360
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    frameROI = frame[150:210,250:390]
    frameROIGRAY = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)
    cv2.imshow("My ROI BGR CAM", frameROIBGR)
    cv2.moveWindow("My ROI BGR CAM", 645,180)
    frame[150:210,250:390] = frameROIBGR
    cv2.imshow("My ROI GRAY CAM", frameROIGRAY)
    cv2.moveWindow("My ROI GRAY CAM", 645,90)
    cv2.imshow("My ROI CAM", frameROI)
    cv2.moveWindow("My ROI CAM", 645,0)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break
myCam.release()
