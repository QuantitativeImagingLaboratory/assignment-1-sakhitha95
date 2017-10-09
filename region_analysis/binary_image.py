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


        count=0
        # for i in range(256):
        #     count = count + hist[i]
        # print(count)
        # threshold = int(len(hist) / 2)
        #
        # for i in range(len(hist)):
        #     if i < threshold:
        #         threshold1 = i* (hist[i] / count) + threshold1
        #     elif i >= threshold:
        #         threshold2 = i * (hist[i] / count) + threshold2
        #     threshold = (threshold1 + threshold2) / 2
        #
        #     threshold=127

        threshold = int((len(hist) - 1) / 2)
        temp = len(hist) - 1

        while True:
            if (temp < 0.5):
                break
            threshold1 = self.evalue(hist, 0, threshold)
            threshold2 = self.evalue(hist, threshold, len(hist))
            nt = int((threshold1 + threshold2) / 2)
            temp = nt - threshold
            threshold = nt

        return threshold


    def evalue(self, hist, lval, rval):
        tot_int = 0
        final_int = 0
        for row in range(lval, rval):
            tot_int += hist[row]
        for col in range(lval, rval):
            final_int += col * (hist[col] / tot_int)
        return final_int




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
                if(image[i,j]>threshold):
                    image[i,j]=255
                else:
                    image[i,j]=0


        return image


