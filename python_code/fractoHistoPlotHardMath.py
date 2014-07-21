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
    arr_out[i] =math.cos(arr_a[i])*math.sin(arr_b[i])+math.sin(arr_a[i])*math.cos(arr_b[i])+math.log10(arr_a[i])*math.log10(arr_b[i])


def adder(a, b):
    cnc = np.empty_like(a)
    cnc = np.cos(a) * np.sin(b) + np.sin(a) * np.cos(b) + np.log10(a) * np.log10(b)
    return cnc





n = 100000
a = np.arange(n,dtype=np.float32)
b = np.arange(n,dtype=np.float32)
c = np.empty_like(a)


thread_ct = my_gpu.WARP_SIZE
block_ct = int(math.ceil(float(n) / thread_ct))
vadd[block_ct, thread_ct](a, b, c)
cnc = adder(a, b)
toGraph = cnc - c

plt.figure()
plt.hist(toGraph, bins = 10) #.0001
plt.show()


















