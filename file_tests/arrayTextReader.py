import numpy as np


def get_collisions(infile):
	names = infile.namelist()
	q = infile.read(names[0])
	file = open("textOfArray.txt", "w")
	file.write(q)
	infile = open("textOfArray.txt", "r")
	list = []
	line = infile.readline()
	while not line == "":
		a = np.fromstring(line, dtype = float, count = -1, sep = " ")
		list.append(a)
		line = infile.readline()
	collisions = np.array(list)
	return collisions
