import cv2
import numpy as np

# -----------------------------
# 1. Global variables
# -----------------------------
drawing = False
start_x, start_y = -1, -1
end_x, end_y = -1, -1
cropped = None

# -----------------------------
# 2. Mouse callback
# -----------------------------
def crop_rectangle(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, drawing, img, preview, cropped

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        # Keep updating preview with live rectangle
        preview = img.copy()
        cv2.rectangle(preview, (start_x, start_y), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_x, end_y = x, y

        # Draw final rectangle on the original image
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

        # Crop from the original image (not modified with rectangles)
        x1, y1 = min(start_x, end_x), min(start_y, end_y)
        x2, y2 = max(start_x, end_x), max(start_y, end_y)

        cropped = original[y1:y2, x1:x2]
        if cropped.size > 0:
            cv2.imshow("Cropped Image", cropped)
            cv2.imwrite("output/cropped_image.jpg", cropped)


# -----------------------------
# 3. Setup Window
# -----------------------------
cv2.namedWindow("Image Cropper")
cv2.setMouseCallback("Image Cropper", crop_rectangle)

# -----------------------------
# 4. Load Image
# -----------------------------
img = cv2.imread("img/tiger.jpg")
original = img.copy()
preview = img.copy()

# -----------------------------
# 5. Main Loop
# -----------------------------
while True:
    # Always show preview (so live rectangle is visible)
    cv2.imshow("Image Cropper", preview)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
