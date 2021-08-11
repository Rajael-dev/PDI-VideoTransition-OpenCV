import cv2
import numpy as np
import decimal

vel = 10
arred = 357/vel
print(arred)
d = decimal.Decimal(arred)
print(d.as_tuple().digits[-1])