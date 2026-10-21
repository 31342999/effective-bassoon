import cv2
import numpy as np
width = 180*4
height = 150
spectrum_img = np.zeros((height,width,3), dtype = np.uint8)

for x in range(width):
    opencv_hue = int(x/4)
    spectrum_img[:,x] = [opencv_hue,255,255]

bgr_specturm = cv2.cvtColor(spectrum_img,cv2.COLOR_HSV2BGR)

padding_bottom = 60

canvas = np.zeros((height+padding_bottom,width,3), dtype=np.unit8)

canvas[0:height,0:width] = bgr_specturm

for opencv_hue in range (0,180,15):
    x_pos = opencv_hue *4
    degree = opencv_hue * 2

    label_deg = f"{degree}"
    label_h = f"H:{opencv_hue}"

    text_x = x_pos - 12 if opencv_hue > 0 else x_pos + 2
    if opencv_hue == 165:
        text_x = x_pos - 20

    cv2.line(canvas,(x_pos,height),(x_pos,height+8),(255,255,255),1)

    