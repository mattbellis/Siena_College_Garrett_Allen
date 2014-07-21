import numpy as np


n = 1000000
#x = np.arange( n,  dtype = np.float32)
x = np.random.rand(n)
total = 0
for i in range(0, n-1):
	total += (x[i] + x[i+1]) / 2


print total
