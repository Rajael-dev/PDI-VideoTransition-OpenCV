import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap1 = cv2.VideoCapture('videos/Bees.mp4')
cap2 = cv2.VideoCapture('videos/Sand.mp4')

# Check if camera opened successfully
if (cap1.isOpened() == False): 
  print("Error opening video stream or file")

i = 2
vel = 0.02

# Read until video is completed
while(cap1.isOpened()):
  # Capture frame-by-frame
  ret, frame1 = cap1.read()
  frame1 = cv2.resize(frame1, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
  ret, frame2 = cap2.read()
  frame2 = cv2.resize(frame2, (540, 380), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

  height, width = frame1.shape[:2]

  if ret == True:
    # Display the resulting frame
    #quarter_height = height/2
    width_variation = width-i*width
    T = np.float32([[1, 0, width_variation], [0, 1, 0]])
  
    # We use warpAffine to transform
    # the image using the matrix, T
    mashup = np.concatenate((frame2, frame1), axis=1)

    img_translation = cv2.warpAffine(mashup, T, (width, height))

    cv2.imshow('Translation', img_translation)
    cv2.waitKey(25)  

    i = i - vel

    if i <= 1:
      vel = 0

    if cv2.waitKey(25) & 0xFF == ord('q'):
          break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap1.release()

# Closes all the frames
cv2.destroyAllWindows()