import numpy as np
import cms_tools
import pickle
import zipfile
import zipReadFile
import zipfile












def onebyonesixty(collision):
    jets, muons, electrons, photons, met = collision
    x = np.zeros(162)
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
    x[160] = met[0]
    x[161] = met[1]
    return x


def fourbyforty(collision):
    jets, muons, electrons, photons, met = collision
    x = np.zeros((4, 42))
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
    x[3][40] = met[0]
    x[3][41] = met[1]
    return x



def thirtytwobyfive(collision):
    jets, muons, electrons, photons, met = collision
    indexer = 0
    x = np.zeros((33, 5))
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
    x[32][0] = met[0]
    x[32][1] = met[1]
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

def makeFiles():
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


    inFile10k = open("mc_dy_1000collisions.dat", "r")
    inFile100k = open("mc_dy.dat", "r")
    inFile400k = open("mc_ttbar.dat", "r")

    collisions10k = cms_tools.get_collisions(inFile10k)
    collisions100k = cms_tools.get_collisions(inFile100k)
    collisions400k = cms_tools.get_collisions(inFile400k)

    np.save("regular_save_data_10k.npy", collisions10k)
    np.save("regular_save_data_100k.npy", collisions100k)
    np.save("regular_save_data_400k.npy", collisions400k)
    
    
    np.savez_compressed("compressed_save_data_10k", collisions10k)
    np.savez_compressed("compressed_save_data_100k", collisions100k)
    np.savez_compressed("compressed_save_data_400k", collisions400k)

    pickle.dump(collisions10k, open("pickle_save_data_10k.dat",'wb' ))
    pickle.dump(collisions100k, open("pickle_save_data_100k.dat", 'wb'))
    pickle.dump(collisions400k, open("pickle_save_data_400k.dat", 'wb'))

    with zipfile.ZipFile('zipfile_save_data_10k.zip', 'w') as myzip:
        myzip.write('mc_dy_1000collisions.dat')


    with zipfile.ZipFile('zipfile_save_data_100k.zip', 'w') as myzip:
        myzip.write('mc_dy.dat')


    with zipfile.ZipFile('zipfile_save_data_400k.zip', 'w') as myzip:
        myzip.write('mc_ttbar.dat')




















    





makeFiles()






#thingy = []
#for collision in toConvert:
    #thingy.append(onebyonesixty(collision))
    #thingy.append(fourbyforty(collision))
    #thingy.append(thirtytwobyfive(collision))




#thingy = np.array(thingy)

    #jets, muons, electrons, photons, met = collision
