import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('rec4.jpg')
image = cv2.imread('rec4.jpg')
print(image.shape)
ori = image.copy()
image = cv2.resize(image, (image.shape[1]//10,image.shape[0]//10))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (11,11), 0)
edged = cv2.Canny(gray, 75, 200)
print("STEP 1: Edge Detection")
plt.imshow(edged)
plt.show()
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts[1], key = cv2.contourArea, reverse = True)[:5]


for c in cnts:
    ### Approximating the contour
    #Calculates a contour perimeter or a curve length
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    # if our approximated contour has four points, then we
    # can assume that we have found our screen
    screenCnt = approx
    if len(approx) == 4:
        screenCnt = approx
        break
    # show the contour (outline)
    print("STEP 2: Finding Boundary")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
image_e = cv2.resize(image,(image.shape[1],image.shape[0]))
cv2.imwrite('image_edge.jpg',image_e)
plt.imshow(image_e)
plt.show()