#creating dataset from camera utilities

import cv2
import os

def setup_camera():
    #Setting up the camera
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # insert the width at which the model was trained 

    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)# insert the height at which the model was trained (usually same as width) 

    cap.set(cv2.CAP_PROP_FPS, 20) # You can vary the frames based on the dataset len you want to achieve
    return cap

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Creates file with the class and labels

def WriteLabel(frameNr, classes, frame, train=True):
    if train:
        path = 'YOLO/labels/train/'
    else:        
        path = 'YOLO/labels/val/'
    faces = facedetect.detectMultiScale(frame,1.3, 5)
    H,W,_ = frame.shape
    with open(path + frameNr + '.txt', 'w') as file:
        for x,y,w,h in faces:
            x = x/W
            y = y/H
            w = w/W
            h= h/H
            file.write(f'{classes} {x} {y} {w} {h}\n')
    file.close()


classes = int(input('Individuals: '))




try:
    os.makedirs('YOLO/images/train')
    os.makedirs('YOLO/images/val')
    os.makedirs('YOLO/images/test')
    os.makedirs('YOLO/labels/train')
    os.makedirs('YOLO/labels/val')
except FileExistsError:
    pass

def folder_scratch(carpeta):
    archivos = os.listdir(carpeta)
    numeros = []
    for archivo in archivos:
        nombre, extension = os.path.splitext(archivo)
        try:
            numero = int(nombre)
            numeros.append(numero)
        except ValueError:
            pass

    if numeros:
        numero_mas_alto = max(numeros)
        return numero_mas_alto + 1
    else:
        return 0    
    

#Capturing the dataset
def capture(path, frameNr, classes, train = True):
    cap = setup_camera()

    while (True):

        success, frame = cap.read()
        
        
        if success:
            cv2.imshow('frame', frame)
            cv2.imwrite(os.path.join(path, str(frameNr)+'.jpg'), frame)
            WriteLabel(str(frameNr), classes, frame, train = train)

        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frameNr = frameNr+1

    cap.release()
    cv2.destroyAllWindows()

def train_data(classes):
    path = 'YOLO/images/train/'
    frameNr = folder_scratch(path)
    input('Press enter for next step')
    capture(path = path, frameNr = frameNr, classes = str(classes), train=True)

def val_data(classes):
    path = 'YOLO/images/val/'
    frameNr = folder_scratch(path)
    input('Press enter for next step')
    capture(path = path, frameNr = frameNr, classes = str(classes), train=False)


def test_data():
    cap = setup_camera()
    path = 'YOLO/images/test/'
    frameNr = folder_scratch(path)
    while (True):

        success, frame = cap.read()
        
        cv2.imshow('frame', frame)
        
        if success:
            cv2.imwrite(os.path.join(path, str(frameNr)+'.jpg'), frame)

        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frameNr = frameNr+1

    cap.release()
    cv2.destroyAllWindows()


def from_camera():
    class_list = []
    for i in range(classes):
        class_list.append(input(f'Insert the number {i+1} class individual:'))

    for number, class_ in enumerate(class_list):
        while True:    
            a = input(f'\nCreating dataset for individual {class_}\n1. train\n2. val\n 3.test\n============> (0 next individual, q quit dataset creation): ')
            if a == '1':
                train_data(number)
            elif a == '2':
                val_data(number)
            elif a == '3':
                test_data()
            elif a == '0' or a =='q':
                break
            else:
                print('Try again\n')
                continue
        if a == 'q':
            break
    return class_list