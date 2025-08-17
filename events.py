import cv2
import numpy as np

# -----------------------------
# 1. Mouse Callback Function
# -----------------------------
# This function will be triggered whenever a mouse event occurs in the window.
# Parameters:
#   event -> type of mouse event (click, move, double-click, etc.)
#   x, y  -> coordinates of the mouse pointer
#   flags -> any flags passed by OpenCV (not used here)
#   param -> extra parameters (optional)
def draw(event, x, y, flags, param):
    # EVENT_LBUTTONDOWN = 1 means left mouse button click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a filled red circle (BGR = (0, 0, 255)) at click location
        cv2.circle(img, center=(x, y), radius=50, color=(0, 0, 255), thickness=-1)


# -----------------------------
# 2. Create a Window and Bind Mouse Event
# -----------------------------
cv2.namedWindow(winname='window')                  # Create a window named "window"
cv2.setMouseCallback("window", draw)               # Attach 'draw' function to mouse events

# -----------------------------
# 3. Load an Image
# -----------------------------
img = cv2.imread('img/tiger.jpg')

# -----------------------------
# 4. Event Loop (Display Image Until Key is Pressed)
# -----------------------------
while True:
    cv2.imshow('window', img)

    # Wait for key press (1 ms)
    # If 'x' is pressed -> break loop
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# -----------------------------
# 5. Close All Windows
# -----------------------------
cv2.destroyAllWindows()
