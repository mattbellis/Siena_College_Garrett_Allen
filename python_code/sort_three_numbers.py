import numpy as np
import time

ntests = 10000

def sort_three_numbers(x,y,z):

    a = b = c = -999

    return a,b,c

start = time.time()
for i in range(ntests):
    x,y,z = np.random.random(3)
    a,b,c = sort_three_numbers(x,y,z)

diff = time.time() - start

print "Time to run %d times: %f" % (ntests,diff)


