#Person detection
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data='person_detection.yaml', epochs=100, imgsz=320)
