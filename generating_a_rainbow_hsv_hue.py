import cv2
import time
import numpy as np
print(cv2.__version__)
x = np.zeros([256,181,3],dtype = np.uint8)
y = np.zeros([256,181,3],dtype = np.uint8)
i = 0
j = 0
for i in range (0,181):
    for j in range(0,256): #HSV
        x[j][i] = (i,j,255)
w = cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
i = 0 
j = 0
for i in range (0,181):
    for j in range(0,256): #HSV
        y[j][i] = (i,255,j)
z = cv2.cvtColor(y,cv2.COLOR_HSV2BGR)
cv2.namedWindow("Color Space",cv2.WINDOW_NORMAL)
cv2.namedWindow("Color Space 1",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Space", 800,256)
cv2.resizeWindow("Color Space 1", 800,256)
while True:
    cv2.imshow("Color Space", w)
    cv2.moveWindow("Color Space",0,0)
    cv2.imshow("Color Space 1", z)
    cv2.moveWindow("Color Space 1",0,287)
    if cv2.waitKey(1) == ord('q'):
        break
