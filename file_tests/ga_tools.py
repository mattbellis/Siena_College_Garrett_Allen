import numpy as np
import pickle


def get_collisions(infile,verbose=False):
#	f = open(infile)
	collisions = pickle.load(infile)
	infile.close()
	return collisions

