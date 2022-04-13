import numpy as np


#these are the coefficients provided in the paper.
#table 1: 
#alpha is the power law
alpha = np.array([0,1,2,3,4,5,6])
#a and k define the power law fitted to rho_eq and R_eq
#(equation 4)
a = np.array([461.0,450.0,440.0,429.0,418.0,407.0,396.0])
k = np.array([-7.5,-7.5,-7.5,-7.6,-7.6,-7.7,-7.7.])

#table 2 could be used instead, though it would be a bit risky
Req = np.array([1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85])
alphav = np.array([7.65,8.95,9.25,6.55,7.15,10.55,0.05,-1.05])
rhoeq = np.array([279.0,99.0,39.0,35.0,18.0,5.0,18.0,14.0])
