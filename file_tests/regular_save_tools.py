

import numpy as np

def get_collisions(infile,verbose=False):
#        f = open(infile, "r")
        collisions = np.load(infile)
        infile.close()
        return collisions

