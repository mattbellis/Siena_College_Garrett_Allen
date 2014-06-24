# Day's second assignment : Printing information on the GPU


import numba.cuda
import numpy as np
import math

my_gpu = numba.cuda.get_current_device()
print "Running on GPU:", my_gpu.name
cores_per_capability = {
	1: 8,
	2: 32,
	3: 192,
}
cc = my_gpu.compute_capability
print "Compute capability: ", "%d.%d" %cc, "Numba requires >= 2.0)"
majorcc = cc[0]
print "Number of streaming pultiprocess:", my_gpu.MULTIPROCESSOR_COUNT
cores_per_multiprocessor = cores_per_capability[majorcc]
print "Number of cores per multiprocessor:", cores_per_multiprocessor
total_cores = cores_per_multiprocessor * my_gpu.MULTIPROCESSOR_COUNT
print "Number of cores on GPU:", total_cores

