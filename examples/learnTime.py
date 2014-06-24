import timeit
import sys


t = timeit.Timer("print 'main statment'", "print 'setup'")

print 'TIMEIT: '
print t.timeit(2)

print 'REPEAT:'
print t.repeat(3, 2)

