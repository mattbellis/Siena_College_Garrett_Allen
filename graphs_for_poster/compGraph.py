import numpy as np
import matplotlib.pylab as plt

x = np.array([100, 1000, 100000, 1000000, 10000000, 100000000])

itjava = np.array([0.00185, 0.00135, 0.00807, 0.794, 9.46, 110.3])
cudapython = np.array([.492, .472, .484, .48, .512, .492])
itpython = np.array([.232, .252, .768, 7.552, 92.464, 1059.74])



plt.xlim(90, 100000000)
plt.ylim(0, 1100)



plt.plot(x, itjava, 'ro', label = 'iterative java', markersize = 12)
plt.plot(x, cudapython, 'bx', label = 'CUDA python', markersize = 12)
plt.plot(x, itpython, 'g^', label = 'iterative python', markersize = 12)

plt.xlabel('array size (elements)')
plt.ylabel('time(seconds)')
plt.title('time vs. array size for various implementations')

plt.legend(loc = 'upper left')
#plt.show()
plt.savefig('timevssize.png')



