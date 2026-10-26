import cv2
import time
print(cv2.__version__)
rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))

width = 640
height = 320
myCam = cv2.VideoCapture(0,cv2.CAP_DSHOW) 
myCam.set(cv2.CAP_PROP_FRAME_WIDTH,width) 
myCam.set(cv2.CAP_PROP_FRAME_HEIGHT,height) 
myCam.set(cv2.CAP_PROP_FPS,30) 
myCam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
print(myCam.get(cv2.CAP_PROP_FPS))
while True:
    ignore, frame=myCam.read()
    frame = cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0,rows):
        for j in range(0,columns):
            WindowName ='Window'+str(i)+" x "+str(j)
            cv2.imshow(WindowName,frame)
            cv2.moveWindow(WindowName,int(width/columns)*j,int(height/columns+30)*i)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()
