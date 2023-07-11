import cv2
import os

#Setting up the camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224) # insert the width at which the model was trained 

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)# insert the height at which the model was trained (usually same as width) 

cap.set(cv2.CAP_PROP_FPS, 30) # You can vary the frames based on the dataset len you want to achieve

facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Creates file with the class and labels

def WriteLabel(frameNr, classes, frame, train=True):
    if train:
        path = '/labels/train'
    else:        
        path = '/labels/val'
    faces = facedetect.detectMultiScale(frame,1.3, 5)
    with open(path + frameNr + '.txt', 'w') as file:
        for x,y,w,h in faces:    
            file.write(f'{classes} {x} {y} {w} {h}\n')
    file.close()


classes = int(input('classes: '))


try:
    os.makedir('images/train')
    os.makedir('images/val')
    os.makedir('images/test')
    os.makedir('labels/train')
    os.makedir('labels/val')
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
    while (True):

        success, frame = cap.read()
        
        cv2.imshow('frame', frame)
        
        if success:
            cv2.imwrite(os.path.join(path, str(frameNr)), frame)
            WriteLabel(str(frameNr), classes, frame, train = train)

        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frameNr = frameNr+1

    cap.release()

def train_data():
    path = 'images/train'
    for i in range(classes):
        frameNr = folder_scratch(path)
        input('Press enter for next step')
        capture(path = path, frameNr = frameNr, classes = str(i), train=True)

def val_data():
    path = 'images/val'
    for i in range(classes):
        frameNr = folder_scratch(path)
        input('Press enter for next step')
        capture(path = path, frameNr = frameNr, classes = str(i), train=False)


def test_data():
    frameNr = folder_scratch(f'/images')
    path = 'images/test'
    while (True):

        success, frame = cap.read()
        
        cv2.imshow('frame', frame)
        
        if success:
            cv2.imwrite(os.path.join(path, str(frameNr)), frame)

        else:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frameNr = frameNr+1

    cap.release()



while True:
    a = int(input('1. train\n2. val\n 3.test\ninput:'))
    if a == 1:
        train_data()
    elif a == 2:
        val_data()
    elif a == 3:
        test_data()
    else:
        print('Try again\n\n\n\n')
        continue
