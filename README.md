# Retail Checkout Object Detection System

## Overview

This project uses a custom-trained YOLO (You Only Look Once) object detection model to identify retail products in real time from images, videos, or a webcam feed. The system is designed for retail checkout applications where products can be automatically detected and counted, helping reduce manual scanning and improve checkout efficiency.

The model has been trained to recognize the following product categories:

* Aqua
* Chitato
* Indomie
* Pepsodent
* Shampoo
* Tissue

---

# Features

* Real-time object detection using a webcam
* Product detection from images
* Product detection from video files
* Automatic object counting
* Bounding box visualization with confidence scores
* FPS (Frames Per Second) monitoring
* Optional video recording of inference results

---

# Project Structure

```text
project/
│
├── yolo_detect.py          # Main detection script
├── my_model.pt             # Trained YOLO model
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── test_images/
├── test_videos/
│
└── output/
```

---

# Requirements

## Hardware

* Webcam (optional)
* MacBook, Windows, or Linux machine

## Software

* Python 3.10+
* OpenCV
* NumPy
* Ultralytics YOLO

---

# Installation

Create and activate a Python environment:

```bash
conda create -n yolo-env python=3.12
conda activate yolo-env
```

Install dependencies:

```bash
pip install ultralytics opencv-python numpy
```

Verify installation:

```bash
python -c "from ultralytics import YOLO; print('YOLO installed successfully')"
```

---

# Running the Application

## 1. Webcam Detection

Use the built-in webcam or an external USB camera.

```bash
python yolo_detect.py --model my_model.pt --source usb0 --resolution 1280x720
```

### Parameters

| Parameter      | Description                          |
| -------------- | ------------------------------------ |
| `--model`      | Path to trained YOLO model           |
| `--source`     | Camera source (`usb0`, `usb1`, etc.) |
| `--resolution` | Display resolution (WxH)             |

Example:

```bash
python yolo_detect.py --model my_model.pt --source usb0 --resolution 1920x1080
```

---

## 2. Detect Objects in an Image

```bash
python yolo_detect.py --model my_model.pt --source test.jpg
```

---

## 3. Detect Objects in a Folder of Images

```bash
python yolo_detect.py --model my_model.pt --source test_images
```

---

## 4. Detect Objects in a Video

```bash
python yolo_detect.py --model my_model.pt --source demo.mp4
```

---

# Confidence Threshold

Control the minimum confidence required for displaying detections.

Example:

```bash
python yolo_detect.py \
--model my_model.pt \
--source usb0 \
--thresh 0.6
```

Default:

```text
0.5
```

---

# Recording Detection Results

To save the output video:

```bash
python yolo_detect.py \
--model my_model.pt \
--source usb0 \
--resolution 1280x720 \
--record
```

Output file:

```text
demo1.avi
```

---

# Controls

| Key | Action                              |
| --- | ----------------------------------- |
| Q   | Quit application                    |
| S   | Pause detection                     |
| P   | Save current frame as `capture.png` |

---

# Output Information

The application displays:

* Detected products
* Confidence score for each detection
* Bounding boxes around products
* Total object count
* Real-time FPS

Example:

```text
Aqua: 98%
Indomie: 95%
Pepsodent: 92%

Number of objects: 3
FPS: 28.7
```

---

# Training Information

The YOLO model was trained using a custom retail product dataset containing six product categories:

```text
aqua
chitato
indomie
pepsodent
shampoo
tissue
```

The trained model is stored as:

```text
my_model.pt
```

---

# Troubleshooting

## Model Not Found

Error:

```text
ERROR: Model path is invalid or model was not found
```

Solution:

Verify that `my_model.pt` exists in the project directory.

---

## Camera Not Detected

Error:

```text
Unable to read frames from the camera
```

Solutions:

* Verify camera permissions are enabled.
* Close other applications using the camera.
* Try a different camera index (`usb1`, `usb2`).

---

## Low FPS

Possible solutions:

* Reduce resolution:

```bash
--resolution 640x480
```

* Use a smaller YOLO model.
* Enable GPU acceleration if available.

---

# Example Command

```bash
python yolo_detect.py \
--model my_model.pt \
--source usb0 \
--resolution 1280x720 \
--thresh 0.5
```

This launches real-time product detection using the webcam and displays detected retail products with bounding boxes, confidence scores, object counts, and FPS information.
