
from numba import cuda
import numba
import numpy as np





@numba.cuda.jit("void(int64[:])")
def conforms(arr_a):
    tx = cuda.threadIdx.x
    bx = cuda.blockIdx.x
    bw = cuda.blockDim.x
    i = tx + bx * bw
    if i >= arr_a.size:
        return	
    x = arr_a[i]
    if x%3 == 0:
        return
    while not x == 1:
        if x%9 == 1:
            x = (4*x - 1)/3
        elif x%9 == 7 or x%9 == 4:
            x = (x-1)/3
        elif x%9 == 2 or x%9 == 8:
            x =(2*x-1)/3
        elif x%9 == 5:
            x = (8*x - 1) / 3
    return





my_gpu = numba.cuda.get_current_device()

counter = 0

myrange = 500000000 #5 * 10^8

n = myrange  * counter #useful for starting runs at a non-zero count

toWrite = False #Will this be running on numbers larger than we have previously tested

answer = np.ones(myrange, dtype = np.int64)
numbers = np.arange(myrange, dtype=np.int64)
numbers += n
thread_ct = my_gpu.WARP_SIZE
block_ct = int(myrange / thread_ct)

while n < 10000000000000000:
    counter += 1
    
    conforms[block_ct, thread_ct](numbers)
    #If a number that the conjecture does not hold for is found,
    #then the above method call will get stuck in an infinite loop

    print "run # ", counter, numbers[0]
    #prints the run number (aka 'counter') and the smallest
    #number the gpu is currently working with

    numbers += myrange
    
    if numbers[0] % 100000000000 == 0 and toWrite: #If we are on a multiple of 10^11
        #and we currently want to keep track of the number we're on
        q = numbers[0] / 100000000000   #10^11 
        f = open('currHighestNumber.txt', 'w') #Write that number / 10^11 to a file
        f.write('%d' % q)
        f.close()
        


