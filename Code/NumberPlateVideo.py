import cv2
import time
import numpy as np

numberPlateClassifierFile = 'haarcascade_russian_plate_number.xml'
numberPlateClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{numberPlateClassifierFile}')

fileName = ''
cap = cv2.VideoCapture(f'videos/{fileName}')

while cap.isOpened():
    time.sleep(.05)

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = numberPlateClassifier.detectMultiScale(gray, 1.4, 2)
    # Extract bounding boxes for any bodies identified
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Number Plates', frame)

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()
