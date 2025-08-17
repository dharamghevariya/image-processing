import cv2
import numpy as np

# Read an image

img = cv2.imread("img/strawberry.jpeg")

# img_grap = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_grap.shape)

# image channel division

# imgBlue = img[:,:,0]
# imgGreen = img[:,:,1]
# imgRed = img[:,:,2]
#
# new_img = np.hstack((imgBlue, imgGreen, imgRed))

# image resize

# img_resize1 = cv2.resize(img, (800, 800))
# img_resize2 = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
#
# print(img_resize2.shape)

# image flipping

# img_flipped = cv2.flip(img, -1) # 0, 1, -1

# image cropping

# img_cropped = img[100:300, 100:300]

cv2.imshow("Original", img_cropped)


cv2.waitKey(0)