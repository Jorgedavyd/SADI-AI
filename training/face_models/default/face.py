import cv2
#Setting up the camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # insert the width at which the model was trained 

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)# insert the height at which the model was trained (usually same as width) 

cap.set(cv2.CAP_PROP_FPS, 30) # Y

human_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, 1.9, 1)
    
    # Display the resulting frame
    for (x,y,w,h) in humans:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         
         

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()