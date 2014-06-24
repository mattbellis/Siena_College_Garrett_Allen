#timeTest.py
#test how long it takes to run vadd vs. adding normally
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
    arr_out[i] = arr_a[i]+arr_b[i]


def adder(array1, array2):
	cnc =  array1 + array2
	return cnc

n = 10
while(n < 1000000000):

	print "n is", n
	a = np.arange(n,dtype=np.float32)
	b = np.arange(n,dtype=np.float32)
	c = np.empty_like(a)


	thread_ct = my_gpu.WARP_SIZE
	block_ct = int(math.ceil(float(n) / thread_ct))


	t = Timer(lambda: vadd[block_ct, thread_ct](a, b, c))
	print "Time it took to complete via vadd was:"
	print  t.timeit(number = 100)
	t2 = Timer(lambda: adder(a, b))
	print "The time it took to complete via adder was:"
	print  t2.timeit(number = 100)
	n = n * 10



