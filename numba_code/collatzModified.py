
from numba import cuda
import numba
import numpy as np
import math






@numba.cuda.jit("void(int64[:],int64[:])")
def conforms(arr_a, arr_b):
	tx = cuda.threadIdx.x
	bx = cuda.blockIdx.x
	bw = cuda.blockDim.x
	i = tx + bx * bw
	if i >= arr_b.size:
		return	
	x = arr_a[i]
	if x%3 == 0:
		arr_b[i] = 1
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
	arr_b[i] = 1






my_gpu = numba.cuda.get_current_device()
n = 500000000 * 10072 #5 * 10^8
myrange = 500000000
nNot = 0
counter = 10072
answer = np.ones(myrange, dtype = np.int64)
numbers = np.arange(myrange, dtype=np.int64)
numbers += n
thread_ct = my_gpu.WARP_SIZE
block_ct = int(myrange / thread_ct)


while n < 10000000000000:
	counter += 1
	ispossible = np.zeros(myrange, dtype = np.int64) 









	conforms[block_ct, thread_ct](numbers, ispossible)

	if not  ispossible.all() == answer.all():
		while 0 < 1:
			print "something within range", n , "to ", nNot , "failed"
	nNot = n
	n += myrange
	print "run # ", counter, numbers[0]
	numbers += myrange
	if n % 100000000000 == 0:
		np.savetxt("currHighestNumber.txt", n)
	



