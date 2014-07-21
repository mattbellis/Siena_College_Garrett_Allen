import numpy as np
import matplotlib.pylab as plt

x = [10, 100, 1000, 10000, 100000, 1000000]
yGPU = [0.105700969696, 0.0993461608887, 0.100205898285, 0.105057001114, 0.168247938156, 0.622693061829]
yNumpy = [0.00163197517395, 0.0185189247131, 0.187418937683, 1.84713196754, 18.4095630646, 185.81090498]

yGPU = [q/100 for q in yGPU]
yNumpy = [q/100 for q in yNumpy]

z = np.polyfit(x, yGPU, 2)
f = np.poly1d(z)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

z2 = np.polyfit(x, yNumpy, 2)
f2 = np.poly1d(z2)

x_new2 = np.linspace(x[0], x[-1], 50)
y_new2 = f2(x_new2)



plt.plot(x, yGPU, 'o', x_new, y_new,label='GPU - numba/cuda')
plt.plot(x, yNumpy, 'ro', x_new2, y_new2,label='CPU - numpy')
plt.xlim([x[0]-1, x[-1]+1])
plt.xscale('log')
plt.yscale('log')
plt.xlabel('# of elements in arrays')
plt.ylabel('time to execute (s)')
plt.legend(loc='upper left')


plt.show()


#plt.figure()
#plt.plot(x, yGPU, 'r-')
#plt.plot(x, yNumpy, 'b-')
#plt.show()


