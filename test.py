import cv2
import numpy
from scipy import misc
img = cv2.imread('cell2.jpg')
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


r, c = image.shape
region_counter = 1
R = numpy.zeros((r, c))
for i in range(r - 1):
    for j in range(c - 1):
        if image[i, j] == 1 and image[i, j - 1] == 0 and image[i - 1, j] == 0:
            R[i, j] = region_counter
            region_counter = region_counter + 1
        if image[i, j] == 1 and image[i, j - 1] == 0 and image[i - 1, j] == 1:
            image[i, j] = R[i - 1, j + 1]
        if image[i, j] == 1 and image[i, j - 1] == 1 and image[i - 1, j] == 0:
            R[i, j] = R[i, j - 1]
        if image[i, j] == 1 and image[i, j - 1] == 1 and image[i - 1, j] == 1:
            R[i, j] = R[i - 1, j]
        if image[i, j] == 1 and image[i, j - 1] == 1 and image[i - 1, j] == 0:
            R[i, j] = R[i, j - 1]

cv2.imshow('Image',R)
cv2.waitKey(0)