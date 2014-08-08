import numpy as np
import zipfile
import cms_tools
def get_collisions(infile,verbose=False):
	names = infile.namelist()
	q = infile.read(names[0])
	file = open("newtxtfile.txt", "w")
	file.write(q)
	file = open("newtxtfile.txt", "r")
	return cms_tools.get_collisions(file)
