import os
import cv2

try:
    os.makedirs('images/train')
    os.makedirs('images/val')
    os.makedirs('images/test')
    os.makedirs('labels/train')
    os.makedirs('labels/val')
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
            cv2.imwrite(os.path.join('images/train', file), image)
            with open('labels/train/' + img_name + '.txt', 'w') as file:
                for x,y,w,h in faces:    
                    file.write(f'{class_num} {x} {y} {w} {h}\n')
            file.close()
        else:
            img_name = file[:-4]
            image = cv2.imread(os.path.join('data', class_name, file))
            faces = facedetect.detectMultiScale(image,1.3, 5)
            cv2.imwrite(os.path.join('images/val', file), image)
            with open('labels/val/' + img_name + '.txt', 'w') as file:
                for x,y,w,h in faces:    
                    file.write(f'{class_num} {x} {y} {w} {h}\n')
            file.close()



