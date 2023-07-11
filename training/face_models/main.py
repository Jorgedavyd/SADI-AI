from YOLO_data_utils.from_camera import from_camera
from YOLO_data_utils.from_folder_with_photos import from_folder
from face_detection import train
import os

def dataset():
    while True:
        ask = int(input('Which way do you want to create your dataset:\n1. From camera.\n2. From loaded folders.\n==================>(1,2)'))
        if ask == 1:
            from_camera()
        elif ask ==2:
            from_folder()
        else:
            continue

def get_labels():
    file = os.listdir('data')
    #Number of classes
    nc = str(len(file))

    #classes
    output = ''

    for classes in file:
        output = output + '"' + classes + '",'
    output = f'[{output[:-1]}]'
    #path to data
    path = os.path.join(os.getcwd(), 'data')
    #insert into yaml config
    with open('face_detection.yaml', 'w') as yaml:
        yaml.writelines([
            f'path: {path}',
            'train: images/train',
            'val: images/val',
            f'nc: {nc}',
            f'names: {output}'
        ])

        