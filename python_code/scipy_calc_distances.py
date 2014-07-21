from numba import cuda
import numba
import numpy as np
import math
import matplotlib.pylab as plt
from scipy.spatial.distance import pdist

npts = 10000

#ncalc = (npts*(npts-1))/2


x = 10*np.random.random(npts)
y = 10*np.random.random(npts)
x = np.float32(x)
y = np.float32(y)

new_array = np.vstack((x.T, y.T)).T

dist = pdist(new_array, 'euclidean')

a = plt.hist(dist, bins=50)
#plt.show()



