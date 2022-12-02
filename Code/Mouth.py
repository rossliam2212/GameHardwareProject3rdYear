import numpy as np
import cv2

mouthClassifierFile = 'haarcascade_mcs_mouth.xml'

mouthClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{mouthClassifierFile}')

fileName = 'budapest.JPG'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mouths = mouthClassifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))

if len(mouths) == 0:
    print("No Face Found")
else:
    for (x, y, w, h) in mouths:
        cv2.rectangle(img, (x, y), (x + w, y + h), (127, 0, 255), 2)
        cv2.imshow('img', img)

    cv2.waitKey(0)

    mouthClassifierOutput = mouthClassifierFile.split(".")
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/{outputFileName[0]}-{mouthClassifierOutput[0]}.png', img)

    cv2.destroyAllWindows()
