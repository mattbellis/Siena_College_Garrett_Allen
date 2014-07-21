import numpy as np
from scipy.integrate import quad
import math



def integrand(x):
	return 3 * x ** 2

def sinof(x):
	return math.sin(x)	

#ans, err = quad(integrand, 0, 1)
ans, err = quad(sinof, 0, 1000000, limit = 100000000)
print ans
print err
