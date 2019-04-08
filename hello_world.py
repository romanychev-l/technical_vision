import cv2 as cv
import numpy as np

# Load an color image in grayscale
img = cv.imread('1.png',0)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
print('done')

print("Hello world")