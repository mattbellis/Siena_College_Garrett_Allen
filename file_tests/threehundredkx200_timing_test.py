
import cms_tools
import compressed_cms_tools
import ga_tools
import regular_save_tools
import pickle
import zipReadFile
import zipfile

inFile = open('save300kx200.npz.npy', 'r') #Regular savefile 300kx200
#inFile = open('compressedsavez300kx200.npz', 'r') #compressed savefile 300kx200
#inFile = open('pickle300kx200.p') #Pickle data 300kx200



#collisions = compressed_cms_tools.get_collisions(inFile)  #compressed runner
#collisions = ga_tools.get_collisions(inFile) #pickle runner
collisions = regular_save_tools.get_collisions(inFile) #Regular savefile runner


for collision in collisions:
#	print collision[0]
	
	muons = 0
	jets = 0
	electrons = 0
	photons = 0
	for jet in range (0, 10):
		jets +=   collision[jet]
	for muon in range(10,20):
		muons +=  collision[muon]
	for electron in range(20, 30):
		electrons +=  collision[electron]
	for photon in range(30,40):
		photons +=   collision[photon]





