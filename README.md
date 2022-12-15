# Game Hardware 3rd Year Project

# Game Hardware 3

## Introduction

This aim of this project was to use the OpenCV python package along with trained algorithms to detect specific objects in 
images and videos. 

For my project, the detection methods I chose were, face and eye detection, face and smile detection, 
number plate detection and car detection. I chose these detection methods as I found them to be the most interesting and 
I felt that I could generate a lot of samples. I sourced various images and videos online to use for my project, which 
can all be found in the Code/images and Code/videos folders. I have also included links to the original sources for all 
these images and videos below. 

The python package that I used in this project was OpenCV. OpenCV is an open source, cross platform, library of 
programming functions aimed at real time computer vision. 

All the python scripts I created 
for this project all followed a similar manner. Here is an example of the script I used for Face and Eye Detection.

![img_4.png](img_4.png)

*Figure 1: Python script used for detecting faces and eyes in PyCharm.*

## Tech Stack
OS:
- macOS Monterey - Version 12,4

Python:
- Version: 3.10

Packages:
- OpenCV - Version: 4.6.0.66
- Numpy - Version: 1.23.5

Environment:
- PyCharm IDE - Version 2022.2.4

Classifiers:
- haarcascade_russian_plate_number.xml
- haarcascade_car.xml 
- haarcascade_frontalface_default.xml 
- lbpcascade_frontalface_improved.xml 
- haarcasade_smile.xml 
- haarcascade_eye.xml

Python Source Files:
- CarsImage.py
- CarsImageImproved.py
- CarsVideo.py
- FaceAndEye.py
- Smile.py
- NumberPlate.py
- NumberPlateVideo.py

## Detections
### Face and Eye Detection

<p style="margin-bottom: -1em">Classifiers Used: haarcascade_frontalface_default.xml & haarcascade_eye.xml</p>

Pythons Script Used: FaceAndEye.py
![img_5.png](img_5.png)
<br>
*Figure 2: Results from Face and Eye Detection Sample 1.*

<p style="margin-bottom: -1em">Classifiers Used:lbpcascade_frontalface_improved.xml & haarcascade_eye.xml</p>

Pythons Script Used: FaceAndEye.py
![img_6.png](img_6.png)
<br>
*Figure 3: Results from Face and Eye Detection Sample 2.*


For face and eye detection, I ran two detection samples with two different face classifiers on each of the sample images 
that I gathered. In the first sample, I used the haarcascade_frontalface_default classifier and in the second sample I 
used the lbpcascade_frontalface_improved classifier. I used the haarcascade_eye classifier on both samples. The green 
boxes indicate a facial detection, and the cyan boxes indicate an eye detection.

My goal was to see which classifier was more accurate for facial detection and what effect that had on detecting the eyes. 
From Figure 2 and Figure 3 above, you can see that both classifiers gave very similar results in most cases. However, I 
do think that the lbpcascade_frontalface_improved classifier was more accurate in detecting faces and it gave off fewer 
invalid detections. As you can see from Figure 4 below, the image on the left contains two invalid facial detections 
around the upper chest area, indicated by the arrows, whereas the image on the right does not.

![img_7.png](img_7.png)
<br>
*Figure 4: Left: haarcascade_frontalface_default, Right: lbpcascade_frontalface_improved.*

I also believe that, in most cases, because the lbpcascade_frontalface_improved classifier gave a more accurate facial 
detection, it led to a more accurate eye detection, as well as fewer invalid detections. As you can see from Figure 5 
below, the face of the man in the middle on the top image was not detected at all, whereas in the bottom image, his face 
was detected which then led to his eyes also being detected. You can also see from the green boxes, indicating a facial 
detection, in both Figure 4 and Figure 5 for the lbpcascade_frontalface_improved classifier, that they are much smaller 
than the haarcascade_frontalface_default classifier, indicating a more accurate detection of the face.

![img_9.png](img_9.png)
<br>
*Figure 5: Top: haarcascade_frontalface_default, Bottom: lbpcascade_frontalface_improved.*

I also ran another two smaller detection samples, specifically on images of people that were wearing glasses. I used both 
face classifiers along with the eye classifier for these samples as firstly, I wanted to see if the eye classifier was 
able to detect the eyes underneath the glasses and if so, would the face classifier used have any effect. The results can 
be seen in Figure 6 and Figure 7 below.

![img_10.png](img_10.png)
<br>
*Figure 6: Results from using the haarcascade_frontalface_default classifier.*

![img_11.png](img_11.png)
<br>
*Figure 6: Results from using the lbpcascade_frontalface_improved. classifier.*

As you can see from the results, both samples gave very similar results. Eyes were captured under the glasses in only 
three of the images and this was consistent for both facial classifiers used.

There were a couple minor exceptions though. As you can see from the bottom left image in Figure 6, only the man’s left 
eye detected, whereas in Figure 7, both of his eyes were detected. I believe this was because of the face classifier that 
was used. The lbpcascade_frontalface_improved classifier captured the face more accurately which led to both eyes being 
detected. The eyes of the man in the image in the top left corner in both Figure 6 and Figure 7 were detected. However, 
as you can see in Figure 6, the image contains two cyan boxes around the eyes, whereas in Figure 7, there is a single box 
around each eye, indicating a more accurate detection.


### Face and Smile Detection

### Number Plate Detection

### Car Detection

## Conclusion

## References:
