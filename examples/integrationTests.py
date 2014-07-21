import pycuda.autoinit
import pycuda.gpuarray
import numpy as np
import pycuda.gpuarray as gpuarray
#import integrate
from scikits.cuda import integrate
integrate.init()
#x = np.asarray(np.random.rand(10), np.float32)
#x = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
#np.asarray(x)














n = 100000
#x = np.arange( n,  dtype = np.float32)##
x = np.random.rand(n)
#print 1
x_gpu = gpuarray.to_gpu(x)
#print 2
z =integrate.trapz(x_gpu)
#print 3
#print x[99]


print z
