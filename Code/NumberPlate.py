import numpy as np
import cv2

numberPlateClassifierFile = 'haarcascade_russian_plate_number.xml'
numberPlateClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{numberPlateClassifierFile}')

fileName = 'numberPlate.jpg'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numberPlates = numberPlateClassifier.detectMultiScale(gray, 1.05, 7)

if len(numberPlates) == 0:
    print("No number plates detected")
else:
    for (x, y, w, h) in numberPlates:
        # draw a rectangle around the number plate
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # cv2.putText(img, "Number plate detected", (x - 20, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)

        # extract the number plate from the grayscale image
        # numberPlate = gray[y:y + h, x:x + w]

        cv2.imshow('Image', img)
        # cv2.imshow('Plates', numberPlate)
        cv2.waitKey(0)

        numberPlayerOutput = numberPlateClassifierFile.split('.')
        outputFileName = fileName.split('.')
        cv2.imwrite(f'outputImages/{outputFileName[0]}({numberPlayerOutput[0]}).png', img)

        cv2.destroyAllWindows()

