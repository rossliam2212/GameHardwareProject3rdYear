import numpy as np
import cv2

# faceClassifierFile = 'lbpcascade_frontalface_improved.xml'
faceClassifierFile = 'haarcascade_frontalface_default.xml'
eyeClassifierFile = 'haarcascade_eye.xml'

faceClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{faceClassifierFile}')
eyeClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{eyeClassifierFile}')

fileName = 'erin.JPG'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = faceClassifier.detectMultiScale(gray, 1.3, 5)
faces = faceClassifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

# When no faces detected, face_classifier returns and empty tuple
if len(faces) == 0:
    print("No Face Found")
else:
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)
        cv2.imshow('img', img)
        # cv2.waitKey(0)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eyeClassifier.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
            cv2.imshow('img', img)
            # cv2.waitKey(0)

    cv2.waitKey(0)

    faceClassifierOutput = faceClassifierFile.split(".")
    eyeClassifierOutput = eyeClassifierFile.split(".")
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/{outputFileName[0]}({faceClassifierOutput[0]}&{eyeClassifierOutput[0]}).png', img)

    cv2.destroyAllWindows()
