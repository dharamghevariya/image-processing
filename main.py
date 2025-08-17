import cv2
import numpy as np

# Read an image

img = cv2.imread("img/strawberry.jpeg")

img_grap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("Original", img_grap)

cv2.waitKey(0)