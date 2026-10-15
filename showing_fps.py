import cv2
import time
start_time = time.perf_counter()
last_time = start_time
print(cv2.__version__)
width = 640
height = 360
myraduis = 30
mycolor = (0,0,0)
mythick = 2
mytext = "Hello, World!"
Font_Height = 2
Font_thick = 2
upperLeft = (250,140)
lowerRight = (390,220)
line_width = 4
counter = 0
myfont = cv2.FONT_HERSHEY_COMPLEX
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    current_time = time.perf_counter()
    if current_time - last_time >=1:
        last_count = counter
        counter=0
        last_time +=1
    ignore, frame=myCam.read()
    fps = f"FPS : {last_count} "
    cv2.putText(frame,str(fps),(60,30),myfont,1,(255,0,0),Font_thick)
    frame[140:220,250:390] = [255,0,0]
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),line_width)
    cv2.circle(frame,(int(width/2),int(height/2)),myraduis,mycolor,mythick)
    cv2.putText(frame,mytext,(120,60),myfont,Font_Height,(255,0,0),Font_thick)
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break
    counter = counter + 1


myCam.release()
