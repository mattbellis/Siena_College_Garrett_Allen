import numpy as np
import matplotlib.pylab as plt

x = np.array([10000, 109000, 383000])

txt = np.array([250810, 28027485, 161626452])
compressed = np.array([ 120569, 13091980, 74500000])
pickle = np.array([300857, 35647624, 199000225])
noncompd = np.array([259938, 28852513, 162218402])
zippd = np.array([91611, 10040492, 59796328])



plt.xlim(1000, 400000)
plt.ylim(8000, 200000000)



plt.plot(x, txt, 'ro', label = 'text file', markersize = 12)
plt.plot(x, compressed, 'bx', label = 'compressed binary file', markersize = 12)
plt.plot(x, pickle, 'g^', label = 'pickle file', markersize = 12)
plt.plot(x, noncompd, 'py',label =  'binary file', markersize = 12)
plt.plot(x, zippd, 'c*',label = 'zipped text file', markersize = 12)

plt.xlabel('array size (elements)')
plt.ylabel('file size(bytes)')
plt.title('file size vs. array size for various file formats')

plt.legend(loc = 'upper left')
#plt.show()
plt.savefig('fig2.png')



