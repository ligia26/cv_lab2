import numpy as np
from math import sqrt, pi, exp

def gauss1D( sigma , kernel_size ):
    if kernel_size % 2 == 0:
        raise ValueError('kernel_size must be odd, otherwise the filter will not have a center to convolve on')
    
    truncate_range = range(-int(kernel_size/2), int(kernel_size/2+1))
    X = [(1 / (sigma * sqrt(2 * pi))) * exp(-(x**2)/(2*sigma**2)) 
        for x in truncate_range]

    # normalize G to sum to 1
    G =  np.asarray([np.asarray(X) / sum(X)])

    return G
