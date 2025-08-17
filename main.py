import cv2
import numpy as np

# -----------------------------
# 1. Read an Image
# -----------------------------
# OpenCV loads images as NumPy arrays in BGR format (not RGB).
img = cv2.imread("img/strawberry.jpeg")
cv2.imshow("Original Image", img)

# -----------------------------
# 2. Converting to Grayscale
# -----------------------------
# A grayscale image has only 1 channel (intensity values).
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_gray)
print("Grayscale image shape:", img_gray.shape)  # (height, width)

# -----------------------------
# 3. Image Channel Division
# -----------------------------
# Splitting into individual B, G, R channels
imgBlue = img[:, :, 0]   # Blue channel
imgGreen = img[:, :, 1]  # Green channel
imgRed = img[:, :, 2]    # Red channel

# Show channels separately
cv2.imshow("Blue Channel", imgBlue)
cv2.imshow("Green Channel", imgGreen)
cv2.imshow("Red Channel", imgRed)

# Combine channels horizontally for comparison
new_img = np.hstack((imgBlue, imgGreen, imgRed))
cv2.imshow("Channels Side-by-Side", new_img)

# -----------------------------
# 4. Image Resize
# -----------------------------
# Resize to a fixed size
img_resize1 = cv2.resize(img, (800, 800))

# Resize to half of the original dimensions
img_resize2 = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv2.imshow("Resized (800x800)", img_resize1)
cv2.imshow("Resized (Half Size)", img_resize2)
print("Half-size image shape:", img_resize2.shape)

# -----------------------------
# 5. Image Flipping
# -----------------------------
# Flip codes: 0 = vertical, 1 = horizontal, -1 = both
img_flip_vertical = cv2.flip(img, 0)
img_flip_horizontal = cv2.flip(img, 1)
img_flip_both = cv2.flip(img, -1)

cv2.imshow("Flipped Vertically", img_flip_vertical)
cv2.imshow("Flipped Horizontally", img_flip_horizontal)
cv2.imshow("Flipped Both", img_flip_both)

# -----------------------------
# 6. Image Cropping
# -----------------------------
# Cropping uses NumPy slicing: img[y1:y2, x1:x2]
img_cropped = img[100:300, 100:300]
cv2.imshow("Cropped Image (100:300, 100:300)", img_cropped)

# -----------------------------
# 7. Saving an Image with OpenCV
# -----------------------------
# cv2.imwrite("output_path", image)
cv2.imwrite("output/strawberry_cropped.jpg", img_cropped)

# -----------------------------
# 8. Drawing Shapes and Text
# -----------------------------
# These are often used in object detection for marking detected objects.

# Copy image for drawing
img_shapes = img.copy()

# Draw Rectangle (img, top-left, bottom-right, color(BGR), thickness)
cv2.rectangle(img_shapes, (50, 50), (200, 200), (0, 255, 0), 3)

# Draw Circle (img, center, radius, color(BGR), thickness)
cv2.circle(img_shapes, (300, 300), 50, (255, 0, 0), -1)  # -1 = filled circle

# Draw Line (img, start_point, end_point, color, thickness)
cv2.line(img_shapes, (100, 400), (400, 400), (0, 0, 255), 5)

# Put Text (img, text, position, font, scale, color, thickness)
cv2.putText(img_shapes, "Strawberry", (50, 450),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Shapes & Text Example", img_shapes)

# -----------------------------
# Wait and Close
# -----------------------------
cv2.waitKey(0)   # Wait until any key is pressed
cv2.destroyAllWindows()
