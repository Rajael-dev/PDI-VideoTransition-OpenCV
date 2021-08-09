import cv2
import numpy as np
from numpy.lib.type_check import imag
  
image = cv2.imread("videos/starry_night.jpg") #note: image needs to be in the opencv format
#height, width, channels = image.shape
height, width = image.shape[:2]
croppedImage1 = image[0:height, int(width/2):width] #this line crops
croppedImage2 = image[0:height, 0:int(width/2)] #this line crops

quarter_width1 = width-1.7*width
T1 = np.float32([[1, 0, -quarter_width1], [0, 1, 0]])
img_translation1 = cv2.warpAffine(croppedImage1, T1, (width, height))

quarter_width2 = width-1.2*width
T2 = np.float32([[1, 0, quarter_width2], [0, 1, 0]])
img_translation2 = cv2.warpAffine(croppedImage2, T2, (width, height))

mashup = cv2.hconcat([img_translation2, img_translation1])
#mashup = cv2.resize(mashup, (752, 600), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

cv2.imshow("a", img_translation1)
cv2.imshow("b", img_translation2)
cv2.imshow("c", mashup)
cv2.waitKey(0)
