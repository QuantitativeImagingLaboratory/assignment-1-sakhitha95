import numpy as np
import cv2
class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        img = cv2.imread(image)
        w,h=img.shape()

        for i in range(255):
            for j in range(w-1):
                for k in range(h-1):
                    if img[j,k]==i:
                        hist[i]=+1


        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0

        m1=sorted(hist)[-1]
        m2=sorted(hist)[-2]
        threshold=(m1+m2)/2


        return threshold

    def binarize(self, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        w,h=bin_img.shape()
        his=self.compute_histogram(image)
        threshold=self.find_optimal_threshold(his)
        for i in range(w-1):
            for j in range(h-1):
                if(bin_img[i,j]<threshold):
                    bin_img[i,j]=255
                else:
                    bin_img[i,j]=1


        return bin_img


