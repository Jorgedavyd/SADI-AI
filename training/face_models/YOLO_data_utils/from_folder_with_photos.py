#creating dataset from labeled images on folders.

import os
import cv2

def from_folder():
    try:
        os.makedirs('YOLO/images/train')
        os.makedirs('YOLO/images/val')
        os.makedirs('YOLO/images/test')
        os.makedirs('YOLO/labels/train')
        os.makedirs('YOLO/labels/val')
    except FileExistsError:
        pass

    facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for class_num, class_name in enumerate(os.listdir('data')):
        data_len = len(os.listdir(os.path.join('data', class_name)))
        train_len = round(0.8*data_len)
        for number, file in enumerate(os.listdir(os.path.join('data', class_name))):
            if number<train_len:
                img_name = file[:-4]
                image = cv2.imread(os.path.join('data', class_name, file))
                faces = facedetect.detectMultiScale(image,1.3, 5)
                cv2.imwrite(os.path.join('YOLO/images/train', file), image)
                H,W,_ = image.shape
                with open('YOLO/labels/train/' + img_name + '.txt', 'w') as file:
                    for x,y,w,h in faces: 
                        x = x/W
                        y = y/H
                        w = w/W
                        h= h/H
                        file.write(f'{class_num} {x} {y} {w} {h}\n')
                file.close()
            else:
                img_name = file[:-4]
                image = cv2.imread(os.path.join('data', class_name, file))
                faces = facedetect.detectMultiScale(image,1.3, 5)
                cv2.imwrite(os.path.join('YOLO/images/val', file), image)
                H,W,_ = image.shape
                with open('YOLO/labels/val/' + img_name + '.txt', 'w') as file:
                    for x,y,w,h in faces:  
                        x = x/W
                        y = y/H
                        w = w/W
                        h= h/H
                        file.write(f'{class_num} {x} {y} {w} {h}\n')
                file.close()
        

