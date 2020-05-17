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

def gamma_correction(f,gamma=2.0):
    g = f.copy()
    nr,nc=f.shape[:2]
    c = 255.0/(255.0**gamma)
    table = np.zeros(256)
    for i in range(256):
        table[i]=round(i**gamma*c,0)
    if f.ndim !=3:
        for x in range(nr):
            for y in range(nc):
                g[x,y]= table[f[x,y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x,y,k]= table[f[x,y,k]]
    return g


def main():
    imgOrg=cv2.imread("2165001.bmp",-1)
    imgNegative = img_negative(imgOrg)
    imgGammaCorrection = gamma_correction(imgOrg,0.1)
    cv2.imshow("Original Image",imgOrg)
    cv2.imshow("Image Negative",imgNegative)
    cv2.imshow("Gamma = 0.1",imgGammaCorrection)
    cv2.waitKey(0)

main()


