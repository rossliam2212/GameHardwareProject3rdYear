import numpy as np
import cv2

fullBodyClassifierFile = 'haarcascade_fullbody.xml'

fullBodyClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{fullBodyClassifierFile}')

fileName = 'b992.JPG'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

bodies = fullBodyClassifier.detectMultiScale(gray, 1.2, 3)

if len(bodies) == 0:
    print("No bodies found")
else:
    for (x, y, w, h) in bodies:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imshow('Bodies', img)

    cv2.waitKey(0)

    fullBodyOutput = fullBodyClassifierFile.split(".")
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/{outputFileName[0]}({fullBodyOutput[0]}).png', img)

    cv2.destroyAllWindows()
