import cv2
import time
print(cv2.__version__)
width = 640
height = 360
jflag = 1
iflag = 1
j = 0
i = 0
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) 
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    
    frameROI = frame[j:j+60,i:i+140]
    frameROIGRAY = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frameROIBGR = cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)  
    frame = frameROIBGR

    frame[j:j+60,i:i+140] = frameROI
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if j>=300:
        jflag = 0   
    if j<=0:
        jflag = 1
    if jflag == 1:
        j+=1
    if jflag == 0:
        j-=1
    if i>=500:
        iflag = 0
    if i<=0:
        iflag = 1
    if iflag == 1:
        i+=1
    if iflag == 0:
        i-=1
    # frameROI = frame[150:210,250:390]
    # frameROIGRAY = cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY)
    # frameROIBGR = cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR)
    # cv2.imshow("My ROI BGR CAM", frameROIBGR)
    # cv2.moveWindow("My ROI BGR CAM", 645,180)
    # frame[150:210,250:390] = frameROIBGR
    # cv2.imshow("My ROI GRAY CAM", frameROIGRAY)
    # cv2.moveWindow("My ROI GRAY CAM", 645,90)
    # cv2.imshow("My ROI CAM", frameROI)
    # cv2.moveWindow("My ROI CAM", 645,0)
    # cv2.imshow("My web CAM",frame)
    # cv2.moveWindow('My web CAM',0,0)
    # if cv2.waitKey(1) == ord('q'):
    #     myCam.release()
    #     exit()
    if cv2.waitKey(1) & 0xff == ord('q'):
            break
myCam.release()

