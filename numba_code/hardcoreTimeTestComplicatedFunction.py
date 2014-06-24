#hardcoretimeTest.py
#test how long it takes to run with trig and log functions
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


def adder(a, b, n):
    cnc = np.empty_like(a)
    cnc = np.cos(a) * np.sin(b) + np.sin(a) * np.cos(b) + np.log10(a) * np.log10(b)
    '''
    for i in range (1, n-1):
        cnc[i] = math.cos(a[i]) * math.sin(b[i]) + math.sin(a[i]) * math.cos(b[i]) + math.log10(a[i]) * math.log10(b[i])
    '''
    return cnc

	

n = 10
while(n < 10000000):

    print "n is ", n
    a = np.arange(n,dtype=np.float32)
    b = np.arange(n,dtype=np.float32)
    c = np.empty_like(a)


    thread_ct = my_gpu.WARP_SIZE
    block_ct = int(math.ceil(float(n) / thread_ct))


    t = Timer(lambda: vadd[block_ct, thread_ct](a, b, c))
    #print  t.timeit(number = 100)
    tfinal = t.timeit(number = 100)
    adder(a, b, n)
    print "Time it took to complete via vadd was:      %f" % (tfinal)
    t2 = Timer(lambda: adder(a, b, n))
    #print  t2.timeit(number = 100)
    tfinal2 = t2.timeit(number = 100)
    print "The time it took to complete via adder was: %f" % (tfinal2)
    n = n * 10



