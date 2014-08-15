import cms_tools
from time import time
import numpy as np
import pickle
import matplotlib.pylab as plt
import os
################################################################################
def do_some_standard_analysis(collisions):

    masses = []
    for collision in collisions:

        jets,muons,electrons,photons,met = collision

        # To access the information about the particles.
        for jet in jets:
            energy,px,py,pz,btag = jet
            m = np.sqrt(energy*energy - (px*px + py*py + pz*pz))
            masses.append(m)

        for muon in muons:
            energy,px,py,pz,charge = muon

        for electron in electrons:
            energy,px,py,pz,charge = electron

        for photon in photons:
            energy,px,py,pz = photon

    print "# masses calculated: %d" % (len(masses))
    #print masses[0:10]
    #print masses[1000:1010]
    #splice!
    return masses

################################################################################
def main():

    infilenames = ["mc_ttbar.dat","zipfile_save_data_400k.zip", "regular_save_data_400k.npy", "compressed_save_data_400k.npz", "pickle_save_data_400k.dat", "onebyonesixty400k.npz", "onebyonesixty400kcompressed.npz","fourbyforty400k.npz", "fourbyforty400kcompressed.npz", "thirtytwobyfive400k.npz", "thirtytwobyfive400kcompressed.npz"]
    #infilenames = ["mc_ttbar.dat", "onebyonesixty400k.npz"]
    #infilenames = [ "onebyonesixty400k.npz"]
    #infilenames = ["mc_ttbar.dat","zipfile_save_data_400k.zip"]
    #infilenames = ["mc_dy_1000collisions.dat"]
    #infilenames = ["thirtytwobyfive400k.npz", "thirtytwobyfive400kcompressed.npz"]
    read_times = []
    process_times = []
    #infilenames = ["thirtytwobyfive400kcompressed.npz", "mc_ttbar.dat"]
    for i,infilename in enumerate(infilenames):
        print infilename
        infile = open(infilename)
        collisions = None
        start_time = time()

        if infilename[0]=='m':
            collisions = cms_tools.get_collisions(infile)
        elif infilename[0]=='z':
            collisions = cms_tools.get_collisions(infile)
        elif infilename[0]=='r':
            collisions = cms_tools.get_array_collisions(infile)
        elif infilename[0]=='c':
            collisions = cms_tools.get_compressed_collisions(infile)
        elif infilename[0]=='p':
            collisions = cms_tools.get_pickle_collisions(infile)
        elif infilename[0]=='o':
            collisions = cms_tools.get_onebyonesixty_collisions(infile)
        elif infilename[0]=='f':
            collisions = cms_tools.get_fourbyforty_collisions(infile)
        elif infilename[0]=='t':
            collisions = cms_tools.get_thirtytwobyfive_collisions(infile)

        #print "type collisions: ",type(collisions)
        #print "# collisions: %d" % (len(collisions))
        time_to_read_in_data = time()-start_time
        read_times.append(time_to_read_in_data)
        
        start_time = time()
        masses = do_some_standard_analysis(collisions)
        print "type masses: ",type(masses)
        time_to_process_data = time()-start_time
        process_times.append(time_to_process_data)

       # print collisions[0]

        # Make a diagnostic plot.
        masses = np.array(masses)
        plt.figure()
        plt.hist(masses[masses>0],bins=100,range=(0,80))
        plt.xlim(0,80)
        plt.figtext(0.4,0.8,infilename,size=18)
        name = "diagnostic_plot_%s.png" % (infilename.split('.')[0])
        plt.savefig(name)
        #plt.show()

    print read_times
    print process_times

    for n,r,p in zip(infilenames,read_times,process_times):
        print "%-40s  %5.2f %5.2f" % (n,r,p)

    plt.figure()
    plt.plot(read_times,'ko')
    plt.xlim(-1,len(read_times))

    plt.figure()
    plt.plot(process_times,'ro')
    plt.xlim(-1,len(process_times))
        
    points = []
    for name in infilenames:
        points.append(os.path.getsize(name))

    plt.figure()
    for i, (point, name) in enumerate(zip(points, infilenames)):
        plt.plot(i, point, 'o', markersize =20, label = name)

    plt.legend()
    plt.xlim(-1, len(points))

    for i in range(len(points)):
        plt.plot(points[i], process_times[i], 'o', markersize = 15, label = infilenames[i])
    plt.legend()

    
    
    
   # plt.show()
################################################################################
if __name__ == "__main__":
    main()
