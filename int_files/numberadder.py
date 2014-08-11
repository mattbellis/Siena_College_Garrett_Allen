import numpy as np

a1 = np.loadtxt('file1')


a2 = np.loadtxt('file2')
a3 = np.loadtxt('file3')
a4 = np.loadtxt('file4')
a5 = np.loadtxt('file5')
a6 = np.loadtxt('file6')
a7 = np.loadtxt('file7')
a8 = np.loadtxt('file8')
a9 = np.loadtxt('file9')
a10 = np.loadtxt('file10')


a11 = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10


np.savetxt('sum', a11)




