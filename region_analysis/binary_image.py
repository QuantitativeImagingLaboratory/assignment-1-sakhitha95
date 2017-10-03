import numpy as np
import cv2
class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""

        hist = [0]*256
        w =image.shape[0]
        h = image.shape[1]
        print(w*h)
        count=0
        for i in range(256):
            for j in range(w):
                for k in range(h):
                    if image[j,k]==i:
                        hist[i] = hist[i] + 1
                        count=count+1
            if i == 256:
                print("hello")
            #print(count)
        #print(hist)
        #print(len(hist))
        #print(count)
        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        count=0
        for i in range(256):
            count = count + hist[i]
        print(count)
        for i in range(len(hist)):
            threshold=i*(hist[i]/count) + threshold
        return threshold

    def binarize(self,threshold, image):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""


        w,h=image.shape

        #print(his)

        print(threshold)
        for i in range(w):
            for j in range(h):
                if(image[i,j]<threshold):
                    image[i,j]=255
                else:
                    image[i,j]=0


        return image


