import cv2
import numpy as np
from PIL import Image

def AddImageToCenter(frame, x, y, img):
    pilim = Image.fromarray(frame)
    pilim.paste(img, box=(int(x) - 32, int(y) - 32), mask=img)
    frame = np.array(pilim)
    return frame

def PointSearch(frame, templateImage, sensitivity):
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayImage = cv2.cvtColor(img_label, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(grayFrame, grayImage, cv2.TM_CCOEFF_NORMED)
    threshold = sensitivity
    locate = np.where(res >= threshold)
    return locate

cap = cv2.VideoCapture(0)
label = "refPoint.jpg"
speedo = Image.open('fly64.png').convert('RGBA')
img_label = cv2.imread(label)
heightPoint, widthPoint, channels = img_label.shape
count = 1
xSum = 0
ySum = 0
while True:
    ret, frame = cap.read()
    loc = PointSearch(frame, img_label, 0.6)
    if len(loc[0]) > 0:
        x = loc[1][0]
        y = loc[0][0]
        cv2.rectangle(frame, (x, y), (x + widthPoint, y + heightPoint), (0, 255, 0), 2)
        cx = x + widthPoint / 2
        cy = y + heightPoint / 2
        xSum += cx
        ySum += cy
        count +=1
        xSr = xSum/count
        ySr = ySum/count
        frame = AddImageToCenter(frame, cx,cy, speedo)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Средняя координата за текущий сеанс: ")
print("x: ", xSr)
print("y: ", ySr)