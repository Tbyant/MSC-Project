from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'detecting.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'detected.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'video1': VIDEO_DIR / 'crab video.mp4',
    'Video2': VIDEO_DIR / 'Ballan wrasse.mp4',
    'Video3': VIDEO_DIR / 'pout1.mp4',
    'Video4': VIDEO_DIR / 'shrimp1.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'best.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

# SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# # Webcam
# WEBCAM_PATH = 1
