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

print np.sin, "is of type", type(np.sin)
print np.add, "is of type", type(np.add)

@numba.vectorize(['float32(float32, float32)', 'float64(float64, float64)'], target = 'cpu')

def cpu_sincos(x, y):
	return math.sin(x) * math.cos(y)

@numbapro.vectorize(['float32(float32, float32)', 'float64(float64, float64)'], target = 'gpu')

def gpu_sincos(x, y):
	return math.sin(x) * math.cos(y)

n = 1000000
x = np.linspace(0, np.pi, n)
y = np.linspace(0, np.pi, n)

np_ans = np.sin(x) * np.cos(y)
nb_cpu_ans = cpu_sincos(x, y)
nb_gpu_ans = gpu_sincos(x, y)

print "CPU: ", np.allclose(nb_cpu_ans, np_ans)
print "GPU: ", np.allcose(nb_gpu_ans, np_ans)




