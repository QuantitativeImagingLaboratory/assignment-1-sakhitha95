import cv2
import numpy
import math

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
                l=self.bilinear_interpolation1(pt1,pt2,pt3,pt4,unknown)
                img1[i,j]=l
        return img1


    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here
        x1=pt1[0]
        y1=pt1[1]
        i1=pt1[2]
        x2=pt2[0]
        y2=pt2[1]
        i2=pt2[2]
        x3=unknown[0]
        y3=unknown[1]
        i3=unknown[2]
        if x3==x1:
            return i1
        elif x3==x2:
            return i2
        else:
            i3=i1*((x2-x3)/(x2-x1)) + i2*((x3-x1)/(x2-x3))
            return i3


        return i3

    def bilinear_interpolation1(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task



        r1 = [unknown[0], pt1[1], 0]
        i1=self.linear_interpolation(pt1,pt2,unknown)
        r1[2]=i1
        r2 = [unknown[0], pt3[1], 0]

        i2 = self.linear_interpolation(pt3, pt4, unknown)
        r2[2] = i2
        fin = self.linear_interpolation(r1, r2, unknown)

        return fin


