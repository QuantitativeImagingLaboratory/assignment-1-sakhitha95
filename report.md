

Nearest Neighbor:

nearest_neighbor(self, image, fx, fy):

1. image, resize scale along x axis (fx) and resize scale along y axis(fy) are taken as input parameters to the nearest_neigbour function.
2. The number of pixels that should be present along the x axis is calculated as (w * int(fx)). where w is the number of pixels along x axis in the original image.
3. The number of pixels that should be present along the y axis is calculated as (h * int(fy)). where h is the number of pixels along y axis in the original image.
4. Blank image is created with new scale is created.
5. Calculated the nearest neigbor pixel in original image(int(i / int(fx)), int(j / int(fy))) to the pixel in new image.
6. Assign nearest neigbor pixel intensity value to the pixel in the new image
7. Repeated for all the pixels in the new image.
8. Thus the image is resized using nearest neighbor and the function returns the resized image.

Linear interpolation:

linear_interpolation(self, pt1, pt2, unknown):

1. Two points whose intensity values are known and the point whose intensity value is not known are passed as the input parameters to the function.
2. The intensity value of that