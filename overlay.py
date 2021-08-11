import cv2
import numpy as np

s_img = cv2.imread("videos/starry_night.jpg")
l_img = cv2.imread("videos/starry_night_inversed.jpg")

height, width = s_img.shape[:2]
croppedImage1 = s_img[0:height, int(width/2):width] #this line crops
croppedImage1 = cv2.resize(croppedImage1, (300, 300), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

x_offset=y_offset=0
l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = croppedImage1

# Store height and width of the image

  
#quarter_height, quarter_width = height / 4, width / 4
  
#T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
  
# We use warpAffine to transform
# the image using the matrix, T
#img_translation = cv2.warpAffine(l_img, T, (width, height))
  
cv2.imshow("Originalimage", l_img)
#cv2.imshow('Translation', img_translation)
cv2.waitKey()