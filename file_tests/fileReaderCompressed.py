import compressed_cms_tools.py
import numpy as np
inFile = open("my_data.dat")
#print "Reading in the data...."
collisions = ga_tools.get_collisions(inFile)

#print len(collisions)

#count = 0
for collision in collisions:

    jets,muons,electrons,photons,met = collision

#    count += 1

#    print "--------------------------"
 #   print "In this event there are..."
 #   print "%d jets" % (len(jets))
  #  print "%d muons" % (len(muons))
  #  print "%d electrons" % (len(electrons))
  #  print "%d photons" % (len(photons))

    # To access the information about the particles.

    for jet in jets:
        energy,px,py,pz,btag = jet
        mass = energy * energy - (px * px + py * py + pz * pz)

    for muon in muons:
        energy,px,py,pz,charge = muon

    for electron in electrons:
        energy,px,py,pz,charge = electron

    for photon in photons:
        energy,px,py,pz = photon

#Play with energy stuff here

