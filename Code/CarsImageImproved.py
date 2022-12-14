import cv2
import numpy as np

carClassifierFile = 'haarcascade_car.xml'
carClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{carClassifierFile}')

fileName = 'cars1.jpeg'
img = cv2.imread(f'images/{fileName}')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
dilated = cv2.dilate(blur, np.ones((3, 3)))

cars = carClassifier.detectMultiScale(gray, 1.1, 2)

if len(cars) == 0:
    print("No cars found")
else:
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Cars', img)

    cv2.waitKey(0)

    # Outputting the image with the detections
    outputFileName = fileName.split('.')
    carClassifierOutput = carClassifierFile.split(".")
    cv2.imwrite(f'outputImages/cars/Improved{outputFileName[0]}({carClassifierOutput[0]}).png', img)

    cv2.destroyAllWindows()


