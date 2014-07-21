from numba import cuda
import numba
import numpy as np
import math
import matplotlib.pylab as plt


npts = 10000
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
    if i>= arr_out.size:
        return
    for j in range(0, len(arr_a)):
        if math.sqrt((arr_a[i] - arr_a[j]) * (arr_a[i] - arr_a[j]) + (arr_b[i] - arr_b[j]) * (arr_b[i] - arr_b[j])) <= radius:
            arr_out[i] += 1






radius = 0 #change the accepted radius here
thread_ct = my_gpu.WARP_SIZE
block_ct = int(math.ceil(float(npts) / thread_ct))
compute[block_ct, thread_ct](x, y, ans, radius)
ans - 1
print ans[3]

