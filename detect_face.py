import os
import subprocess
import cv2
import pyautogui
import _winapi

executable = "C:\\path\\to\\your\\executable.exe"
args = ["arg1", "arg2"]

working_directory = "C:\\path\\to\\working\\directory"
environment = os.environ.copy()  # Copy the current environment variables

hp, ht, pid, tid = _winapi.CreateProcess(executable, args, None, None, 0, 0, None, working_directory, environment)
def capture_screenshot():
    subprocess.call(["osascript", "-e", 'tell app "Adobe Photoshop" to activate'])
    pyautogui.hotkey('command', 'shift', '4', 'space')
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")

# Step 2: Open the screenshot in OpenCV
def open_screenshot():
    return cv2.imread("photo_2023-10-15_01-10-40.jpg")

# Step 3: Perform face detection using OpenCV
def detect_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    return faces

# Step 4: Draw outlines around detected faces
def draw_outlines(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Step 5: Display the image and save it
def display_and_save_image(image):
    cv2.imshow("Photoshop Screenshot with Face Outlines", image)
    cv2.waitKey(0)
    cv2.imwrite("photo_2023-10-15_01-10-40.jpg", image)

if __name__ == "__main__":
    # Step 1: Capture a screenshot of the active Photoshop window
    capture_screenshot()

    # Step 2: Open the screenshot in OpenCV
    image = open_screenshot()

    # Step 3: Detect faces in the image
    faces = detect_faces(image)

    # Step 4: Draw outlines around detected faces
    draw_outlines(image, faces)

    # Step 5: Display and save the image with outlines
    display_and_save_image(image)
