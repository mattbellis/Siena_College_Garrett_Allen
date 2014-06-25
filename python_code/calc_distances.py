import numpy as np
import matplotlib.pylab as plt
import math
npts = 1000

x = 10*np.random.random(npts)
y = 10*np.random.random(npts)

plt.figure()
plt.plot(x,y,'o',markersize=1)
plt.show()
distance = [0]*500500
count = 0
for i in range(0, 1000):
	for j in range(i+1, 1000):
		distance[count] =math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
		count = count + 1

plt.figure()	
plt.hist(x, bins=20)
plt.show()

