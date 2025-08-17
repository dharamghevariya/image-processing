import cv2
import numpy as np

# Read an image

img = cv2.imread("img/strawberry.jpeg")

# img_grap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_grap.shape)

imgBlue = img[:,:,0]
imgGreen = img[:,:,1]
imgRed = img[:,:,2]

new_img = np.hstack((imgBlue, imgGreen, imgRed))


cv2.imshow("Original", new_img)


cv2.waitKey(0)