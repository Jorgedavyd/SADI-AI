#app
import cv2
from ultralytics import YOLO

#You have to download the pretrained or train on your own with all the utils of this repository.

model = YOLO('./models/face_recognition.pt')
#model = YOLO('./models/person_detection.pt')
#model = YOLO('./models/person_and_threat_detection.pt')
#model = YOLO('./models/threat_detection.pt')


model.predict(source = '0', show = True, conf = 0.5)
