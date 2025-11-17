import cv2
import numpy as np
import random

img = cv2.imread("experiments/beachgs.bmp",cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('image')

h, w = img.shape

img2=cv2.resize(img,None,fx=2.0,fy=2.0,interpolation=cv2.INTER_LANCZOS4)

h2, w2 = img2.shape

out = img.copy()

for i in range(12):
# 1. Random ROI size
    roi_w = random.randint(30, w// 3)
    roi_h = random.randint(30, h // 3)

    # 2. Random ROI origin
    x1 = random.randint(0, w - roi_w)
    y1 = random.randint(0, h - roi_h)

    roi = img[y1:y1+roi_h, x1:x1+roi_w].copy()

    # 3. Random placement location (must fit)
    x2 = random.randint(0, w - roi_w)
    y2 = random.randint(0, h - roi_h)

    # 4. Paste ROI
    out[y2:y2+roi_h, x2:x2+roi_w] = roi



while(1):
    cv2.imshow('image',out)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()