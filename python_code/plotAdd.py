import numpy as np
import matplotlib.pylab as plt

x = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]
yVadd = [0.105684041977, 0.0995857715607, 0.0999331474304, 0.104926109314, 0.165735960007, 0.53479218483, 3.7153699398, 34.6903600693]
yAdder = [0.000123023986816, 0.00013279914856, 0.0001540184021, 0.000375986099243, 0.00373005867004, 0.0657839775085, 1.29767799377, 12.9012799263]

yVadd = [q/100 for q in yVadd]
yAdder = [q/100 for q in yAdder]
#print yVadd
#print yAdder

plt.figure()
plt.plot(x, yVadd, 'r-')
plt.plot(x, yAdder, 'b-')
plt.xscale('log')
plt.yscale('log')
plt.show()


