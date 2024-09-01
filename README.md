# <span style="color:deepskyblue"> Real time Deep Convolutional Neural Networks for Detecting Underwater using YOLOv8 with Attention Models </span>

## Overview
This repository presents a custom implementation of the YOLOv8 object detection model, enhanced with the Squeeze-and-Excitation (SE) attention mechanism. Our adaptation aims to refine the model's focus on salient features, thus improving detection accuracy in complex scenarios.

## Features

- **Custom YOLOv8**: Combines the speed and robustness of YOLOv8 with advanced feature extraction capabilities.
- **SE Attention Mechanism**: Utilizes channel-wise recalibration to enhance the network's representational power.
- **Boosted Accuracy**: Prioritizes crucial features for better performance.
- **Modular SE Blocks**: Allows toggling the attention mechanism as required.
- **Pretrained Models**: Includes weights trained on standard datasets for quick deployment.
- **Real-Time Performance**: Maintains YOLOv8's swift detection for immediate application use.

## Implementation Details

- SE blocks are integrated within the backbone and head of the YOLOv8 architecture.
- The `Squeeze` operation aggregates features globally, while `Excitation` learns to use these global features to emphasize informative features.
- Accommodates various input sizes and is adaptable to different computational resources.
- The model is implemented using PyTorch for its user-friendly and flexible environment.

## Getting Started

1. Clone the repo and set up the environment with the required dependencies.
2. Obtain the pretrained weights or train your model with our custom script.
3. Run the detection using our inference scripts on your images or video feeds.
4. Feel free to adjust the SE blocks or other hyperparameters to suit your task.

## Results

Benchmark results and comparisons with the standard YOLOv8 are provided to demonstrate the enhancements brought by the SE mechanism.

This repository is an extensive open-source project showcasing the seamless integration of **object detection and tracking** using **YOLOv8** (object detection algorithm), along with **Streamlit** (a popular Python web application framework for creating interactive web apps). The project offers a user-friendly and customizable interface designed to detect and track objects in real-time video streams from sources such as RTSP, UDP, and YouTube URLs, as well as static videos and images.


## <span style="color:deepskyblue">WebApp Demo on Streamlit Server</span>

Thank you team [Streamlit](<https://github.com/streamlit/streamlit>) for the community support for the cloud upload. 

This app is up and running on Streamlit cloud server!!! You can check the demo of this web application on this link 
[yolov8-streamlit-detection-tracking-webapp](https://yolov8-object-detection-and-tracking-app.streamlit.app/)

**Note**: In the demo, Due to non-availability of GPUs, you may encounter slow video inferencing.


## Requirements

Python 3.6+
YOLOv8
Streamlit

```bash
pip install ultralytics streamlit pytube
```

## Installation

- Clone the repository: git clone <https://github.com/CodingMantras/yolov8-streamlit-detection-tracking.git>
- Change to the repository directory: `cd yolov8-streamlit-detection-tracking`
- Create `weights`, `videos`, and `images` directories inside the project.
- Download the pre-trained YOLOv8 weights from (<https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt>) and save them to the `weights` directory in the same project.

## Usage

- Run the app with the following command: `streamlit run app.py`
- The app should open in a new browser window.

### ML Model Config

- Select task (Detection)
- Use the slider to adjust the confidence threshold (25-100) for the model.

One the model config is done, select a source.

### Detection on images

- The default image with its objects-detected image is displayed on the main page.
- Select a source. (radio button selection `Image`).
- Upload an image by clicking on the "Browse files" button.
- Click the "Detect Objects" button to run the object detection algorithm on the uploaded image with the selected confidence threshold.
- The resulting image with objects detected will be displayed on the page. Click the "Download Image" button to download the image.("If save image to download" is selected)

## Detection in Videos

- Create a folder with name `videos` in the same directory
- Dump your videos in this folder
- In `settings.py` edit the following lines.

```python
# video
VIDEO_DIR = ROOT / 'videos' # After creating the videos folder

# Suppose you have four videos inside videos folder
# Edit the name of video_1, 2, 3, 4 (with the names of your video files) 
VIDEO1_PATH = VIDEO_DIR / 'video1.mp4' 
VIDEO2_PATH = VIDEO_DIR / 'video2.mp4'
VIDEO3_PATH = VIDEO_DIR / 'video3.mp4'
VIDEO4_PATH = VIDEO_DIR / 'video4.mp4'

# Edit the same names here also.
VIDEOS_DICT = {
    'video1': VIDEO1_PATH,
    'video2': VIDEO2_PATH,
    'video3': VIDEO3_PATH,
    'video4': VIDEO4_PATH,
}

# Your videos will start appearing inside streamlit webapp 'Choose a video'.
```

- Click on `Detect Video Objects` button and the selected task (detection) will start on the selected video.

### Detection on RTSP

- Select the RTSP stream button
- Enter the rtsp url inside the textbox and hit `Detect Objects` button

### Detection on YouTube Video URL

- Select the source as YouTube
- Copy paste the url inside the text box.
- The detection/segmentation task will start on the YouTube video url

<https://user-images.githubusercontent.com/104087274/226178296-684ad72a-fe5f-4589-b668-95c835cd8d8a.mov>

## Acknowledgements

This app uses [YOLOv8](<https://github.com/ultralytics/ultralytics>) for object detection algorithm and [Streamlit](<https://github.com/streamlit/streamlit>) library for the user interface. and also thanks to (https://medium.com/@mycodingmantras).


- Streamlit
- YoloV8
- Object-Detection on Images And Live Video Streams
- Python-OpenCV

### Hit star ⭐ if you like this repo!!!
