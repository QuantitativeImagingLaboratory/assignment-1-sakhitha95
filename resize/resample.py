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
        fx=float(fx)
        fy=float(fy)
        print(w,fx)
        nx = int(w * fx)
        ny = int(h * fy)
        img1 = numpy.zeros((nx, ny))
        for i in range(nx):
            for j in range(ny):
                img1[i, j] = image[int(i / fx), int(j / fy)]

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
        fx=float(fx)
        fy=float(fy)
        nx = int(w * fx)
        ny = int(h * fy)
        img1 = numpy.zeros((nx, ny))
        for i in range(nx - 3):
            for j in range(0,ny - 3):
                x1=math.ceil(i / fx)
                x2=x1+1
                y1=math.ceil(j / fy)
                y2=y1+1
                pt1 = [x1,y1,image[x1,y1]]
                pt2 = [x2, y1, image[x2, y1]]
                pt3 = [x1, y2, image[x1, y2]]
                pt4 = [x2, y2, image[x2, y2]]
                unknown=[i / fx,j / fy,0]
                l=interobj.bilinear_interpolation(interobj,pt1,pt2,pt3,pt4,unknown)
                img1[i,j]=l
                if i==(nx-3):
                    print("hello")
                if j == (ny - 3):
                    print("hello2")
        for i in range(nx - 3,nx):
            for j in range(0,ny):
                img1[i,j]=img1[i-1,j]
                if i == nx:
                    print(i)
        for i in range(0,nx):
            for j in range(ny-3,ny):
                img1[i,j]=img1[i,j-1]

        return img1



