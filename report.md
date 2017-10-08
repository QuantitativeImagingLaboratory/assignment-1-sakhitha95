

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
2. The intensity value of the unknown point is calculated using this i1*((x2-x3)/(x2-x1)) + i2*((x3-x1)/(x2-x3)).
3. The intensity value of the unknown point is returned.

Bilinear Interpolation:

bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):

1. Four points whose intensity values are known and the point whose intensity value is not known are passed as the input parameters to the function.
2. Two points which are on same line are passed to the linear interpolation method so that the intensity at point whose x value is same as that of other 2 points and y value is that of unknown.
3. The same is repeated for other two points.
4. The two points and their intensities which you got from the previous two steps are passed in to linear interpolation method to find the intensity of the unkown point.
5. The intensity of the unkown point is returned.

Interpolation using Bilinear:

bilinear_interpolation(self, image, fx, fy):

1. image, resize scale along x axis (fx) and resize scale along y axis(fy) are taken as input parameters to the nearest_neigbour function.
2. The number of pixels that should be present along the x axis is calculated as (w * int(fx)). where w is the number of pixels along x axis in the original image.
3. The number of pixels that should be present along the y axis is calculated as (h * int(fy)). where h is the number of pixels along y axis in the original image.
4. Blank image is created with new scale is created.
5. Calculated the four nearest neigbor pixel in original image to the pixel in new image.
6. we find the intensity of the point in the new image by calling the bilinear_interpolation function.
7. Repeated for all the pixels in the new image except the last 3 columns and rows.
8. The last three columns and rows pixels are assigned with the previous column and row intensity values.
9. The resized image(new image with all the pixel values assigned) is reutrned.

Histogram:

compute_histogram(self, image):

1. Image is taken as the input parameter to this function where we find the pixels which have perticular intensity.
2. Iterate through all the pixels checking for the a particular intensity.
3. If the intensity of pixels matches with the particular intensity then increment the count at that intensity in the list.
4. Repeat for all the intensity values.
5. The list of number of pixels at particular intensity is returned.

Threshold:

find_optimal_threshold(self, hist):

1. The list of the frequency of occurance of intensities in a image is taken as the input.
2. sum of all the probabilities of the count of pixels with that intensity multiplied by that intensity.
3. The sum gives the threshold

Binary Image:

binarize(self,threshold, image):

1. Threshold and the image are passed as the input parameter to the function
2. For each pixel
3. if the intensity value is less than threshold then make the intensity as 255(which represents white background).
4. else the intensity value is 0.
5. The binary image obtained is returned.



