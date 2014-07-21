import pycuda.autoinit
import pycuda.gpuarray
import numpy as np
import pycuda.gpuarray as gpuarray
#import integrate
import timeit
from timeit import Timer

from scikits.cuda import integrate
integrate.init()

	
	
	













def iterative(x):
	total = 0
	for i in range(0, n-1):
        	total += (x[i] + x[i+1]) / 2
	return total


def numba(x):
	z = np.trapz(x)
	return z



def scikits(x):
	x_gpu = gpuarray.to_gpu(x)
	#print 2
	z =integrate.trapz(x_gpu)
	return z




n = 100000000
while n < 10000000000:
    a = np.random.rand(n)
#   t = Timer(lambda: iterative(a))
#    t2 = Timer(lambda: numba(a))
#    t3 = Timer(lambda: scikits(a))
#    print n, "elements"
#   print "Iterative way", (t.timeit(number = 100) / 100)
#    print "numba way", (t2.timeit(number = 10) / 10)
#    print "scikits way", (t3.timeit(number = 2) / 2)
#    print "\n \n"
    x = scikits(a)
    y = numba(a)
    print y










    n *= 10
