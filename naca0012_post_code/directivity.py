import numpy as np



def plot_routine(rr,theta,r,varible):
    theta_plot1 = np.asarray([])
    r_plot1 = np.asarray([])
    varible_plot = np.asarray([])
    tol = 0.03
    for i in range(len(r)):
        if abs(rr[i] - 3) <= tol:
            theta_plot1 = np.concatenate((theta_plot1,theta[i]),axis=None)
            r_plot1 = np.concatenate((r_plot1,r[i]),axis=None)
            varible_plot = np.concatenate((varible_plot,varible[i]),axis=None)
    return varible_plot,theta_plot1
