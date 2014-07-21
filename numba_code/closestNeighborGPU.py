from numba import cuda
import numba
import numpy as np
import math
import matplotlib.pylab as plt


npts = 400000
my_gpu = numba.cuda.get_current_device()



x = 10*np.random.random(npts)
y = 10*np.random.random(npts)
x = np.float32(x)
y = np.float32(y)
ans = np.zeros(npts, dtype = np.float32)

@numba.cuda.jit("void(float32[:], float32[:], float32[:], float32)")
def compute(arr_a, arr_b, arr_out, radius):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    i = tx + bx * bw
    a0 = arr_a[i]
    b0 = arr_b[i]
    if i>= arr_out.size:
        return
    narr_a = len(arr_a)
    for j in xrange(narr_a):
        diff0 = a0 - arr_a[j]
        diff1 = b0 - arr_b[j]
        if math.sqrt(diff0 * diff0 + diff1 * diff1) <= radius:
            arr_out[i] += 1






radius = 0.1 #change the accepted radius here
thread_ct = my_gpu.WARP_SIZE
block_ct = int(math.ceil(float(npts) / thread_ct))
compute[block_ct, thread_ct](x, y, ans, radius)

ans -= 1 #Since each element counts itself
print ans



