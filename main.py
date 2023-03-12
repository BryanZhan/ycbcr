import cv2
import numpy as np

img = cv2.imread('mp2a.jpg')
img1 = img.copy()
ycrcb = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
channels = cv2.split(ycrcb)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe.apply(channels[0], channels[0])
cv2.merge(channels, ycrcb)
cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR, img1)
res1 = img1.copy()
cv2.imshow('img1', res1)

img2 = cv2.imread('mp2a.jpg')
img2_yuv = cv2.cvtColor(img2, cv2.COLOR_BGR2YUV)
img2_yuv[:, :, 0] = cv2.equalizeHist(img2_yuv[:, :, 0])
img2_output = cv2.cvtColor(img2_yuv, cv2.COLOR_YUV2BGR)
cv2.imshow('opencv', img2_output)
cv2.waitKey(0)