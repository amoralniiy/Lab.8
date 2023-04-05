import cv2

img = cv2.imread('variant-9.png')

def pyramid(image):
    level = 5
    temp = image.copy()
    pyramid_image = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_image.append(dst)
        cv2.imshow("pyramid_down_" + str(i), dst)
        temp = dst.copy()
    return pyramid_image



pyramid(img)
cv2.imshow('Result', img)
cv2.waitKey(0)