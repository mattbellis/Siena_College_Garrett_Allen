# FIRST ASSIGNMENT
# FIX THIS / FIGURE OUT VADD
#TMP.PY
from numba import cuda 
import numba
import numpy as np
import math


my_gpu = numba.cuda.get_current_device()
@numba.cuda.jit("void(float32[:],float32[:],float32[:])")
def vadd(arr_a,arr_b,arr_out):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    i = tx + bx * bw
    if i>= arr_out.size:
        return
    arr_out[i] = arr_a[i]+arr_b[i]


n = 1000000
a = np.arange(n,dtype=np.float32)
b = np.arange(n,dtype=np.float32)
c = np.empty_like(a)



thread_ct = my_gpu.WARP_SIZE
block_ct = int(math.ceil(float(n) / thread_ct))


print c
print "Threads per block:", thread_ct
print "Block per grid:", block_ct
vadd[block_ct, thread_ct](a, b, c)
print "a \n", a, "\n \n"
print "b \n", b, "\n \n"
print "c \n", c
