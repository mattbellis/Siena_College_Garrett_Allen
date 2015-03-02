import numpy as np
import csv
import zipfile 

x = 100*np.random.random((100000,7))

print x

f = open('npy_test.npy','w')
np.save(f,x)
f.close()

f = open('npy_test.npy','r')
x = np.load(f)
f.close()

f = open('txt_test.txt','w')
#writer = csv.writer(f, delimiter='\t')
#writer.writerows(x)
output = ""
for row in x:
    for col in row:
        output += "%.4f " % (col)
    output += "\n"
f.write(output)
f.close()

with zipfile.ZipFile('txt_test.zip','w',zipfile.ZIP_DEFLATED) as zf:
    zf.write('txt_test.txt')


