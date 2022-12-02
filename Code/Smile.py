import numpy as np
import cv2

faceClassifierFile = 'lbpcascade_frontalface_improved.xml'
smileClassifierFile = 'haarcascade_smile.xml'

faceClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{faceClassifierFile}')
smileClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{smileClassifierFile}')

fileName = 'budapest.JPG'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

if len(faces) == 0:
    print("No faces found")
else:
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)
        cv2.imshow('img', img)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        smiles = smileClassifier.detectMultiScale(roi_gray)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (255, 0, 0), 2)
            cv2.imshow('img', img)

    cv2.waitKey(0)

    faceClassifierOutput = faceClassifierFile.split(".")
    smileClassifierOutput = smileClassifierFile.split(".")
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/{outputFileName[0]}({faceClassifierOutput[0]}&{smileClassifierOutput[0]}).png', img)
    cv2.destroyAllWindows()


