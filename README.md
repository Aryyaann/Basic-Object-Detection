Basic Object Detection (Real-Time Webcam)

A simple, fast, and beginner-friendly project that runs real-time object detection from your webcam using Python and OpenCV.
The goal is to keep the project minimal and easy to run in VS Code on Windows, while still producing clean, useful results.

This project is ideal if you want a quick, practical starting point for:

real-time computer vision experiments

learning the basics of object detection

building a foundation to later train your own custom detector (e.g., watch/keys, etc.)

What it does

Opens your webcam feed

Runs object detection on each frame

Draws bounding boxes + class labels + confidence score

Displays the annotated video stream in real time

Tech stack

Python 3.10+

OpenCV for camera + display

Ultralytics YOLO (lightweight models available for CPU)

Works on Windows without GPU (CPU-only)

Project structure

(Update filenames if your project uses different names)

Basic-Object-Detection/
│── webcam_detect.py
│── requirements.txt
│── README.md
│── .gitignore
└── (optional) assets/

Setup (Windows + VS Code)
1) Create and activate a virtual environment

Open the terminal inside the project folder:

python -m venv venv
venv\Scripts\activate

2) Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, you can install directly:

pip install ultralytics opencv-python

Run the project
python webcam_detect.py


Controls:

Press Q (or ESC) to quit

Performance tips (CPU-only)

If the video feels slow on your laptop, these changes usually help a lot:

Use a smaller model (fastest):

yolov8n.pt (nano) is usually the best CPU choice

Lower the input resolution (imgsz), e.g. 320–480

Increase confidence threshold (fewer boxes to draw), e.g. 0.45–0.55

Process every 2nd frame (frame skipping)

These optimizations can significantly improve FPS without changing the project structure.

About detected objects (important)

Most pretrained models detect a fixed list of common objects (for example, the COCO dataset classes: person, phone, bottle, etc.).
That means objects like keys or wristwatch may not always appear as a label out-of-the-box.

If your goal is to detect specific custom objects (e.g., watch, keys, wallet), the next step is:

fine-tuning/training a small model on your own labeled images
or

using an open-vocabulary detector that supports custom text labels

This repo is designed to be the clean baseline you build on.

Common issues
Webcam doesn’t open

Close apps that might be using the camera (Zoom/Teams/Discord)

Try changing the camera index in code:

cv2.VideoCapture(0) → cv2.VideoCapture(1)

“Module not found”

Make sure your venv is activated:

venv\Scripts\activate

Then reinstall:

pip install -r requirements.txt

Roadmap (next improvements)

 Add FPS counter + performance mode toggle

 Add “target classes” mode (filter detections)

 Export detections to a log file (CSV/JSON)

 Custom training guide for personal objects (keys/watch)

 Simple UI controls (confidence threshold, model choice)

License

This project is free to use for learning and personal experimentation.
(If you want, you can add an official license like MIT.)
