 # YOLOv8 Real-Time Object Detection

This project implements real-time object detection using the YOLOv8 model by Ultralytics. The program captures live video from the webcam and identifies objects in real time with high accuracy and speed. This is ideal for applications such as security systems, smart surveillance, and interactive AI-based applications.

---

## Table of Contents

1. [Features](#features)  
2. [Requirements](#requirements)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [How It Works](#how-it-works)  
6. [Troubleshooting](#troubleshooting)  
7. [Credits](#credits)  
8. [License](#license)  

---

## Features

- **Real-time object detection** using YOLOv8.
- **Fast and efficient** detection with OpenCV.
- **Live webcam feed** integration.
- **Easy to customize** for different YOLOv8 models or video sources.
- **Quick setup** with Poetry for dependency management.

---

## Requirements

- **Operating System**: macOS, Linux, or Windows  
- **Python**: 3.8 or higher  
- **Dependencies**:  
  - OpenCV  
  - Ultralytics YOLOv8  

---

## Installation

Follow these steps to set up the project on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/tommattoo/yolo-real-time-detection.git
cd yolo-real-time-detection
```

### 2. Install Poetry (if not already installed)

Poetry is used to manage dependencies for this project. To install Poetry, run the following:

```bash
pip install poetry
```

### 3. Install Dependencies

With Poetry installed, you can install all the necessary dependencies:

```bash
poetry install
```
### 4. Activate the Poetry Environment

To activate the virtual environment and ensure you are using the correct dependencies, run the following command:

```bash
poetry shell
```
### Usage

After installing the dependencies and activating the environment, run the following command to start real-time object detection using your webcam:

```bash
python main.py
```

### Keyboard Shortcuts

Press `q` to exit the detection loop and close the program.

### Model Customization

By default, the project uses the small YOLOv8 model (`yolov8n.pt`). You can change the model by specifying a different file. For example, you can use `yolov8s.pt` for a medium-sized model or `yolov8x.pt` for a larger, more accurate model. The model files are available on the [Ultralytics YOLO repository](https://github.com/ultralytics/yolov8).

### How It Works

#### Main Components

- **Model Loading**: The YOLOv8 model is loaded using the Ultralytics library.
- **Webcam Feed**: OpenCV captures live video from the default webcam.
- **Object Detection**: For each frame, the YOLO model detects objects and draws bounding boxes around them.
- **Real-Time Display**: The processed frame is displayed with the bounding boxes and labels of the detected objects.

#### Code Breakdown (main.py)

```python
import cv2
from ultralytics import YOLO
```

# Load YOLOv8 model
model = YOLO('yolov8n.pt')  # You can replace 'yolov8n.pt' with other model variants

# Open webcam
cap = cv2.VideoCapture(0)

# Loop for capturing frames and running detection
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Perform detection
    results = model(frame)
    result = results[0]  # Get the first result from the list
    frame_with_results = result.plot()

    # Display frame
    cv2.imshow("Real-Time Object Detection", frame_with_results)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
### Troubleshooting

- **Webcam Not Detected**:
  - Ensure your webcam is properly connected and accessible.
  - If it still doesn't work, try changing the camera source. Replace `cv2.VideoCapture(0)` with `cv2.VideoCapture(1)` to use another available camera.

- **AttributeError: 'list' object has no attribute 'plot'**:
  - Ensure you are accessing the first detection result correctly: `result = results[0]`.

- **Dependency Issues**:
  - Verify dependencies are installed by running `poetry install`.

- **Model Not Found**:
  - Ensure that the `yolov8n.pt` file is correctly downloaded or provide the correct path to the model in the YOLO constructor.

### Credits

- **YOLOv8 Model**: Ultralytics YOLOv8
- **Dependencies**: OpenCV, Ultralytics library

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

