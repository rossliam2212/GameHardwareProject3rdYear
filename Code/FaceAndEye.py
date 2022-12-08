import numpy as np
import cv2

# faceClassifierFile = 'lbpcascade_frontalface_improved.xml'
faceClassifierFile = 'haarcascade_frontalface_default.xml'  # Face Classifier File
eyeClassifierFile = 'haarcascade_eye.xml'  # Eye Classifier File

faceClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{faceClassifierFile}')  # Setting up the Face Classifier
eyeClassifier = cv2.CascadeClassifier(f'cascadeClassifiers/{eyeClassifierFile}')  # Setting up the Eye Classifier

fileName = 'jake.jpg'
img = cv2.imread(f'images/{fileName}')  # Reading in the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converting the input image to gray scale

faces = faceClassifier.detectMultiScale(gray, 1.3, 5)  # Detect faces in the input image

if len(faces) == 0:
    print("No Face Found")
else:
    # Drawing a rectangle around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('img', img)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eyeClassifier.detectMultiScale(roi_gray, 1.2, 4)

        # Drawing a rectangle around the detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
            cv2.imshow('img', img)

    cv2.waitKey(0)  # Waits for any key to be pressed

    # Outputting the image with the detections
    faceClassifierOutput = faceClassifierFile.split(".")
    eyeClassifierOutput = eyeClassifierFile.split(".")
    outputFileName = fileName.split('.')
    cv2.imwrite(f'outputImages/faceAndEyes/{outputFileName[0]}({faceClassifierOutput[0]}&{eyeClassifierOutput[0]}).png',img)

    cv2.destroyAllWindows()  # De allocating any emory usage
