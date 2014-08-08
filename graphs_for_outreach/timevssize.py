import numpy as np
import matplotlib.pylab as plt

x = np.array([10000, 109000, 383000])

txt = np.array([.3, 3.1, 14.0])
compressed = np.array([.5, 21.7, 113.8])
pickle = np.array([.4, 9.5, 46.9])
noncompd = np.array([.2, 1.9, 9.6])
zippd = np.array([.3, 3.2, 14.7])

fig, ax = plt.subplots()
plt.xlim(1000, 400000)
plt.ylim(0, 120)
plt.figure(figsize = (12, 8))

plt.plot(x, txt, 'ro', label = 'text file', markersize = 12)
plt.plot(x, compressed, 'bx', label = 'compressed binary file', markersize = 12)
plt.plot(x, pickle, 'g^', label = 'pickle file', markersize = 12)
plt.plot(x, noncompd, 'py',label =  'binary file', markersize = 12)
plt.plot(x, zippd, 'c*',label = 'zipped text file', markersize = 12)

plt.legend(loc = 'upper left')
"""
:
#ax.plot(x, txt, 'ro', label = 'text file')
#ax.plot(x, compressed, 'bx', label = 'compressed file')

"""
plt.xlabel('array size (elements)')
plt.ylabel('time (s)')
plt.title('time vs. array elements for various file formats')
#plt.show()
plt.savefig('fig1.png')




