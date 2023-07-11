from YOLO_data_utils.from_camera import from_camera
from YOLO_data_utils.from_folder_with_photos import from_folder
from face_detection import train
import os

def dataset():
    while True:
        ask = int(input('Which way do you want to create your dataset:\n1. From folder.\n2. From camera.\n==================>(1,2): '))
        if ask == 1:
            from_folder()
            return ask-1
            break
        elif ask ==2:
            class_list = from_camera()
            return [ask-1, class_list]
            break
        else:
            continue

def YAML_config(*args):
    if args[0]:
        output = ''
        for classes in args[1]:
            output = output + '"' + classes + '",'
        
        output = f'[{output[:-1]}]'
        nc = str(len(args[1]))
    else:
        file = os.listdir('data')
        #Number of classes
        nc = str(len(file))

        #classes
        output = ''

        for classes in file:
            output = output + '"' + classes + '",'
        output = f'[{output[:-1]}]'
    #path to data
    path = os.path.join(os.getcwd(), 'YOLO')
    #insert into yaml config
    with open('face_detection.yaml', 'w') as yaml:
        yaml.writelines([
            f'path: {path}\n',
            'train: images/train\n',
            'val: images/val\n',
            f'nc: {nc}\n',
            f'names: {output}'
        ])

def main():
    mode = dataset()
    YAML_config(*mode)
    train()

if __name__ == '__main__':
    main()