import cv2
import numpy as np

image = cv2.imread("videos/starry_night.jpg")

croppedImage1 = image[0:600, 0:376]

image[0:600, 250:450] = cv2.blur(image[0:600, 250:450], (30, 30))

#mashup = np.concatenate((croppedImage1[0:600, 0:345], smoothing), axis=1)

cv2.imshow("a", image)
#cv2.imshow("b", smoothing)
cv2.imshow("c", croppedImage1)
#cv2.imshow("d", mashup)
cv2.waitKey(0)
