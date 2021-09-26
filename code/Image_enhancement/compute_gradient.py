from math import sqrt
from scipy import signal
import numpy as np

def compute_gradient(image):
    filter1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    filter2 = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])
    Gx = signal.convolve2d(image, filter1)
    Gy = signal.convolve2d(image, filter2)
    im_magnitude = sqrt(Gx**2+Gy**2)
    im_direction = (np.tan(Gx/Gy))**(-1)                   
    return Gx, Gy, im_magnitude,im_direction


