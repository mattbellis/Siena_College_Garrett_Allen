import numpy as np


import compressed_cms_tools

one = False
four = False
three = False




#inFile = open("onebyonesixty10k.npz", "r"); one = True;
#inFile = open("onebyonesixty10kcompressed.npz", "r"); one = True;
#inFile = open("fourbyforty10k.npz", "r"); four = True;
#inFile = open("fourbyforty10kcompressed.npz", "r"); four = True
#inFile = open("thirtytwobyfive10k.npz", "r"); three = True
#inFile = open("thirtytwobyfive10kcompressed.npz", "r"); three = True
#inFile = open("onebyonesixty100k.npz","r"); one = True
#inFile = open("onebyonesixty100kcompressed.npz", "r"); one = True
#inFile = open("fourbyforty100k.npz", "r"); four = True
#inFile = open("fourbyforty100kcompressed.npz", "r"); four = True
#inFile = open("thirtytwobyfive100k.npz","r"); three = True
#inFile = open("thirtytwobyfive100kcompressed.npz", "r"); three = True
#inFile = open("onebyonesixty400k.npz", "r"); one = True
#inFile = open("onebyonesixty400kcompressed.npz","r"); one = True
#inFile = open("fourbyforty400k.npz", "r"); four = True
#inFile = open("fourbyforty400kcompressed.npz", "r"); four = True
#inFile = open("thirtytwobyfive400k.npz", "r"); three = True
inFile = open("thirtytwobyfive400kcompressed.npz", "r"); three = True


collisions = compressed_cms_tools.get_collisions(inFile)


def onebyonesixtyParser():
    masses = []
    for collision in collisions:
        jets = collision[0:40]
        muons = collision[40:80]
        electrons = collision[80:120]
        photons = collision[120:160]

        for i in xrange(8):
            jet = jets[i*5:(i+1)*5]:
            energy,px,py,pz,btag = jet
            m = energy*energy - (px*px + py*py + pz*pz)
            masses.append(m)

    return masses

#        x = 0
#        while x < 40:



def fourbyfortyParser():
    for collision in collisions:
        jets, muons, electrons, photons = collision



def thirtytwobyfiveParser():
    for collision in collisions:
        jets = collision[0:8]
        muons = collision[8:16]
        electrons = collision[16:24]
        photons = collision[24:32]




if one:
    onebyonesixtyParser()
elif four:
    fourbyfortyParser()
elif three:
    thirtytwobyfiveParser()



