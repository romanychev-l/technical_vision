import cv2
import numpy as np


img = np.random.randint(222, size=(100, 100, 3))
gen = np.array(img, dtype=np.uint8)

#cv2.imshow('i', gen)
cv2.imshow('j', gen.transpose())
cv2.waitKey(0)
cv2.destroyWindow('i')

#TODO