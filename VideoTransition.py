import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('videos\Bees.mp4')

# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Error opening video stream or file")

#height, width = cap.shape[:2]
vel = 0.05
#width  = cap.get(3)  # float `width`
#height = cap.get(4)  # float `height`

#print('width, height:', width, height)
i = 1
vel = 0.01
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  frame = cv2.resize(frame, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
  height, width = frame.shape[:2]

  if ret == True:
    # Display the resulting frame
    #quarter_height = height/2
    quarter_width = width-i*width
    T = np.float32([[1, 0, quarter_width], [0, 1, 0]])
  
    # We use warpAffine to transform
    # the image using the matrix, T
    img_translation = cv2.warpAffine(frame, T, (width, height))
  
    cv2.imshow('Translation', img_translation)
    cv2.waitKey(25)  
    
    i = i - vel

    if cv2.waitKey(25) & 0xFF == ord('q'):
          break

  # Break the loop
  else: 
    break


# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()