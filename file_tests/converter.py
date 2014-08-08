import numpy as np
import cms_tools

#infile = open("fourhundredthousand.dat", "r")
#inFile = open("hundredthousand.dat", "r")
#inFile = open("thousand.dat", "r")# 10k text file
#toConvert = cms_tools.get_collisions(inFile) #textfile runner











def onebyonesixty(collision):
    jets, muons, electrons, photons, met = collision
    x = np.zeros(160)
    for photon in photons:
        photon.append(0)
    counter = 0
    for jet in jets:
        for i in range(0, 5):
            x[counter] = jet[i]
            counter += 1
    counter = 40
    for muon in muons:
        for i in range(0, 5):
            x[counter] = muon[i]
            counter += 1
    counter = 80
    for electron in electrons:
        for i in range(0, 5):
            x[counter] = electron[i]
            counter += 1
    counter = 120
    for photon in photons:
        for i in range(0, 5):
            x[counter] = photon[i]
            counter += 1
    return x


def fourbyforty(collision):
    jets, muons, electrons, photons, met = collision
    x = np.zeros((4, 40))
    counter = 0
    indexer = 1 #0-3
    for photon in photons:
        photon.append(0)
    for muon in muons:
        for i in range(0, 5):
            x[indexer][counter] = muon[i]
            counter += 1
    counter = 0
    indexer = 2
    for electron in electrons:
        for i in range(0, 5):
            x[indexer][counter] = electron[i]
            counter += 1
    counter = 0
    indexer = 0

    for jet in jets:
        for i in range(0, 5):
            x[indexer][counter] = jet[i]
            counter += 1
    counter = 0
    indexer = 3
    for photon in photons:
        for i in range(0, 5):
            x[indexer][counter] = photon[i]
            counter += 1
    counter = 0
    return x



def thirtytwobyfive(collision):
    jets, muons, electrons, photons, met = collision
    indexer = 0
    x = np.zeros((32, 5))
    for photon in photons:
        photon.append(0)
    for jet in jets:
        for i in range(0, 5):
            x[indexer][i] = jet[i]
        indexer += 1
    indexer = 8
    for muon in muons:
        for i in range(0, 5):
            x[indexer][i] = muon[i]
        indexer += 1
    indexer = 16
    for electron in electrons:
        for i in range(0, 5):
            x[indexer][i] = electron[i]
        indexer += 1
    indexer = 24
    for photon in photons:
        for i in range(0, 5):
            x[indexer][i] = photon[i]
        indexer += 1
    return x


def uniformify_1(collisions):
    thingy = []
    for collision in collisions:
        thingy.append(onebyonesixty(collision))
    thingy = np.array(thingy)
    return thingy


def uniformify_2(collisions):
    thingy = []
    for collision in collisions:
        thingy.append(fourbyforty(collision))
    thingy = np.array(thingy)
    return thingy


def uniformify_3(collisions):
    thingy = []
    for collision in collisions:
        thingy.append(thirtytwobyfive(collision))
    thingy = np.array(thingy)
    return thingy

def makeFlies():
    inFile = open("fourhundredthousand.dat", "r")
    inFile2 = open("hundredthousand.dat", "r")
    inFile3 = open("thousand.dat", "r")# 10k text file
    forhund = cms_tools.get_collisions(inFile) #textfile runner
    onehund = cms_tools.get_collisions(inFile2)
    ten = cms_tools.get_collisions(inFile3)
    arr_1_0 = uniformify_1(ten)
    arr_1_1 = uniformify_2(ten)
    arr_1_2 = uniformify_3(ten)
    arr_2_0 = uniformify_1(onehund)
    arr_2_1 = uniformify_2(onehund)
    arr_2_2 = uniformify_3(onehund)
    arr_3_0 = uniformify_1(forhund)
    arr_3_1 = uniformify_2(forhund)
    arr_3_2 = uniformify_3(forhund)
    np.savez("onebyonesixty10k.npz", arr_1_0)
    np.savez_compressed("onebyonesixty10kcompressed.npz", arr_1_0)
    np.savez("fourbyforty10k.npz", arr_1_1)
    np.savez_compressed("fourbyforty10kcompressed.npz", arr_1_1)
    np.savez("thirtytwobyfive10k.npz", arr_1_2)
    np.savez_compressed("thirtytwobyfive10kcompressed.npz", arr_1_2)

    np.savez("onebyonesixty100k.npz", arr_2_0)
    np.savez_compressed("onebyonesixty100kcompressed.npz", arr_2_0)
    np.savez("fourbyforty100k.npz", arr_2_1)
    np.savez_compressed("fourbyforty100kcompressed.npz", arr_2_1)
    np.savez("thirtytwobyfive100k.npz", arr_2_2)
    np.savez_compressed("thirtytwobyfive100kcompressed.npz", arr_2_2)


    np.savez("onebyonesixty400k.npz", arr_3_0)
    np.savez_compressed("onebyonesixty400kcompressed.npz", arr_3_0)
    np.savez("fourbyforty400k.npz", arr_3_1)
    np.savez_compressed("fourbyforty400kcompressed.npz", arr_3_1)
    np.savez("thirtytwobyfive400k.npz", arr_3_2)
    np.savez_compressed("thirtytwobyfive400kcompressed.npz", arr_3_2)














#thingy = []
#for collision in toConvert:
    #thingy.append(onebyonesixty(collision))
    #thingy.append(fourbyforty(collision))
    #thingy.append(thirtytwobyfive(collision))




#thingy = np.array(thingy)

    #jets, muons, electrons, photons, met = collision
