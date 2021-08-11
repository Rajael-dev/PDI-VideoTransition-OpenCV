import cv2
import numpy as np
from numpy.lib.type_check import imag
  
image = cv2.imread("videos/starry_night.jpg") 

j = 0

height, width = image.shape[:2]

x_offset1=376
y_offset1=0

x_offset2=0
y_offset2=0

vel = 4

while j <= 400:
    img = cv2.imread("videos/colegio.jpg") 
    croppedImage1 = image[0:height, int(width/2):width-j]
    croppedImage2 = image[0:height, 0+j:int(width/2)]

    img[y_offset1:y_offset1+croppedImage1.shape[0], x_offset1:x_offset1+croppedImage1.shape[1]] = croppedImage1
    img[y_offset2:y_offset2+croppedImage2.shape[0], x_offset2:x_offset2+croppedImage2.shape[1]] = croppedImage2

    cv2.imshow("c", img)
    cv2.waitKey(10)

    j = j + vel
    x_offset1 = x_offset1 + vel