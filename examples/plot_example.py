import numpy as np
import matplotlib.pylab as plt

x = np.random.random(10)
y = np.random.random(10)
plt.figure()
plt.plot(x,y,'ro')


x = np.linspace(0,10,100)
y = np.sin(x)
plt.figure()
plt.plot(x,y,'b-')

plt.show()



'''
plt.xlabel('# of elements in arrays')
plt.ylabel('time to execute (s)')
plt.legend(loc='upper left')

plt.plot(x, yGPU, 'o', x_new, y_new,label='GPU - numba/cuda')
plt.plot(x, yNumpy, 'ro', x_new2, y_new2,label='CPU - numpy')
'''
