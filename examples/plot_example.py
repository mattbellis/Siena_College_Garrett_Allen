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
