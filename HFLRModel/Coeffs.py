import numpy as np
from scipy.interpolate import interp1d


#these are the coefficients provided in the paper.
#table 1: 
#alpha is the power law
alpha = np.array([0,1,2,3,4,5,6])
#a and k define the power law fitted to rho_eq and R_eq
#(equation 4)
a = np.array([461.0,450.0,440.0,429.0,418.0,407.0,396.0])
k = np.array([-7.5,-7.5,-7.5,-7.6,-7.6,-7.7,-7.7])

#interpolation objects
fa = interp1d(alpha,a,bounds_error=False,fill_value='extrapolate')
fk = interp1d(alpha,k,bounds_error=False,fill_value='extrapolate')


#table 2 could be used instead, though it would be a bit risky
Req = np.array([1.15,1.25,1.35,1.45,1.55,1.65,1.75,1.85])
alphav = np.array([7.65,8.95,9.25,6.55,7.15,10.55,0.05,-1.05])
rhoeq = np.array([279.0,99.0,39.0,35.0,18.0,5.0,18.0,14.0])

#interpolation object for variable alpha
fAlphaR = interp1d(Req,alphav,bounds_error=False,fill_value='extrapolate')

#approximate fit to rhoeq (fitted in log space)
def fRhoEq(Req):
	'''
	Function to esimate equatorial plasma mass density with radial at a
	radial distance (L-shell). It is a power law fit to Req and rhoeq.
	
	This function was found using scipy.optimize.curve_fit with initial
	parameters of a = 450 and k = -7.7.
	
	'''
	
	a = 1347.46354651
	k = -11.33556141
	return a*Req**k
