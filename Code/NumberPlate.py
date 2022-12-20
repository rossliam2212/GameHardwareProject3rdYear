import numpy as np
import cv2

numberPlateClassifierFile = 'haarcascade_russian_plate_number.xml'
numberPlateClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{numberPlateClassifierFile}')

fileName = 'irishPLate4.jpeg'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numberPlates = numberPlateClassifier.detectMultiScale(gray, 1.05, 7)

if len(numberPlates) == 0:
    print("No number plates detected")
else:
    for (x, y, w, h) in numberPlates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        # cv2.putText(img, "Number plate detected", (x - 20, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)

    # Outputting the image with the detections
    numberPlayerOutput = numberPlateClassifierFile.split('.')
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/numberPlate/{outputFileName[0]}({numberPlayerOutput[0]}).png', img)

    cv2.destroyAllWindows()


