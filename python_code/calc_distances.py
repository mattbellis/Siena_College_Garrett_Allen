import numpy as np
import matplotlib.pylab as plt
import math
npts = 1000

x = 10*np.random.random(npts)
y = 10*np.random.random(npts)

plt.figure()
plt.plot(x,y,'o',markersize=1)
plt.show()

count = 0
for i in range(0, 1000):
	if i%10==0:
		print "halfway"
	for j in range(i+1, 1000):
		distance[count] =math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
		count = count + 1

	print "we are here"
plt.figure()	
plt.hist(x, bins=100)
plt.show()

