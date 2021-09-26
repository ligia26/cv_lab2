from gauss1D import gauss1D
import numpy as np

def gauss2D( sigma_x, sigma_y , kernel_size ):
    X = gauss1D(sigma_x, kernel_size)
    Y = gauss1D(sigma_y, kernel_size)
    G = np.outer(X,Y)
    return G