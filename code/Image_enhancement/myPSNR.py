import math
import numpy as np
import cv2

def myPSNR( orig_image, approx_image ):
    orig_image = orig_image.astype('float32')
    approx_image = approx_image.astype('float32')

    MSE = np.mean((orig_image - approx_image)**2)
    I_max = orig_image.max()
    PSNR = 20 * math.log10(I_max/math.sqrt(MSE))
    
    return PSNR

if __name__ == '__main__':
    img1_saltpepper = cv2.imread('./images/image1_saltpepper.jpg')
    img1_gaussian = cv2.imread('./images/image1_gaussian.jpg')
    img1 = cv2.imread('./images/image1.jpg')

    print("PSNR img1 + img1 saltpepper: ", myPSNR(img1, img1_saltpepper))
    print("PSNR img1 + img1 gaussian: ", myPSNR(img1, img1_gaussian))
