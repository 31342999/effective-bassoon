
import cv2

img = cv2.imread("Images/bus.jpg")

cv2.imshow("Test Window", img)

print("Waiting for key press...")
key = cv2.waitKey(0)

print("Key pressed:", key)

cv2.destroyAllWindows()
