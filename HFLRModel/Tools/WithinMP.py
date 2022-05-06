import numpy as np
from .MagnetopauseR import MagnetopauseR

def WithinMPRT(r,t,Rsm):
	'''
	Determine whether vector(s) are within the magnetopause.
	
	Inputs
	======
	r : float
		Radial coordinate (R_m, MSM)
	t : float
		Angle between the x-MSM axis and the line connecting the centre
		of Mercury's dipole to the position being tested (rads)
	Rsm : float
		Magnetopause standoff distance, R_m
		
	Returns
	=======
	out : bool
		True if within the magnetopause
	
	'''
	
	Rmp = MagnetopauseR(t,Rsm)
	
	return r <= Rsm
		



def WithinMP(x,y,z,Rsm):
	'''
	Determine whether vector(s) are within the magnetopause.
	
	Inputs
	======
	x : float
		x-coordinate (R_m, MSM)
	y : float
		y-coordinate (R_m, MSM)
	z : float
		z-coordinate (R_m, MSM)
	Rsm : float
		Magnetopause standoff distance, R_m
		
	Returns
	=======
	out : bool
		True if within the magnetopause
	
	'''
	
	rho2 = y*y + z*z
	r2 = x*x + rho2
	rho = np.sqrt(rho2)
	r = np.sqrt(r2)
	t = np.arctan2(rho,x)
	
	return WithinMPRT(r,t,Rsm)
