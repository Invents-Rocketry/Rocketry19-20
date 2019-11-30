from cv2 import cv2
import numpy as np
import time

left = cv2.imread('test1.jpg',-1)
right = cv2.imread('test2.jpg',-1)
images=[left,right]

stitcher = cv2.createStitcher()

ret,pano = stitcher.stitch(images)

if ret == cv2.Stitcher_OK:
    cv2.imshow('Panorama', pano)
    cv2.waitKey()
else:
    print('These images cannot be stitched')
    time.sleep(3000)

cv2.destroyAllWindows()