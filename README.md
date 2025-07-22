# Real-Time-Object-Tracker

This project allows you to manually select an object in the first webcam frame and track it in real time using OpenCV's KCF tracker. If the object is lost, you can press R to reselect it or X to exit.

-------------------------------
📋 Features:

- 🎯 Manual object selection via mouse (on first frame)

- 🎞️ Real-time tracking using OpenCV's KCF tracker

- 🔄 Optional re-selection if the object is lost

- ❌ Quit cleanly with a key press

-------------------------------


✅ Requirements:

- Python ≥ 3.6

- OpenCV with contrib modules

-------------------------------

📦 Installations:

` pip install opencv-contrib-python `

-------------------------------
Running the Tracker:

` python tracker.py `

-------------------------------
🔧 Controls:

- Use your mouse to draw a box around the object in the first frame.

- If the tracker loses the object:

- Press R to reselect the object manually.

- Press X to exit the application.

-------------------------------
🧠 How It Works

- On startup, the system captures a frame from your webcam.

- You draw a bounding box around the object you want to track.

- The program initializes OpenCV's KCF (Kernelized Correlation Filters) tracker on that object.

- If tracking is lost, you’re prompted to reselect the object or exit.

-------------------------------
🧠 Implementation Details

- The webcam feed is accessed via cv2.VideoCapture(0).

- The user manually selects the object in the first frame using cv2.selectROI(), which returns a bounding box.

- OpenCV’s built-in KCF tracker (cv2.TrackerKCF_create()) is initialized with this box.

- The tracker continuously updates the object's position on each new frame.

- If tracking fails (object moves out of frame or is occluded), a message is displayed and the user can:

    - Press R to reselect and reinitialize tracking

    - Press X to exit

- The tracking loop continues until the user explicitly exits.