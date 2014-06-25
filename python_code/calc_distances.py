import numpy as np
import matplotlib.pylab as plt

npts = 1000

x = 10*np.random.random(npts)
y = 10*np.random.random(npts)

plt.figure()
plt.plot(x,y,'o',markersize=1)
plt.show()
