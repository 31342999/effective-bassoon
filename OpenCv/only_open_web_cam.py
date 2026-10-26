import cv2
print(cv2.__version__)
myCam = cv2.VideoCapture(0)

while True:
    _,frame=myCam.read()
    cv2.imshow("My web CAM",frame)
    cv2.moveWindow('My web CAM',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

myCam.release()
