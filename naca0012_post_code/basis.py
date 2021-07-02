###########################################################################
# This file contains essential codes for Naca 0012 aerofoil post-processing
# protetial bug: section aerofoiltool which returns normal direction (theta) to coeff sub routine
# Zhenyang Yuan 2021-7-2
###########################################################################



import numpy as np
from math import pi
import math


## calculate total, mean, fluctuation pressure values
def fluc_pressure(p,time):
    dp = np.zeros([len(time), len(p[0])])
    dptuda = np.zeros([len(time), len(p[0])])
    dpmean = np.zeros(len(p[0]))
    for i in range(len(time)):
        dp[i] = p[i] - 1/1.4*np.ones(len(p[0]))
        dpmean += dp[i]
    dpmean = dpmean/len(time)
    for i in range(len(time)):
        dptuda[i] = dp[i] - dpmean

    return dp,dpmean,dptuda


## calculate rms values of input time depended arrays
## root mean square
def rms(p,time):
    pms_ = np.zeros(p.shape[1])
    
    for i in range(len(time)):
        pms_ += p[i]**2
            
    pms = pms_/len(time)
    prms = np.sqrt(pms)
    
    return pms, prms
    
# polar coordinate respect to (0,0,0)
def polar_coor(x,y):
    theta =np.arctan2(y,x)
    r = np.sqrt(x**2+y**2)
    return theta,r

# rotation routine
def rotate(x,y,deg):
    # deg = -pi/60    # degree in rad
    #xx = np.zeros(len(x))
    #yy = np.zeros(len(y))
    
    xx = x*np.cos(deg) - y*np.sin(deg)
    yy = x*np.sin(deg) + y*np.cos(deg)
    return xx,yy




def swap(p_coe,index):
    temp = np.zeros([p_coe.shape[0],p_coe.shape[1]])
    for i in range(p_coe.shape[0]):
        for j in range(p_coe.shape[1]):
            temp[i][j] = p_coe[i][j]
    pp_coe = np.zeros([p_coe.shape[0],p_coe.shape[1]])
    for j in range(p_coe.shape[0]):
        for i in range(index.shape[0]):
            pp_coe[j][i] = temp[j][index[i]]
    return pp_coe

def swap_1d(q,index):
    temp = np.zeros(q.shape[0])
    for i in range(q.shape[0]):
        temp[i] = q[i]
    qq = np.zeros(len(temp))
    for j in range(q.shape[0]):
        qq[j] = temp[index[j]]
    return qq

def cal_area(xaero,yaero):
    ## calculate dA
    
    
    a0 = 0.2969
    a1 = -0.126
    a2 = -0.3516
    a3 = 0.2843
    a4 = -0.1015
    
    xx = np.asarray([])
    yy = np.asarray([])
    
    
    xx = np.concatenate((xaero,xaero[0]),axis=None)
    yy = np.concatenate((yaero,yaero[0]),axis=None)
    dA_ = np.zeros(len(xx))
   
    for i in range(len(xx)-1):
        dA_[i] = np.sqrt((xx[i] - xx[i+1])**2+(yy[i] - yy[i+1])**2)
        """
        if xx[i] < 0.98:
            a1 = T/0.2*(a0*xx[i]**1.5/1.5+a1*xx[i]**2/2+a2*xx[i]**3/3+a3*xx[i]**4/4+a4*xx[i]**5/5)
            j = i + 1
            a2 = T/0.2*(a0*xx[j]**1.5/1.5+a1*xx[j]**2/2+a2*xx[j]**3/3+a3*xx[j]**4/4+a4*xx[j]**5/5)
            dA_[i] = abs(a2-a1)
        else:
            dA_[i] = np.sqrt((xx[i] - xx[i+1])**2+(yy[i] - yy[i+1])**2)"""
        
    
    
    dA = np.zeros(len(yaero))
    for j in range(1,len(yaero)):
        dA[j] = (dA_[j] + dA_[j-1])/2
    return dA





def aerfoiltool(xaero,yaero):
    ### build the NACA aerofoil
    ### refernce web page: http://airfoiltools.com/airfoil/naca4digit?MNaca4DigitForm%5Bcamber%5D=0&MNaca4DigitForm%5Bposition%5D=0&MNaca4DigitForm%5Bthick%5D=12&MNaca4DigitForm%5BnumPoints%5D=200&MNaca4DigitForm%5BcosSpace%5D=0&MNaca4DigitForm%5BcosSpace%5D=1&MNaca4DigitForm%5BcloseTe%5D=0&MNaca4DigitForm%5BcloseTe%5D=1&yt0=Plot
    ### this program is only valid for NACA 00XX aerofoils, note yc = 0 here
    

    ## The constants a0 to a4 are for a 20% thick airfoil. The expression T/0.2 adjusts the constants to the required thickness.
    a0 = 0.2969
    a1 = -0.126
    a2 = -0.3516
    a3 = 0.2843
    a4 = -0.1015

    T = 0.12  ## aerofoil NACA 0012
    
    


    #yt = T/0.2*(a0*xc**0.5+a1*xc+a2*xc**2+a3*xc**3+a4*xc**4)   #thickness respect to x
    
    k = np.zeros(len(xaero))
    theta = np.zeros(len(xaero))
    
    for i in range(len(xaero)):
        if xaero[i] < 0.98:
            if xaero[i] == 0.0:
                theta[i] = 0
            else:
                k[i] = T/0.2*(0.5*a0*xaero[i]**(-0.5)+a1+2*a2*xaero[i]+3*a3*xaero[i]**2+4*a4*xaero[i]**3)  ##slope of the aerofoil surface
                k_t = -1/k[i]
                if yaero[i] > 0 and k_t > 0:
                    
                    theta[i] = np.arctan(k_t)
                    
                elif yaero[i] < 0 and k_t < 0:
                    theta[i] =  -np.arctan(k_t) - pi
                    
                elif yaero[i] > 0 and k_t < 0:
                    theta[i] = np.arctan(k_t) + pi
                    
                elif yaero[i] < 0 and k_t > 0:
                    theta[i] = -np.arctan(k_t)
                    #print(str(xaero[i])+','+str(yaero[i])+','+str(theta[i]*180/pi))
                
                else:
                    print('error')
        else:
            x_c = 0.98 - 0.004*0.98
            y_c = 0
            
            #theta[i] = yaero[i]/abs(yaero[i])*pi + np.arctan2(yaero[i] - y_c , xaero[i] - x_c)
            theta[i] = np.arctan2(yaero[i] - y_c , xaero[i] - x_c)
   
    
    return theta
            
    
    
