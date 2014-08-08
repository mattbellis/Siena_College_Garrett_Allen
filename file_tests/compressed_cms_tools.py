
import numpy as np



def get_collisions(infile,verbose=False):
#        f = open(infile, "r")
        b = np.load(infile)
	collisions = b['arr_0']
        infile.close()
        return collisions











