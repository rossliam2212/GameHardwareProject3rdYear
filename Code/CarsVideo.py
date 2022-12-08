import cv2
import time
import numpy as np

carClassifierFile = 'haarcascade_car.xml'
carClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{carClassifierFile}')

fileName = 'carsOnHighway.mp4'
cap = cv2.VideoCapture(f'videos/{fileName}')

while cap.isOpened():

    time.sleep(.05)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = carClassifier.detectMultiScale(gray, 1.1, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
