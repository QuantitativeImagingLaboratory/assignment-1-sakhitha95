import numpy as np
import cv2
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        region_counter=1
        R = np.zeros(shape=(image.shape[0], image.shape[1]))
        for i in range(0,image.shape[0]):
            for j in range(0,image.shape[1]):
                if i == 0 and j == 0:

                    R[i,j]=region_counter

                    region_counter=region_counter+1
                if i == 0 and j!=0:
                    if image[i,j-1]==255 and image[i,j]==0:
                        R[i,j]=region_counter
                        region_counter=region_counter+1
                    if image[i,j-1]==0 and image[i,j]==0:
                        R[i,j]=R[i,j-1]
                if j==0 and i!=0:
                    if image[i-1,j]==255 and image[i,j]==0:
                        R[i,j]=region_counter
                        region_counter=region_counter+1
                    if image[i-1,j]==0 and image[i,j]==0:
                        R[i,j]=R[i-1,j]


                if i!=0 and j!=0:
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
                            val = R[i, j - 1]
                            R[i, j - 1]= R[i - 1, j]



        for i in range(0, R.shape[0]):
            for j in range(0, R.shape[1]):
                if R[i, j] in regions.keys():
                    regions[R[i, j]].append([i, j])
                else:
                    regions[int(R[i, j])] = [[i, j]]



        print(regions)

        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""
        finalreg=dict()
        count=1

        for key, value in region.items():
            x = 0
            y = 0

            for i in range(0, len(value)):
                x = x + value[i][0]
                y = y + value[i][1]
            x = round(x / len(value))
            y = round(y / len(value))
            centroid = [x, y]
            if (len(value) >= 15):
                finalreg[count] = [centroid, len(value)]
                count=count+1

        print(len(finalreg))
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
        # for i in range(1,len(stats)+1):
        #     x=stats[i][0][0]
        #     y=stats[i][0][1]
        #     image[x,y]=126
        #     #print(x,y)
        #     #cv2.putText(image, "*", (y,x), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (126,0, 0))

        for key, value in stats.items():
            msg = "*"+str(key)+","+str(value[1])
            pixel = (value[0][1], value[0][0])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, msg, pixel, font, 0.2, (255,255,255), 1, cv2.LINE_AA)

        return image

