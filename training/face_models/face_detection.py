#Person and threat detection at the same time
from ultralytics import YOLO
import os

def transport():
    folder = os.listdir('/runs')[-1]
    path = os.path.join('/runs', folder, 'weights', 'best.pt')        
    models_path = os.abspath(os.path.join('/SADI-AI', 'models'))
    os.rename(path, models_path)

def train():
    # Load a model
    model = YOLO('yolov8n.yaml')  # build a new model from YAML

    # Train the model
    results = model.train(data='face_detection.yaml', epochs=100, imgsz=640)

    transport()