# YOLOv8 Object Detection Web App

This is a Flask-based web application for object detection using the YOLOv8 model. Users can upload images and view detected objects directly in their browser.

## Demo

[Watch the video demo here](YOUR_VIDEO_LINK_HERE)

## Features

- Upload images (JPG, JPEG, PNG)
- Detect objects using YOLOv8
- View original and detected images side by side

## Setup Instructions

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/yolov8_webapp.git
cd yolov8_webapp
```

### 2. Create and activate a Python virtual environment (recommended)

```sh
python3 -m venv yolov8
source yolov8/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Download YOLOv8 model weights

Place the `yolov8n.pt` file in the project root directory.  
You can download it from the [Ultralytics YOLOv8 releases](https://github.com/ultralytics/ultralytics/releases).

### 5. Run the application

```sh
python app.py
```

The app will start at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Open the web app in your browser.
2. Upload an image (JPG, JPEG, PNG).
3. View the original and detected images.

## Notes

- Uploaded images are stored in `static/uploads/`.
- Results are saved in `static/results/`.
- Maximum upload size is 16
