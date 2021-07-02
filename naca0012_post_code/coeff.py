import basis

import numpy as np
import math
from math import pi


# CL and CD

#Time-averaged pressure coefficient
def cal_cp_cl_cd(p,x,y,time):
    
    deg = pi/60
    T = 0.12
    
    xaero,yaero = basis.rotate(x,y,deg)
    
    
    
    x_temp = np.zeros(len(xaero))
    for i in range(len(x_temp)):
        if y[i] != 0:
            x_temp[i] = xaero[i]*yaero[i]/abs(yaero[i])

    index1 = np.argsort(x_temp)
    xt = basis.swap_1d(xaero,index1)
    yt = basis.swap_1d(yaero,index1)
    
    
    
    theta = - basis.aerfoiltool(xt,yt) - deg
    
    #theta = basis.swap_1d(theta,index1)
    p_coe = basis.swap(p,index1)
    
    dA = basis.cal_area(xt,yt)

    ## calculate Cl Cd
    cd = np.zeros(len(time))
    cl = np.zeros(len(time))
    cp = np.zeros(p_coe.shape[1])
    for i in range(len(time)):
        temp1 = 0
        temp2 = 0
        for j in range(len(theta)):
            temp1 += (p_coe[i][j]-1/1.4)*np.sin(theta[j])*dA[j]
            temp2 += (p_coe[i][j]-1/1.4)*np.cos(theta[j])*dA[j]
        cp += p_coe[i] - 1/1.4
        cl[i] = temp1
        cd[i] = temp2

    cl = cl/(0.5*1*0.3**2)/np.sum(dA)
    cd = cd/(0.5*1*0.3**2)/np.sum(dA)
    cp = cp/len(time)/(0.5*1*0.3**2)
   
    print(np.sum(dA))
    return cd,cl,cp,xt,yt,theta
