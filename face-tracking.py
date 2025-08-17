# import cv2
#
# # Global variables
# drawing = False
# ix, iy = -1, -1
# rect_color = (0, 255, 0)
#
# # Mouse callback function
# def draw_rectangle(event, x, y, flags, param):
#     global ix, iy, drawing, frame, rect_color
#
#     if event == cv2.EVENT_LBUTTONDOWN:  # Mouse pressed
#         drawing = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_MOUSEMOVE:  # Mouse move
#         if drawing:
#             temp = frame.copy()  # copy current frame
#             cv2.rectangle(temp, (ix, iy), (x, y), rect_color, 2)
#             cv2.imshow("Video", temp)
#
#     elif event == cv2.EVENT_LBUTTONUP:  # Mouse released
#         drawing = False
#         cv2.rectangle(frame, (ix, iy), (x, y), rect_color, 2)
#
# # Open video capture (0 = webcam, or path to file)
# cap = cv2.VideoCapture(0)
# cv2.namedWindow("Video")
# cv2.setMouseCallback("Video", draw_rectangle)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     cv2.imshow("Video", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):  # Quit with 'q'
#         break
#
# cap.release()
# cv2.destroyAllWindows()

import cv2

# -----------------------------
# 1. Load Haar Cascade for Face Detection
# -----------------------------
# OpenCV provides pre-trained Haar Cascade classifiers for face, eyes, smiles, etc.
# Here we use the frontal face classifier.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# -----------------------------
# 2. Open Video Capture
# -----------------------------
# 0 = default webcam, or provide a video file path for processing a saved video
cap = cv2.VideoCapture(0)

# -----------------------------
# 3. Main Video Loop
# -----------------------------
while True:
    # Read a frame from the video stream
    ret, frame = cap.read()
    if not ret:
        break  # Exit if video cannot be read

    # -----------------------------
    # 3a. Convert to Grayscale
    # -----------------------------
    # Haar cascades work better on grayscale images
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # 3b. Detect Faces
    # -----------------------------
    # detectMultiScale returns a list of rectangles around detected objects
    # scaleFactor: compensates for faces appearing at different sizes
    # minNeighbors: higher value = fewer detections but higher quality
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # -----------------------------
    # 3c. Draw Rectangles Around Faces
    # -----------------------------
    for (x, y, w, h) in faces:
        # Draw a green rectangle with thickness 2 around each detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # -----------------------------
    # 3d. Display the Video Frame
    # -----------------------------
    cv2.imshow("Face Tracking", frame)

    # -----------------------------
    # 3e. Exit Condition
    # -----------------------------
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# 4. Release Resources
# -----------------------------
cap.release()             # Release webcam/video
cv2.destroyAllWindows()   # Close all OpenCV windows

