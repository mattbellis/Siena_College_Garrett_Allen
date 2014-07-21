import numpy as np
import matplotlib.pylab as plt
import math

npts = 1000


ncalc = (npts*(npts-1))/2

x = 10*np.random.random(npts)
y = 10*np.random.random(npts)


'''
plt.figure()
plt.plot(x,y,'o',markersize=1)
#plt.show()
distance = [-100]*ncalc #exactly 499500 operations (numPoints * (numPoints-1))/2
#print distance[2014]
print len(distance)
count = 0
for i in range(0, npts):
	for j in range(i+1, npts):
		distance[count] =math.sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]))
		count = count + 1




plt.figure()	
x = plt.hist(distance, bins=50)
#plt.show()
print x
'''
count = 0
for i in range(0, npts):
        for j in range(i+1, npts):
		print i, j, count, (i+1) * j - 1
		count = count + 1

