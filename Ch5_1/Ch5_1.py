import numpy as np
import cv2

def img_negative(img):
    #b,g,r = cv2.split(img)
    #b = 255 - b
    #g = 255 - g
    #r = 255 - r
    #img[:,:,0] = b
    #img[:,:,1] = g
    #img[:,:,2] = r
    g=255-img
    return g

def main():
    imgOrg=cv2.imread("2165001.bmp",-1)
    imgNegative = img_negative(imgOrg)
    cv2.imshow("Original Image",imgOrg)
    cv2.imshow("Image Negative",imgNegative)
    cv2.waitKey(0)

main()


