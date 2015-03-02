import numpy as np
import matplotlib.pylab as plt

x = np.array([1000, 100000, 1000000, 10000000, 100000000])

itjava = np.array([0.00135, 0.00807, 0.794, 9.46, 110.3])
itpython = np.array([.252, .768, 7.552, 92.464, 1059.74])
#cudapython = np.array([.492, .472, .484, .48, .512, .492])
# This is what I get.
cudax = np.array([1000, 100000, 1000000, 10000000, 100000000, 500000000])
cudapython = np.array([0.312, .324, 0.384, 0.576, 2.64, 9.7])



plt.xlim(500, 900000000)
plt.ylim(0.1, 1300)



plt.plot(x, itpython, 'g^', label = 'Python', markersize = 12)
plt.plot(x, itjava, 'rv', label = 'Java', markersize = 12)
plt.plot(cudax, cudapython, 'bo', label = 'numba.cuda (Python)', markersize = 12)

plt.xlabel('# of numbers checked per call (array size)', fontsize=24)
plt.ylabel('Time (seconds)', fontsize=24)
plt.title('Time vs. array size', fontsize=24)
plt.xscale('log')
plt.yscale('log')

plt.tight_layout()

plt.legend(loc = 'upper left')
#plt.show()
plt.savefig('timevssize.png')


plt.show()
