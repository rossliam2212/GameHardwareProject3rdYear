import cv2
import numpy as mp

carClassifierFile = 'haarcascade_car.xml'
carClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{carClassifierFile}')

fileName = 'cars.jpeg'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cars = carClassifier.detectMultiScale(gray, 1.4, 2)

if len(cars) == 0:
    print("No cars found")
else:
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', img)

    cv2.waitKey(0)

    # Outputting the image with the detections
    outputFileName = fileName.split('.')  # Splitting the fileName at the '.' (cars.jpeg -> 'cars', 'jpeg)
    carClassifierOutput = carClassifierFile.split(".")
    cv2.imwrite(f'outputImages/{outputFileName[0]}({carClassifierOutput[0]}).png', img)

    cv2.destroyAllWindows()


