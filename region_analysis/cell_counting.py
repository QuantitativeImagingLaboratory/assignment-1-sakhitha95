import numpy as np
import cv2
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        r,c=image.shape
        region_counter=1
        R = np.zeros((r, c))
        for i in range(r):
            for j in range(c):
                if image[i, j] == 255 and image[i, j - 1] == 0 and image[i - 1, j] == 0:
                    R[i, j] = region_counter
                    region_counter = region_counter + 1
                if image[i, j] == 255 and image[i, j - 1] == 0 and image[i - 1, j] == 255:
                    R[i, j] = R[i - 1, j ]
                if image[i, j] == 255 and image[i, j - 1] == 255 and image[i - 1, j] == 0:
                    R[i, j] = R[i, j - 1]
                if image[i, j] == 255 and image[i, j - 1] == 255 and image[i - 1, j] == 255:
                    R[i, j] = R[i - 1, j]
                if R[i, j - 1] != R[i - 1, j]:
                    R[i, j - 1] == R[i - 1, j]
        for i in range(r):
            for j in range(c):
                for m in range(1,region_counter):
                    if image[i, j] == 0 and R[i, j]!= m :
                        image[i, j] = 255
        #for k in range(1,region_counter):
        #    regions[k]=[]
        #    for i in range(r):
        #        for j in range(c):
        #            if R[i,j]==k:
        #                regions[k].append([i,j])
        for k in range(1, region_counter):
            regions[k] = []
            for i in range(r):
                for j in range(c):
                    if image[i,j]==k:
                        regions[k].append([i,j])



        print(regions)

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        finalreg=dict()
        count=1
        for i in range(1,len(region)+1):
            if(len(region[i])>15):
                cx=0
                cy=0
                for j in range(len(region[i])):
                    cx+=(region[i][j][0]/len(region[i]))
                    cy += (region[i][j][1]/len(region[i]))

                finalreg[count]=[[int(cx),int(cy)],len(region[i])]
                count += 1

        print(finalreg)

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return finalreg

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for i in range(1,len(stats)+1):
            x=stats[i][0][0]
            y=stats[i][0][1]
            #print(x,y)
            cv2.putText(image, "*", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (126,0, 0))
        return image

