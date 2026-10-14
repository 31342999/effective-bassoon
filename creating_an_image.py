import numpy as np
import cv2
print(cv2.__version__)
frame=np.zeros([800,800,3],dtype=np.uint8)
iold = 0
jold = 0
for i in range(0,800):
    for j in range(0,800):
        x = int(i/8)
        y = int(j/8)
        if (x+y)%2 == 1:
                frame[iold:i,jold:j] = [255,255,255]
        jold = j
    iold = i
while True:
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break