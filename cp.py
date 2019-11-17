import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt 


intensity=[]
frameIntensity=0
total=0
prevInten=0
maxlist=[]
localMax=[]
avgInten=0
flag=1
count=0
final=[]

cap=cv2.VideoCapture('B:\\R&D\\OpenCV\\Learning\\new\\67.mp4')
#fourcc=cv2.VideoWriter_fourcc(*'FMP4')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height =cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
fps = cap.get(cv2.CAP_PROP_FPS) #float


print("resoluion is"+str(width)+"*"+str(height))
print("Frame Rate : "+ str(fps))


midWidth=abs(width/2)
midWidthLow=int(midWidth-50)
midWidthHigh=int(midWidth+51)
midHeight=abs(height/2)
midHeightLow=int(midHeight-50)
midHeightHigh=int(midHeight+51)

hRange=range(midHeightLow,midHeightHigh)
wRange=range(midWidthLow,midWidthHigh)


while True:
    ret,frame=cap.read()
    if(ret==False):
        break
    total=total+1
    for i in wRange:
        for j in hRange:
            frameIntensity=frameIntensity+frame[i][j][2]
    intensity.append(frameIntensity)
    frameIntensity=0
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

for inten in intensity:
    avgInten=avgInten+inten

avgInten=int(round(abs(avgInten/len(intensity))))-500
print(avgInten)

for inten in intensity: 
    if inten > avgInten:
        maxlist.append(inten)
        flag=0
    else:
        if flag==0:
            if(len(maxlist)>(4)):
                localMax.append(max(maxlist))
                count=len(maxlist)
            maxlist.clear()
        flag=1


print(len(localMax))
print(localMax)
plt.plot(intensity,'g')
plt.show()
# plt.hist(intensity)
# plt.show()

intensity=np.asarray(intensity)
from scipy.signal import find_peaks
peaks, _ = find_peaks(intensity, height=0, distance=40 , prominence=(10000,30000))
plt.plot(intensity)
print("Frames with peaks :")
print(peaks)
print("Total :")
print(len(peaks))
plt.plot(peaks, intensity[peaks], "x")
#plt.plot(np.zeros_like(intensity), "--", color="gray")
plt.show()
