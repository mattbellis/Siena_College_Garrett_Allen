import pycuda.autoinit
import pycuda.gpuarray
import numpy as np
from scikits.cuda import integrate
import pycuda.gpuarray as gpuarray
import pycuda.autoinit


integrate.init()

x = np.asarray(np.random.rand(10), np.float32)
x_gpu = gpuarray.to_gpu(x)
z = integrate.trapz(x_gpu,0.1)
np.allclose(np.trapz(x), z)
