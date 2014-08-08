import cms_tools
import compressed_cms_tools
import ga_tools
import regular_save_tools
import pickle
import zipReadFile
import zipfile




infile = zipfile.ZipFile('mattszip4.zip', 'r')

names = infile.namelist()

q = infile.read(names[0])

file = open("newtxtfile.txt", "w")

file.write(q)


file = open("newtxtfile.txt", "r")



x = np.loadtxt(file)



