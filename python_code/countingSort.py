import numpy as np
import math


n = 1000000
max = 11
count = np.zeros(max)
input = np.random.randint(0, max, n)
output = np.empty_like(input)

for i in range(0, n):
    count[i] += 1

total = 0
for i in range(max):
    oldCount = count[i]
    count[i] = total
    total += oldCount

for i in range(0, 1000000):
    output[count[i]] = count[i]
    count[i] += 1

if output.all() == np.sort(input).all():
    print ":)"
else:
    print "loser"


