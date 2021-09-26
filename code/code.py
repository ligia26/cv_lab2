
from math import pi,sqrt,exp

def  gauss1D(sigma ,kernel_size):
	r = range(-int(kernel_size/2),int(kernel_size/2)+1)
        return [1 / (sigma * sqrt(2*pi)) * exp(-float(x)**2/(2*sigma**2)) for x in r]

def  gauss2D(sigma ,kernel_size):
	# your code
	return G

def createGabor():
	# your code
