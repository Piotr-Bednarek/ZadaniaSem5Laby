import numpy as np
import cv2 as cv

plist=[]
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(resized,(x,y),10,(0,0,255),-1)

        plist.append((x,y)) 

    

    if len(plist)==4:
        points=np.float32(plist)
        M = cv.getPerspectiveTransform(points,pts2)
        imgres=cv.warpPerspective(resized,M,(300,300))
        cv.imshow("res",imgres)


 
# Create a black image, a window and bind the function to window
img = cv.imread("lab4/obraz.jpg")

scale = 0.5
h, w = img.shape[:2]
new_size = (int(w * scale), int(h * scale))

resized = cv.resize(img, new_size, interpolation=cv.INTER_AREA)

cv.namedWindow('image')
cv.namedWindow("res")
cv.setMouseCallback('image',draw_circle)
 
while(1):
    cv.imshow('image',resized)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()