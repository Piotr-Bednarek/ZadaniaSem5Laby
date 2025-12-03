import cv2
import numpy as np

nazwa_okna = 'img'
cv2.namedWindow(nazwa_okna)

image = np.zeros((500, 500, 3), dtype=np.uint8)

square_size = 25

def empty_callback(val):
    pass

cv2.createTrackbar("R", nazwa_okna, 0, 255, empty_callback)
cv2.createTrackbar("G", nazwa_okna, 0, 255, empty_callback)

cv2.setTrackbarPos("R", nazwa_okna, 255)
cv2.setTrackbarPos("G", nazwa_okna, 255)
        
newR = cv2.getTrackbarPos("R",nazwa_okna)
newG = cv2.getTrackbarPos("G",nazwa_okna)

while True:
    newR = cv2.getTrackbarPos("R",nazwa_okna)
    newG = cv2.getTrackbarPos("G",nazwa_okna)

    for i in range(0, 500, square_size):
        for j in range(0, 500, square_size):
            row = i // square_size
            col = j // square_size

            if (row + col) % 2 == 0:
                # Red square
                image[i : i + square_size, j : j + square_size] = [0, 0, newR]
            else:
                # Green square
                image[i : i + square_size, j : j + square_size] = [0, newG, 0]

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
                break
    
    cv2.imshow(nazwa_okna, image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q") or key == 27:
                break
