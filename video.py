import cv2 as cv2
import operator
import os


video="video/video1.mp4"
cascade="./haarcascade_frontalface_alt2.xml"
img_non_classe='img_non_classe'

if not os.path.exists(video):
    print("Le fichier video n'existe pas", video)
    quit()

if not os.path.exists(cascade):
    print("Le fichier cascade n'existe pas", cascade)
    quit()

face_cascade=cv2.CascadeClassifier(cascade)
cap=cv2.VideoCapture(video)

if not os.path.isdir(img_non_classe):
    os.mkdir(img_non_classe)
    
id=0
while True:
    ret, frame=cap.read()
    if ret is False:
        break
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4, minSize=(50, 50))
    for x, y, w, h in face:
        cv2.imwrite("{}/p-{:d}.png".format(img_non_classe, id), frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        id+=1
    cv2.imshow('video', frame)
    key=cv2.waitKey(1)&0xFF
    if key==ord('q'):
        break
    if key==ord('a'):
        for cpt in range(100):
            ret, frame=cap.read()
    for cpt in range(4):
        ret, frame=cap.read()

cap.release()
cv2.destroyAllWindows()