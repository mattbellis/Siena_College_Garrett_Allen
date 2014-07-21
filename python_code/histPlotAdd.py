#Exactly Equal, histogram irrelevant
import numpy as np
import matplotlib.pylab as plt




from numba import cuda
import numba
import numpy as np
import math
import timeit
from timeit import Timer

my_gpu = numba.cuda.get_current_device()
@numba.cuda.jit("void(float32[:],float32[:],float32[:])")
def vadd(arr_a,arr_b,arr_out):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    i = tx + bx * bw
    if i>= arr_out.size:
        return
    arr_out[i] =arr_a[i] + arr_b[i]


def adder(a, b):
	c = a + b
	return c





n = 1000000
a = np.arange(n,dtype=np.float32)
b = np.arange(n,dtype=np.float32)
c = np.empty_like(a)


thread_ct = my_gpu.WARP_SIZE
block_ct = int(math.ceil(float(n) / thread_ct))
vadd[block_ct, thread_ct](a, b, c)
cnc = adder(a, b)
toGraph = cnc - c

plt.figure()
plt.hist(toGraph, bins = 100, range =(-.00000001, .00000001))
if c.all() == cnc.all():
	print "equal"
plt.show()


















