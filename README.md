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

<img width="601" alt="script" src="https://user-images.githubusercontent.com/73957889/208790357-5eb597eb-4541-4407-8777-5aeefe5976bd.png">

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

![InvalidDetectionExample](https://user-images.githubusercontent.com/73957889/208790644-14bae602-f16c-4974-a5b2-df7eb4568354.png)
<br>
*Figure 4: Left: haarcascade_frontalface_default, Right: lbpcascade_frontalface_improved.*

I also believe that, in most cases, because the lbpcascade_frontalface_improved classifier gave a more accurate facial 
detection, it led to a more accurate eye detection, as well as fewer invalid detections. As you can see from Figure 5 
below, the face of the man in the middle on the top image was not detected at all, whereas in the bottom image, his face 
was detected which then led to his eyes also being detected. You can also see from the green boxes, indicating a facial 
detection, in both Figure 4 and Figure 5 for the lbpcascade_frontalface_improved classifier, that they are much smaller 
than the haarcascade_frontalface_default classifier, indicating a more accurate detection of the face.

![MoreAccurateEyeDetection](https://user-images.githubusercontent.com/73957889/208790710-05a2a945-d66c-4714-a4f0-1bbeac17107b.png)
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
*Figure 7: Results from using the lbpcascade_frontalface_improved. classifier.*

As you can see from the results, both samples gave very similar results. Eyes were captured under the glasses in only 
three of the images and this was consistent for both facial classifiers used.

There were a couple minor exceptions though. As you can see from the bottom left image in Figure 6, only the man’s left 
eye detected, whereas in Figure 7, both of his eyes were detected. I believe this was because of the face classifier that 
was used. The lbpcascade_frontalface_improved classifier captured the face more accurately which led to both eyes being 
detected. The eyes of the man in the image in the top left corner in both Figure 6 and Figure 7 were detected. However, 
as you can see in Figure 6, the image contains two cyan boxes around the eyes, whereas in Figure 7, there is a single box 
round each eye, indicating a more accurate detection.


### Face and Smile Detection

<p style="margin-bottom: -1em">Classifiers Used: lbpcascade_frontalface_improved.xml & haarcascade_smile.xml</p>

Pythons Script Used: FaceAndEye.py
![img_12.png](img_12.png)
<br>
*Figure 8: Results from Face and Smile Detection.*

For face and smile detection, the classifiers I used were lbpcascade_frontalface_improved and haarcascade_smile. I decided 
to use lbpcascade_frontalface_improved for the facial detections over the haarcascade_frontalface_default as I thought it 
was the more accurate classifier after completing my face and eye detection samples. The results can be seen in Figure 8, 
where the pink box indicates a facial detection, and the blue box indicates a smile detection.

After I ran the face and smile detection samples, I found the haarcascade_smile classifier to be quite accurate. Almost
all the smiles of the people in the sample images were detected. However, there were some exceptions as in some images, 
the face was detected but the smile was not, even though the person was clearly smiling with their teeth.  As you can see 
from Figure 9 below, both men are smiling with their teeth, but their smile was not detected.

![smileNotDetected](https://user-images.githubusercontent.com/73957889/208790828-b19e9e8c-3c10-4c55-a504-a504465ce4e0.png)
<br>
*Figure 9: Smiles not detected due to facial detection.*

My initial thought was the images were just bad and the classifier could not detect the smiles, however after inspecting 
it further, I noticed that the pink boxes around the face were very small and were cutting off the smile. I realized then 
that because the face was not properly captured, this meant that the smile was not detected at all.

After realizing this, I decided to run another test specifically on the images where smiles were not detected with the 
haarcascade_frontalface_default classifier to see if I would get different results. The results from the first two images 
are shown in Figure 10 below, and it clearly shows that the smiles were detected. As you can see the pink boxes are bigger 
and captured more of the face which in turn allowed for the smiles to be detected.

![smileDetected](https://user-images.githubusercontent.com/73957889/208790862-7bb7ceea-2078-4d0d-a0cb-0720c83cd3df.png)
<br>
*Figure 10: Smiles detected using the haarcascade_frontalface_default classifier.*

However, the haarcascade_frontalface_default classifier along with the haarcascade_smile did not always give accurate 
results. The results from the second two images are shown in Figure 11 below. As you can see from the image on the left, 
only one of the two smiles was detected. I am not including the man in the middles smile in this case as I have already 
shown in Figure 5 that the haarcascade_frontalface_default classifier could not detect his face. From the image on the 
right, you can see that his smile was, in fact, detected, however the image also contains two invalid detections, which 
I believe are due to the facial classifier used.

![smilesDetected1(haarcascade_frontalface_default)](https://user-images.githubusercontent.com/73957889/208790892-127f3b99-5835-4c79-b5e3-31daf3f12f26.png)
<br>
*Figure 11: Inaccurate smile detections using the haarcascade_frontalface_default classifier.*

### Number Plate Detection

<p style="margin-bottom: -1em">Classifiers Used: haarcascade_russian_plate_number.xml</p>

Pythons Script Used: NumberPlate.py, NumberPlateVideo.py
![img_19.png](img_19.png)
<br>
*Figure 12: Results from Detections on Russian Number Plates only.*

<p style="margin-bottom: -1em">Classifiers Used: haarcascade_russian_plate_number.xml</p>

Pythons Script Used: NumberPlate.py
![img_20.png](img_20.png)
<br>
*Figure 13: Results from Detections on various types of Number Plates.*

For number plate detection I used the haarcascade_russian_plate_number classifier. I ran two sample detections with this 
classifier. In the first one, I used only Russian number plates and then in the second one, I used a variety of number 
plates, including Irish, English, and German. The results can be seen in Figure 12 and Figure 13 above, where the yellow 
boxes indicate a number plate detection.

I felt the need to run these two samples as I was originally under the impression that the classifier would only be able 
to detect Russian number plates as the name of the classifier suggested. Upon running the second sample, I found myself 
to be wrong as the classifier worked for almost all kinds of number plates. Even though the classifier worked all number 
plates, I did find that Russian plates were more easily detected. As you can see from all the images in Figure 12, and 
closer in Figure 14, the Russian plates were very accurately detected, even from a distance, in all the sample images 
and the sample video as the yellow boxes were almost perfectly around the number plates.

![3](https://user-images.githubusercontent.com/73957889/208791048-708b0b04-31b8-4b2f-8674-ee97d9ecd9e6.png)
<br>
*Figure 14: Accurate Russian Number Plate Detection.*

As I have already stated, in the second sample, as shown in Figure 13, I ran tests on Irish, English, and German number 
plates, and I was able to get detections on these using the same classifier. Even though, I was able to get detections, 
I don’t believe the classifier was as accurate at detecting these types of plates. As you can see from the images in 
Figure 13, the yellow boxes around the number plates are much bigger as opposed to the ones in Figure 12. Figure 15 
below shows a closer view of a German number plate. As you can see the number plate is being detected, however it does 
not seem to be as accurate, because the number plate is clearly in view, but the yellow box is not perfectly around it.

![golf2(haarcascade_russian_plate_number)](https://user-images.githubusercontent.com/73957889/208790980-1baaa3a6-4df3-406d-89b0-0535400546ea.png)
<br>
*Figure 15: German Number Plate Detection.*

The classifier did not always work with every number plate. As you can see from Figure 16 below, the classifier could not 
detect the Irish number plate, and has two invalid detections indicated by the two yellow boxes. I am not exactly sure 
why this is the case as you can see the number plate is clearly visible. One theory I had as to why it was not detected 
is because this specific number plate is a “3D number plate”, meaning the actual characters on the number plate itself 
stand around three millimetres above the face of the plate. If you look closely at the characters, you can see that they 
are not flat.

![irishPlate1(haarcascade_russian_plate_number)](https://user-images.githubusercontent.com/73957889/208791004-4f545486-1d95-4763-bd6b-a31a2860de76.png)
<br>
*Figure 16: Irish number plate not detected.*

I decided to test my theory out on two images with 3D number plates where the 3D effect on the characters was more prominent. 
The two images I used for this test can be seen in Figure 17 and as you can see the 3D effect is much more visible. 
After running the classifier on these two images, I could not get a detection on either of the number plates. I believe 
my theory was correct that the plates were not detected due to the 3D effect on them.

![3dNumberPlatesNotDetected](https://user-images.githubusercontent.com/73957889/208791106-6cbb1b71-c8a1-459c-b83d-89e40437b7a7.png)
<br>
*Figure 17: 3D number plates not being detected.*

### Car Detection.

<p style="margin-bottom: -1em">Classifiers Used: lbpcascade_car.xml</p>

Pythons Script Used: CarsImage.py, CarsVideo.py

![img_25.png](img_25.png)
<br>
*Figure 18: Results from Car Detections*

For car detection I used the haarcascade_car classifier. The results can be seen in Figure 18, where the yellow boxes 
indicate a car detection.

I found that the classifier was unable to detect cars up close and only able to detect those that were at a distance. I 
am not exactly sure why this is the case; however, my best guess is that this was the way that the classifier was trained. 
As you can see from Figure 19, the cars in these images were not detected properly at all and contained many invalid 
detections. This was something I that tried to fix by playing around with different values for the parameters in the 
detectMultiScale method however I could get a result I was satisfied with.

![img_26.png](img_26.png)
<br>
*Figure 19: Invalid Car Detections.*

The sample images I used of cars that were at a distance worked quite well. As you can see from the images at the top of 
Figure 18 and more closely in Figure 20,  the classifier was able to detect cars that were facing both towards and away 
from the camera. However, the classifier was not always perfect, as not all cars were detected and the images do contain 
several invalid detections.

![img_27.png](img_27.png)
<br>
*Figure 20: Cars detected from a distance.*

## Conclusion

After running all my samples on all my detection methods, I was satisfied with my results. I feel that I was able to get 
accurate detections across all the methods I chose. The classifiers that I used were very accurate at detecting what they 
were trained to detect. I firmly believe that all the classifiers worked best with high resolution images, as I had to 
discard many of the sample images that I gathered due to them being unusable with the classifiers.

I also feel that I could have expanded on the python scripts a bit more to possibly get more accurate detections. Upon 
researching, after I had completed all my detection samples, I found that blurring and dilating an image after converting 
it to gray scale could have helped with more accurate detections particularly with detecting cars. The use different 
detection algorithms, such as the YOLO (You Only Live Once) object detection algorithm, which is a very fast and highly 
accurate algorithm, might also have led me to more accurate detections.

I was intrigued to see if the method of blurring and dilating the image after converting it to gray scale would improve 
my detections, so I decided to run a quick sample test on some of my car sample images. The results can be seen in Figure 
20 below. I was very satisfied with the results, as you can see, a more cars were more accurately detected as opposed to 
the results without using this method in Figure 18 and Figure 20.

<p style="margin-bottom: -1em">Classifiers Used: haarcascade_car.xml</p>

Pythons Script Used: CarsImageImproved.py
![img_28.png](img_28.png)
<br>
*Figure 21: Results from improved car detection test.*

To implement this new method, I first converted the image to grayscale, shown in Figure 22. This was the technique I used 
in all of my detection samples. I then applied Gaussian blur to the image, as shown in Figure 23. By applying Gaussian 
blur to the image, the details of the image were removed as well as the noise being reduced and the image smoothed out. 
Lastly, I dilated the image, as shown in Figure 24. Dilation is a morphological technique that adds pixels to the boundaries 
of objects in an image. I then passed the dilated image to the classifier to get the output image.

![Improvedcars2(GRAY)](https://user-images.githubusercontent.com/73957889/208791466-34727c4c-57ea-4123-bdc3-28b3b558a2aa.png)
<br>
*Figure 22: cars1.jpeg after converting to grayscale.*

![Improvedcars2(BLUR)](https://user-images.githubusercontent.com/73957889/208791485-7b84d7d4-8161-43fd-b193-3274c92ae051.png)
<br>
*Figure 23: cars1.jpeg after applying Gaussian blur on top of grayscale.*

![Improvedcars2(DILATED)](https://user-images.githubusercontent.com/73957889/208791506-dabce516-b779-4975-941e-4a4f2bfe07e9.png)
<br>
*Figure 24: cars1.jpeg after dilation on top of Gaussian blur and grayscale.*

I feel that I have a lot learned with regards to OpenCV, and I feel I have a decent understanding of how object detection 
and how the algorithms behind them work. I am highly interested in expanding my knowledge in this area. I plan on trying 
to expand on the python scripts I have written for this project to try and get more accurate and sophisticated detections. 
I also plan on trying the OpenCV C++ library as well, as C++ is something that I already have an interest in and feel 
comfortable in.

## References:

### Images
- cars.jpeg: https://tinyurl.com/mu66rndw
- cars1.jpeg: https://tinyurl.com/5n7ksa3v
- chevelle70.jpg: https://tinyurl.com/s34jywuc
- chevelle68.jpg: https://tinyurl.com/yn6v8uwz
- chevelle71.jpg: https://tinyurl.com/nh533zmx
- golf1.jpg: https://tinyurl.com/v586avpn
- golf2.jpg: https://tinyurl.com/2p8wmy5v


- b991.jpg:  https://tinyurl.com/49rhv3rk
- post.jpg: https://tinyurl.com/mwcaunm4
- tommy.jpg: https://tinyurl.com/mr3dft8p
- dazed3.jpg: https://tinyurl.com/53w3xkdh
- smileWoman.jpg: https://tinyurl.com/2wn2my9c
- smileMan.jpg: https://tinyurl.com/bddfc6d4
- leo.png: https://tinyurl.com/bddp26cr
- matthew.png: https://tinyurl.com/3y46da5s
- boyle.jpg: https://tinyurl.com/2627nktj
- amy.png: https://tinyurl.com/3c3snykn
- jesse1.png: https://tinyurl.com/yck9jswt
- jake.jpg: https://tinyurl.com/492w6jv8
- steve.jpeg: https://tinyurl.com/yc7e3dp8
- tony.png: https://tinyurl.com/3834ht4k
- ryan.jpeg: https://tinyurl.com/5yswbzm9
- johnny.jpeg: https://tinyurl.com/554xwfup
- johnny1.jpeg: https://tinyurl.com/3p3s3zm5


- numberPlate.jpg: https://tinyurl.com/mrye4ykw
- numberPlate1.jpg: https://tinyurl.com/e9daf5yf
- numberPlate2.jpg: https://tinyurl.com/6rm9ash7
- numberPlate3.jpg: https://tinyurl.com/yansb2r4
- americanPlate.jpg: https://tinyurl.com/bdhst93h
- irishPlate.jpg: https://tinyurl.com/bdz4uanh
- irishPlate1.jpg: https://tinyurl.com/4p6kkpjn
- irishPlate2.jpg: https://tinyurl.com/4vubauzf
- irishPlate3.jpeg: https://tinyurl.com/4bt25pmp
- irishPlate4.jpeg: https://tinyurl.com/csjhcfwp
- englishPlate.jpg: https://tinyurl.com/bdd9ntz7
- englishPlate1.jpeg: https://tinyurl.com/yxnd4e9d

### Videos
- cars.mp4: https://tinyurl.com/mr2upffk
- numberPlateVid.mp4: https://tinyurl.com/msu98beb
- carsOnHighway1.mp4: https://tinyurl.com/ymj3b4dc

### Classifiers

- haarcascade_russian_plate_number.xml: https://tinyurl.com/tkdufr4p
- haarcascade_car.xml: https://tinyurl.com/tkdufr4p
- haarcascade_frontalface_default.xml: https://tinyurl.com/tkdufr4p
- haarcasade_smile.xml: https://tinyurl.com/tkdufr4p
- haarcascade_eye.xml: https://tinyurl.com/tkdufr4p
- lbpcascade_frontalface_improved.xml: https://tinyurl.com/9rzv9c57

