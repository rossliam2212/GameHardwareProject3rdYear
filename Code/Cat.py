import numpy as np
import cv2

catClassifierFile = 'haarcascade_frontalcatface_extended.xml'
catFaceClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{catClassifierFile}')
eyeClassifier = cv2.CascadeClassifier('cascadeClassifiers/haarcascade_eye.xml')

fileName = 'cat.JPEG'
img = cv2.imread(f'images/{fileName}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = catFaceClassifier.detectMultiScale(gray, 1.3, 5)

# When no faces detected, face_classifier returns and empty tuple
if faces == ():
    print("No Cat Face Found")
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

    outputFileName = fileName.split('.')
    catFaceClassifierOutput = catClassifierFile.split(".")
    cv2.imwrite(f'outputImages/{outputFileName[0]}({catFaceClassifierOutput[0]}).png', img)

    cv2.destroyAllWindows()
