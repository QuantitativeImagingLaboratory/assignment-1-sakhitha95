import numpy as np
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
        for i in range(r - 1):
            for j in range(c - 1):
                if image[i, j] == 0 and image[i, j - 1] == 255 and image[i - 1, j] == 255:
                    R[i, j] = region_counter
                    region_counter = region_counter + 1
                if image[i, j] == 0 and image[i, j - 1] == 255 and image[i - 1, j] == 0:
                    R[i, j] = R[i - 1, j ]
                if image[i, j] == 0 and image[i, j - 1] == 0 and image[i - 1, j] == 255:
                    R[i, j] = R[i, j - 1]
                if image[i, j] == 0 and image[i, j - 1] == 0 and image[i - 1, j] == 0:
                    R[i, j] = R[i - 1, j]

        for k in range(1,region_counter-1):
            regions[k]=[]
            for i in range(r - 1):
                for j in range(c - 1):
                    if R[i,j]==k:
                        regions[k].append([i,j])




        return regions

    def compute_statistics(self, region):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        numpix=len(region)


        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return 0

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        return image

