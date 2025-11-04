import numpy as np
import cv2 as cv 

img = cv.imread("lab5/Albert.jpg",cv.IMREAD_GRAYSCALE)

def empty_callback(value):
    pass

cv.namedWindow('image')
cv.createTrackbar('Tmin', 'image', 50, 500, empty_callback)
cv.createTrackbar('Tmax', 'image', 150, 500, empty_callback)


Mx=np.array([[1,0,-1],
             [2,0,-2],
             [1,0,-1]])
My=np.array([[1,2,1],
             [0,0,0],
             [-1,-2,-1]])

dstx = cv.filter2D(img,cv.CV_32F,Mx,None,(-1,-1),0,cv.BORDER_DEFAULT) /4
dsty = cv.filter2D(img,cv.CV_32F,My,None,(-1,-1),0,cv.BORDER_DEFAULT) /4 

mag=np.sqrt(dstx**2+dsty**2)/255


while(1):
    cv.imshow('image',mag)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()