import cms_tools
import compressed_cms_tools
import ga_tools
import regular_save_tools
import pickle
import zipReadFile
import zipfile

#inFile = open("mc_dy_1000collisions.dat", "r") # 10k text file
#inFile = open("mc_dy.dat", "r")# 100k text file
#inFile = open("temp_compressed.npz", "r") #10k cmopressed binary file
#inFile = open("my_data.dat") #Pickle Data 10k 
#inFile = open("temp_compressed2.npz", "r") #100k cmopressed binary file
#inFile = open("my_data2.dat") #Pickle Data 100k
#inFile = open("regular_save_data_2.dat.npy", "r") #Regular savefile 10k
#inFile = open("regular_save_data.dat.npy", "r") #Regular savefile 100k
#inFile = open("regular_save_data_3.dat.npy", "r") #Regular savefile 300k
#inFile = open("mc_ttbar.dat", "r") #300k text file
#inFile = open("temp_compressed3.npz", "r") #300k cmopressed binary file
#inFile = open("my_data3.dat") #Pickle Data 300k
inFile = zipfile.ZipFile('mattszip3.zip', 'r') #Zipped file 300k
#inFile = zipfile.ZipFile('mattszip2.zip', 'r') #Zipped file 100k
#inFile = zipfile.ZipFile('mattszip.zip', 'r') #Zipped file 10k


#inFile = open('savez300kx200.npz', 'r') #Regular savefile 300kx200
#inFile = open('compressedsavez300kx200.npz', 'r') #compressed savefile 300kx200
#inFile = open('pickle300kx200') #Pickle data 300kx200



#print "Reading in the data...."
#collisions = cms_tools.get_collisions(inFile) #textfile runner
#collisions = compressed_cms_tools.get_collisions(inFile)  #compressed runner
#collisions = ga_tools.get_collisions(inFile) #pickle runner
#collisions = regular_save_tools.get_collisions(inFile) #Regular savefile runner
collisions = zipReadFile.get_collisions(inFile) #Zipfile runne
masses = []

for collision in collisions:

    jets,muons,electrons,photons,met = collision

    #print "--------------------------"
    #print "In this event there are..."
    #print "%d jets" % (len(jets))
    #print "%d muons" % (len(muons))
    #print "%d electrons" % (len(electrons))
    #print "%d photons" % (len(photons))

    # To access the information about the particles.

   # for jet in jets:
        #        energy,px,py,pz,btag = jet
        #m = energy*energy - (px*px + py*py + pz*pz)
        #masses.append(m)

    #for muon in muons:
        #energy,px,py,pz,charge = muon

    #for electron in electrons:
        #energy,px,py,pz,charge = electron

    #for photon in photons:
        #energy,px,py,pz = photon

# Here is where you would plot masses.

#print len(masses)
