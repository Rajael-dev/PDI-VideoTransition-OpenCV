import cv2
import numpy as np

# Carrega os vídeos
cap1 = cv2.VideoCapture('videos/Bees.mp4')
fps1 = cap1.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
duration1 = frame_count1/fps1
print('----------video 1----------')
print('fps = ' + str(fps1))
print('number of frames = ' + str(frame_count1))
print('duration (S) = ' + str(duration1))
print()

cap2 = cv2.VideoCapture('videos/Sand.mp4')
fps2 = cap2.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
duration2 = frame_count2/fps2
print('----------video 2----------')
print('fps = ' + str(fps2))
print('number of frames = ' + str(frame_count2))
print('duration (S) = ' + str(duration2))

# Checa se os vídeos foram econtrados com sucesso
if (cap1.isOpened() == False or cap2.isOpened() == False): 
  print("Error opening video stream or file")

current_frame1 = 0
current_frame2 = 0

# Valor inicial da posição dos vídeos na janela
i = 1

# Velocidade do efeito de transição
# Quanto mais próximo de 1 mais rápido e quanto mais próximo de 0 mais lento
# A velocidade deve ser entre: 0.1 (muito rápido) e 0.01 (muito lento)
# Valor recomendado: 0.02
vel = 0.02

transition_point = (round(duration1)/vel)/round(duration1)
transition_point = round(transition_point)

# Lê até que os vídeos estejam completos
while(cap2.isOpened()):
    ret1, frame1 = cap1.read()
    #print(current_frame)
    
    if current_frame2 <= frame_count2:
        if current_frame1 <= frame_count1-transition_point:
            frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

            cv2.imshow("Slide Right to Left", frame1)
            cv2.waitKey(10)

            final_frame = frame1
            current_frame1 = current_frame1 + 1
   
        else:
            if ret1 == True:
                frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                cv2.imshow("Slide Right to Left", frame1)
                #current_frame = current_frame + 1
            else:
                frame1 = cv2.resize(final_frame, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                cv2.imshow("Slide Right to Left", final_frame)
            
            ret2, frame2 = cap2.read()

            if ret2 == True:
                frame2 = cv2.resize(frame2, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

                height, width = frame2.shape[:2]

                width_variation = width-i*width
                T = np.float32([[1, 0, width_variation], [0, 1, 0]])

                # Concatena os 2 vídeos
                mashup = np.concatenate((frame1, frame2), axis=1)

                # Translada os vídeos
                frame_translation = cv2.warpAffine(mashup, T, (width, height))

                # Exibe os vídeos
                cv2.imshow('Slide Right to Left', frame_translation)
                cv2.waitKey(10)  

                # Altera a posição do frame a cada ciclo do laço
                i = i + vel

                # Verifica se o vídeo 2 está todo na janela e para a translação
                if i >= 2:
                    i=2
                    vel = 0

                current_frame2 = current_frame2 + 1
            else:
                break

        # Define a tecla Q para encerrar a aplicação
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Quando tudo estiver finalizado, solta as capturas de vídeo
cap1.release()
cap2.release()
# Fecha todas a janelas
cv2.destroyAllWindows()