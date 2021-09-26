
from math import pi,sqrt,exp

def  gauss1D(sigma ,kernel_size):
	if kernel_size % 2 == 0:
		raise ValueError('kernel_size must be odd, otherwise the filter will not have a center to convolve on')
	
	truncate_range = range(-int(kernel_size/2), int(kernel_size/2+1))
	X = [(1 / (sigma * sqrt(2 * pi))) * exp(-(x**2)/(2*sigma**2)) 
        for x in truncate_range]

    # normalize G to sum to 1
	G =  np.asarray(X) / sum(X)
	return G

def  gauss2D(sigma_x,sigma_y,kernel_size):
	X = gauss1D(sigma_x, kernel_size)
	Y = gauss1D(sigma_y, kernel_size)
	G = np.outer(X,Y)
	return G

def createGabor():
	# your code
