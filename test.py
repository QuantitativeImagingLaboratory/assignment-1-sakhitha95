import cv2
import numpy as np;
image=cv2.imread("cells.png")
hist = [0]*256
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
w,h =image.shape
print(w*h)
count=0
for i in range(255):
    for j in range(w-1):
        for k in range(h-1):
            if image[j,k] == i:
                hist[i] = hist[i] + 1
                count=count+1

threshold = 0
count = 0
for i in range(255):
    count = count + hist[i]
print(count)
for i in range(len(hist) - 1):
    threshold = i * (hist[i] / 1543200) + threshold

for i in range(w - 1):
    for j in range(h - 1):
        if (image[i, j] < threshold):
            image[i, j] = 255
        else:
            image[i, j] = 0

regions = dict()
region_counter=1
R = np.zeros((w, h))
for i in range(w - 1):
    for j in range(h - 1):
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
    for i in range(w - 1):
        for j in range(h - 1):
            if R[i,j]==k:
                regions[k].append([i,j])
finalreg=dict()
count=1
for i in range(1,len(regions)):
    if(len(regions[i])>15):
        cx=0
        cy=0
        for j in (len(regions[i])-1):
            cx+=(regions[i][j][0]/len(regions[i]))
            cy += (regions[i][j][1]/len(regions[i]))

        finalreg[count]=[len(regions[i]),[int(cx),int(cy)]]
        count += 1

cv2.imshow("Image",image)
cv2.waitKey(0)