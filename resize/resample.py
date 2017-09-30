import cv2
import numpy
import math
from resize import interpolation as inter
interobj = inter.interpolation
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        w, h = image.shape
        print(w,fx)
        nx = int(w * int(fx))
        ny = int(h * int(fy))
        img1 = numpy.zeros((nx, ny))
        for i in range(nx - 1):
            for j in range(ny - 1):
                img1[i, j] = image[int(i / int(fx)), int(j / int(fy))]

        print("hello")

        return img1


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here

        w, h = image.shape
        print(w,fx)
        nx = int(w * int(fx))
        ny = int(h * int(fy))
        img1 = numpy.zeros((nx, ny))
        for i in range(nx - 3):
            for j in range(0,ny - 3):
                x1=math.ceil(i / int(fx))
                x2=x1+1
                y1=math.ceil(j / int(fy))
                y2=y1+1
                pt1 = [x1,y1,image[x1,y1]]
                pt2 = [x2, y1, image[x2, y1]]
                pt3 = [x1, y2, image[x1, y2]]
                pt4 = [x2, y2, image[x2, y2]]
                unknown=[i / int(fx),j / int(fy),0]
                l=interobj.bilinear_interpolation(interobj,pt1,pt2,pt3,pt4,unknown)
                img1[i,j]=l
        return img1



