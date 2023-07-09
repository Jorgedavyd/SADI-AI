#app
import cv2

#Importing camera frames
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)
cap.set(cv2.CAP_PROP_FPS, 30)


while True:
    
    #Import frame
    _, frame = cap.read()
    
    #pasar a RGB
    input_= frame[:, :, [2, 1, 0]]    
    
    
    ##inferencia

    #Mostrar en pantalla
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()