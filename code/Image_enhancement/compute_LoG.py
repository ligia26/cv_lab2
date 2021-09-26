from gauss2D import gauss2D
from scipy.signal import convolve2d
import numpy as np
from math import pi, exp
from scipy.ndimage import laplace

def compute_LoG(image, LOG_type):
    sigma = 0.5
    kernel_size = 5

    if LOG_type == 1:
        gauss_kernel = gauss2D(sigma, sigma, kernel_size)
        smoothed_image = convolve2d(image, gauss_kernel)
        imOut = laplace(smoothed_image)

    elif LOG_type == 2:
        LoG_kernel = np.zeros((kernel_size, kernel_size))
        
        for i in range(kernel_size):
            for j in range(kernel_size):
                LoG_kernel[i][j] = (
                    (- 1/(pi * sigma**4)) *
                    (1 - (i**2 + j**2)/ (2*sigma**2)) * 
                    exp(-(i**2 + j**2)/(2*sigma**2)))
        
        imOut = convolve2d(image, LoG_kernel)
        

    elif LOG_type == 3:
        sigma2 = 1
        gauss_kernel1 = gauss2D(sigma, sigma, kernel_size)
        gauss_kernel2 = gauss2D(sigma2, sigma2, kernel_size)
        DoG_kernel = gauss_kernel1 - gauss_kernel2
        imOut = convolve2d(image, DoG_kernel)
        
    return imOut

