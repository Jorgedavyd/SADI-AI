#Person and threat detection at the same time
from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data='both.yaml', epochs=100, imgsz=640)