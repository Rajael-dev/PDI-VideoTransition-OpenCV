import cv2
import numpy as np

cap1 = cv2.VideoCapture('videos/Bees.mp4')
fps1 = cap1.get(cv2.CAP_PROP_FPS)
frame_count1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
duration1 = frame_count1/fps1
# print('----------video 1----------')
# print('fps = ' + str(fps1))
# print('number of frames = ' + str(frame_count1))
# print('duration (S) = ' + str(duration1))
# print()

cap2 = cv2.VideoCapture('videos/Sand.mp4')
fps2 = cap2.get(cv2.CAP_PROP_FPS)
frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
duration2 = frame_count2/fps2
# print('----------video 2----------')
# print('fps = ' + str(fps2))
# print('number of frames = ' + str(frame_count2))
# print('duration (S) = ' + str(duration2))

if (cap1.isOpened() == False or cap2.isOpened() == False): 
  print("Error opening video stream or file")

current_frame1 = 0
current_frame2 = 0

# Velocidade do efeito de transição
# A velocidade deve ser entre: 30 (mais rápido) e 3 (mais lento)
# Valor recomendado: 10
print()
print('Escolha a velocidade')
print('Deve ser um valor entre 3 (min) e 30 (máx): ')
vel = input()
vel = float(vel)

if vel > 30 or vel < 3:
    print('Valor para velocidade inválido!')
    print()
    exit()

transition_point = round(357/vel)+1

j = 0

while(cap2.isOpened()):
    ret1, frame1 = cap1.read()
    
    if current_frame2 <= frame_count2:
        if current_frame1 <= frame_count1-transition_point:
            frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

            cv2.imshow("Horizontal Split", frame1)
            cv2.waitKey(10)

            final_frame = frame1
            current_frame1 = current_frame1 + 1
   
        else:
            if ret1 == True:
                frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                cv2.imshow("Horizontal Split", frame1)

            else:
                frame1 = cv2.resize(final_frame, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                cv2.imshow("Horizontal Split", final_frame)
            
            ret2, frame2 = cap2.read()

            if ret2 == True:
                frame2 = cv2.resize(frame2, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

                height, width = frame2.shape[:2]

                if j <= width/2:
                    croppedImage1 = frame1[0:height, int(width/2):int(width-j)]
                    croppedImage2 = frame1[0:height, int(0+j):int(width/2)]

                    frame2[0:0+croppedImage1.shape[0], int(j+width/2):int(j+width)] = croppedImage1
                    frame2[0:0+croppedImage2.shape[0], 0:0+croppedImage2.shape[1]] = croppedImage2

                    j = j + vel

                cv2.imshow("Horizontal Split", frame2)
                cv2.waitKey(10)

                current_frame2 = current_frame2 + 1
            else:
                break

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap1.release()
cap2.release()
cv2.destroyAllWindows()