
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("Images/bus.jpg", show=False)

img = results[0].plot()

cv2.namedWindow("YOLO Detection")
cv2.imshow("YOLO Detection", img)

while True:
    key = cv2.waitKey(100) & 0xFF
    if key == ord("q") or key == 27:
        break

cv2.destroyAllWindows()
