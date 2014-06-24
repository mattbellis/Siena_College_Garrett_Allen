import numpy as np
import matplotlib.pylab as plt

x = np.random.random(1000)
plt.figure()
plt.hist(x,bins=25)

x = np.random.normal(5.0,0.5,10000)
plt.figure()
plt.hist(x,bins=100,range=(0,10))
plt.xlim(0,10)

plt.show()
