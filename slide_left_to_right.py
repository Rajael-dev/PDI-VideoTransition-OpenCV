import cv2
import numpy as np

def slide_left_to_right():
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

    i = 2

    # Velocidade do efeito de transição
    # A velocidade deve ser entre: 0.1 (mais rápido) e 0.01 (mais lento)
    # Valor recomendado: 0.02
    print()
    print('Escolha a velocidade')
    print('Deve ser um valor entre 0.01 (min) e 0.1 (máx): ')
    vel = input()
    vel = float(vel)

    if vel > 0.1 or vel < 0.01:
        print('Valor para velocidade inválido!')
        print()
        exit()

    print()
    print('Escolha o tipo da borda')
    print('0 - Borda sólida')
    print('1 - Borda suave')
    edge_type = input()
    edge_type = int(edge_type)

    if edge_type != 0 and edge_type != 1:
        print('Tipo de borda inválido!')
        print()
        exit()

    transition_point = (round(duration1)/vel)/round(duration1)
    transition_point = round(transition_point)

    while(cap2.isOpened()):
        ret1, frame1 = cap1.read()
        
        if current_frame2 <= frame_count2:
            if current_frame1 <= frame_count1-transition_point:
                frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

                cv2.imshow("Slide Left to Right", frame1)
                cv2.waitKey(10)

                final_frame = frame1
                current_frame1 = current_frame1 + 1
    
            else:
                if ret1 == True:
                    frame1 = cv2.resize(frame1, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                    cv2.imshow("Slide Left to Right", frame1)

                else:
                    frame1 = cv2.resize(final_frame, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
                    cv2.imshow("Slide Left to Right", final_frame)
                
                ret2, frame2 = cap2.read()

                if ret2 == True:
                    frame2 = cv2.resize(frame2, (720, 480), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)

                    height, width = frame2.shape[:2]

                    width_variation = width-i*width
                    T = np.float32([[1, 0, width_variation], [0, 1, 0]])

                    mashup = np.concatenate((frame2, frame1), axis=1)

                    if edge_type == 1 and vel != 0:
                        mashup[0:480, 710:730] = cv2.blur(mashup[0:480, 710:730], (20, 20))

                    frame_translation = cv2.warpAffine(mashup, T, (width, height))

                    cv2.imshow('Slide Left to Right', frame_translation)
                    cv2.waitKey(10)  

                    i = i - vel

                    if i <= 1:
                        i=1
                        vel = 0

                    current_frame2 = current_frame2 + 1
                else:
                    break

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap1.release()
    cap2.release()
    cv2.destroyAllWindows()