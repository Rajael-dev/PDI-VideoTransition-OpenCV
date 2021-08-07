import cv2
import numpy as np
  
image = cv2.imread('starry_night.jpg')
  
# Store height and width of the image
height, width = image.shape[:2]

cv2.imshow("Originalimage", image)

for i in reversed(np.arange(0.0, 1.1, 0.1)):
    print(i)

#quarter_height = height/2


    quarter_width = width-i*width


    T = np.float32([[1, 0, quarter_width], [0, 1, 0]])
  
# We use warpAffine to transform
# the image using the matrix, T
    img_translation = cv2.warpAffine(image, T, (width, height))
  

    cv2.imshow('Translation', img_translation)

    cv2.waitKey(100)  
cv2.destroyAllWindows()