import cv2
import numpy as np

# main
img = cv2.imread('starry_night.jpg', 1)

print(img.shape)

print("Altura(height): %d pixels" % (img.shape[0]))
print("Largura(width): %d pixels" % (img.shape[1]))
print("Canais(Channels): %d " % (img.shape[2]))

cv2.imshow('College20 -Original', img)


#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))
#Moon = img[50:500,50:500] até hj procurando aquela lua que brilha lá no céu
favoritos = img[0:600,0:376]
img[0:600, 0:376] = favoritos
#img[100:550,5:455] = Moon


cv2.imshow('College20 - Mesclado', img)
cv2.waitKey(0)
cv2.imshow('College20 - Corte realizado',favoritos)


cv2.imwrite('College20 - Merged.jpg',img)

W = cv2.waitKey(0) & 0xFF
if W == 27:
   cv2.destroyAllWindows()