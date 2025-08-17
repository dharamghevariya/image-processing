import cv2
import numpy as np

# -----------------------------
# 1. Global variables
# -----------------------------
drawing = False          # True when mouse is pressed
start_x, start_y = -1, -1  # Starting point of rectangle

# -----------------------------
# 2. Mouse callback function
# -----------------------------
def draw_rectangle(event, x, y, flags, param):
    global start_x, start_y, drawing, img

    # When left mouse button is pressed, start drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y  # Save starting coordinates

    # When mouse is moving while left button is pressed, draw preview
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        # Clone original image to show live rectangle preview
        temp_img = img.copy()
        cv2.rectangle(temp_img, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow("Rectangle Drawer", temp_img)

    # When left mouse button is released, finalize the rectangle
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow("Rectangle Drawer", img)


# -----------------------------
# 3. Create a Window and Bind Callback
# -----------------------------
cv2.namedWindow("Rectangle Drawer")
cv2.setMouseCallback("Rectangle Drawer", draw_rectangle)

# -----------------------------
# 4. Load a Blank Canvas or Image
# -----------------------------
# You can either draw on a blank canvas or an image
img = np.ones((600, 800, 3), np.uint8) * 255  # white canvas
# img = cv2.imread("img/tiger.jpg")           # OR draw on an actual image

# -----------------------------
# 5. Event Loop
# -----------------------------
while True:
    cv2.imshow("Rectangle Drawer", img)

    # Press 'x' to exit
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
