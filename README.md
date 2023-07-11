# SADI A.I. ()
This is a base program for A.I. powered security systems.

## Functionalities

### Pretrained:

#### Person detection:

- This model named 

```python 
person_detection.pt
```

has been made for person tracking.
#### Threat detection:

- This model named 

```python 
threat_detection.pt
```

has been made for person tracking.
#### Person and threat detection:

- This model named 

```python 
person_and_threat_detection.pt
```

has been made for person tracking.

### To train
#### face recognition:
- This model has been made for you to give it a dataset, and then automates the training process to get the model.

In order to train it, follow these steps:
1. Give a dataset: For face recognition, we want labels/classes where the photos of individuals are. 

The directory where you should put the classes images is: ./training/face_models/YOLO_data_utils/data/

        ... data/
                ---individual_1:
                    photos
                ---individual_2:
                    photos
                ---individual_3:
                    photos
                ---individual_4:
                ...
                ...
                ...
                ...
                ...

The process is detailed on the README.md inside data folder.

2. Run `main.py` on face_models.

3. Wait until the model finishes the training phase.

4. Now you can access to the model and save it on `/models/` directory