import numpy as np




def MagnetopauseR(t,Rsm):
	'''
	Determine the magnetopause radial coordinate for a given angle theta
	
	Inputs
	======
	t : float
		Angle between the x-MSM axis and the line connecting the centre
		of Mercury's dipole to the position being tested (rads)
	Rsm : float
		Magnetopause standoff distance, R_m
		
	Returns
	=======
	Rsm : float
		Radial coordinate of the magnetopause at theta. (R_m)
	
	'''
	
	return Rsm*np.sqrt(2.0/(1.0 + np.cos(t)));
