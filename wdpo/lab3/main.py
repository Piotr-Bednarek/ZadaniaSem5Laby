import cv2 
import numpy as np

def empty_callback(value):
    pass

def zad1():

    # create a black image, a window
    img = cv2.imread("lab3/512-512-max.png",cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('image')
    cv2.namedWindow('img res')

    # create trackbars for color change
    cv2.createTrackbar('progowanie', 'image', 0, 5, empty_callback)

    while True:
        # sleep for 10 ms waiting for user to press some key, return -1 on timeout
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break
        cv2.imshow('image', img)

        val = cv2.getTrackbarPos('progowanie', 'image')
        filsize=2*val+1 

        img_fil=cv2.GaussianBlur(img,(filsize,filsize),2,None,borderType=cv2.BORDER_DEFAULT)
        cv2.imshow("img res",img_fil)
        # get current positions of four trackbars
        
    # closes all windows (usually optional as the script ends anyway)
    cv2.destroyAllWindows()

def zad2():
    # create a black image, a window
    img = cv2.imread("lab3/512-512-max.png",cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('image')

    while True:
        # sleep for 10 ms waiting for user to pr ess some key, return -1 on timeout
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break

        #silly petla 
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if i%3==0:
                    img[i,j]=0
                if j%3==0:
                    img[i,j]=255

        cv2.imshow('image', img)
        
    # closes all windows (usually optional as the script ends anyway)
    cv2.destroyAllWindows()

def zad3():
    # create a black image, a window
    img = cv2.imread("lab3/512-512-max.png",cv2.IMREAD_GRAYSCALE)
    img = img.astype(np.float32)
    cv2.namedWindow('image')

    while True:
        # sleep for 10 ms waiting for user to pr ess some key, return -1 on timeout
        key_code = cv2.waitKey(10)
        if key_code == 27:
            # escape key pressed
            break

        #silly petla 
        for i in range(1,img.shape[0]-1):
            for j in range(1,img.shape[1]-1):
                img[i,j]=(img[i,j]+img[i-1,j]+img[i+1,j]+img[i,j+1]+img[i,j-1]+img[i+1,j+1]+img[i+1,j-1]+img[i-1,j+1]+img[i-1,j-1])/9

        cv2.imshow('image', img)
        
    # closes all windows (usually optional as the script ends anyway)
    cv2.destroyAllWindows()


def main():
    zad3()

if __name__=="__main__":
    main()
