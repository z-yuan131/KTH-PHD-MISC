#############################
# this piece of code is for convert Nekmesh generated high order mesh to Gmsh format which can be used by PyFR
# Note four bcs(in out free wall) and fluid element is needed, approate modification is needed when meeting different case
# input file name nekv2.msh output file name nek_newv2.msh
# 2020-6-26
############################

import numpy as np
from math import pi
import math


wall = [9,10,11,12]
inlet = [6,7]
outlet = [2,3]
freestream = [1,4,5,8]
fluid = [100,101]

new = []

mesh = iter(open('nekv2.msh'))
temp = next(mesh).split()
new.append(temp)



while temp != ['$EndElements']:
    if temp == ['$Elements']:
        
        eleNum = next(mesh).split()
        new.append(eleNum)
        eleNum= np.array(eleNum)

        
            
        for j in range(int(eleNum)):
            
            temp = next(mesh).split() 
            new.append(temp)
            h = 0
            if h != 1:
                for i in wall:
                    if temp[3] == str(i):
                        new[-1][2] = str(2)
                        new[-1][3] = str(4)
                        new[-1][5] = str()
                        h = 1
            if h != 1:
                for i in freestream:
                    if temp[3] == str(i):
                        new[-1][2] = str(2)
                        new[-1][3] = str(2)
                        new[-1][5] = str()
                        h = 1
            if h != 1:
                for i in inlet:
                    if temp[3] == str(i):
                        new[-1][2] = str(2)
                        new[-1][3] = str(3)
                        new[-1][5] = str()
                        h = 1
            if h != 1:    
                for i in outlet:
                    if temp[3] == str(i):
                        new[-1][2] = str(2)
                        new[-1][3] = str(1)
                        new[-1][5] = str()
                        h = 1
            if h != 1:    
                for i in fluid:
                    if temp[3] == str(i):
                        new[-1][2] = str(2)
                        new[-1][3] = str(5)
                        new[-1][5] = str()
                        h = 1
    
    
    elif temp == ['$Nodes']:
        nodeNum = next(mesh).split()
        new.append(nodeNum)
        nodeNum= np.array(nodeNum)
        for j in range(int(nodeNum)):
            temp = next(mesh).split() 
            new.append(temp)

            new[-1][1] = "{:.12f}".format(float(new[-1][1]))
            new[-1][2] = "{:.12f}".format(float(new[-1][2]))
            new[-1][3] = "{:.12f}".format(float(new[-1][3]))
            
        
    else:
        temp = next(mesh).split()
        new.append(temp)
        
f = open('nek_newv2.msh','a')
for i in new:
    if i == ['$EndMeshFormat']:
        f.write('$EndMeshFormat\n')
        
        f.write('$PhysicalNames\n')
        f.write('5\n')
        f.write('1 1 "outlet"\n')
        f.write('1 2 "freestream"\n')
        f.write('1 3 "inlet"\n')
        f.write('1 4 "wall"\n')
        f.write('2 5 "fluid"\n')
        f.write('$EndPhysicalNames\n')
        
    elif i == ['$MeshFormat']:
        f.write('$MeshFormat\n')
    elif i == ['$Nodes']:
        f.write('$Nodes\n')
    elif i == ['$EndNodes']:
        f.write('$EndNodes\n')
    elif i == ['$Elements']:
        f.write('$Elements\n')
    elif i == ['$EndElements']:
        f.write('$EndElements\n')
    else:
        for j in i:
            f.write(str(j)+' ')
        f.write('\n')
        
    
f.close()
