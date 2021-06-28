import numpy as np
from math import pi
import math
# small code to produce the paraview collection file to  make animation
#n = np.linspace(30.00,50.00,0.15)
n = np.arange(30.00, 50.00, 0.15)
cout = []
for i in n:
    cout.append("{:.2f}".format(i))
print(cout)

f = open("video.pvd", "a")
f.write('<VTKFile type="Collection" version="0.1"\n')
f.write('         byte_order="LittleEndian"\n')
f.write('         compressor="vtkZLibDataCompressor">\n')

f.write('    <Collection>\n')
for i in range(len(n)):
    f.write('      <DataSet timestep="'+str(cout[i])+'" group="" part="0"\n')
    f.write('            file="vtu/'+str(cout[i])+'.vtu"/>\n')
f.write('    </Collection>\n')
f.write('</VTKFile>\n')

f.close()
