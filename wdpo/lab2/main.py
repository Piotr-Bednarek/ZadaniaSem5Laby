import cv2
import numpy as np


def empty_callback(value):
    pass

# create a black image, a window
img = cv2.imread("lab3/512-512-max.png",cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('progowanie', 'image', 0, 255, empty_callback)

while True:
    # sleep for 10 ms waiting for user to press some key, return -1 on timeout
    key_code = cv2.waitKey(10)
    if key_code == 27:
        # escape key pressed
        break
    cv2.imshow('image', img) 


    # get current positions of four trackbars
    val = cv2.getTrackbarPos('progowanie', 'image')
    _, img_scale =cv2.threshold(img,val,255,cv2.THRESH_BINARY)

    kernel=np.ones((5,5),np.uint8)

    cv2.imshow("res",img_scale)
    cv2.imshow('res_erode',cv2.erode(img_scale,kernel))
    cv2.imshow("res_dilatation",cv2.dilate(img_scale,kernel))
     

# closes all windows (usually optional as the script ends anyway)
cv2.destroyAllWindows()

#zadanie domowe na kostke 