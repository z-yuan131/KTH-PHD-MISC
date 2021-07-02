

import numpy as np
import matplotlib.pyplot as plt



def ReadWallMesh(meshfilename,walltag):
    ## extract wall boundary points using mesh file mesh.msh

    walltag = str(walltag)

    mesh = iter(open(meshfilename))
    temp = next(mesh).split()

    wallEle = []


    while temp != ['$EndElements']:
        if temp == ['$Elements']:
            
            eleNum = next(mesh).split()
            eleNum= np.array(eleNum)

            
                
            for j in range(int(eleNum)):
                
                temp = next(mesh).split()
                h = 0
                if temp[3] == walltag:
                    wallEle = np.append(wallEle,temp[5:],axis=None)
        else:
            temp = next(mesh).split()

    mesh = iter(open(meshfilename))
    temp = next(mesh).split()

    wallcoorX = []
    wallcoorY = []
    wallEntity = []


    while temp != ['$EndNodes']:
        if temp == ['$Nodes']:
        
            nodeNum = next(mesh).split()
            nodeNum= np.array(nodeNum)
            for j in range(int(nodeNum)):
                temp = next(mesh).split()

                for i in wallEle:
                    if temp[0] == str(i):
                        wallcoorX.append(temp[1])
                        wallcoorY.append(temp[2])
                        wallEntity.append(temp[0])
                        break
            
        else:
            temp = next(mesh).split()
            
    
    ## end of reading mesh from meshfilename.msh
    
    ## convert to float number
    xwall_ = np.zeros(len(wallcoorX))
    ywall_ = np.zeros(len(wallcoorY))
    Entitywall = []

    for i in range(len(wallcoorX)):
        xwall_[i] = float(wallcoorX[i])
        ywall_[i] = float(wallcoorY[i])
        Entitywall.append(int(wallEntity[i]))
    
    return xwall_,ywall_
        
def MeshPointExtraction(xwall_,ywall_,x,y,p):
    ## extract the wall mesh by defining a filter
    ds = 0.0000001
    ds2 = 0.00001

    index = []
    for i in range(len(x)):
        if x[i] > -0.0001 and x[i] < 1.0 and y[i] > -0.08 and y[i] < 0.05:
            for j in range(len(xwall_)):
                if abs(x[i] - xwall_[j]) < ds and abs(y[i] - ywall_[j]) < ds:
                    index.append(i)

                    
                    
    ## quality check
    print(len(xwall_))
    print(len(x[index]))
    print(len(index))
    
    plt.figure(figsize=(20,4))
    plt.plot(xwall_,ywall_,'r-')
    plt.plot(x[index],y[index],'.')
    #plt.plot(xwall_,ywall_,'r.')


    #plt.xlim([0.96,0.985])
    #plt.ylim([-0.06,-0.04])

    #plt.xlim([0.4,0.6])
    #plt.ylim([-0.08,-0.07])
                    
    xwall = x[index]
    ywall = y[index]
    pwall = p.T[index].T
    
    return xwall,ywall,pwall
