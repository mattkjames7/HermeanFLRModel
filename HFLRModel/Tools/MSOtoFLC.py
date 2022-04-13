import numpy as np
import KT17

def MSMtoFLC(x,y,z,Rsm=1.42):
	'''
	Convert Mercury Solar Magnetic (MSM) coords to field line 
	coordinates (Req, MLTe and Rnorm). This uses the KT17 model to trace
	each point to the equator.
	
	Inputs
	======
	x : float
		x-coordinate (Rm)
	y : float
		y-coordinate (Rm)
	z : float
		z-coordinate (Rm)
	Rsm : float
		Magnetopause standoff distance (Rm)
	
	Returns
	=======
	Req : float
		Equatorial footprint of the magnetic field line (Rm)
	MLTe : float
		Local time of the equatorial footprint (hours)
	Rnorm : float
		Normalized radial distance along the field line.
	
	'''

	#calculate R
	R = np.sqrt(x*x + y*y + z*z)
	
	#get the traces
	T = KT17.TraceField(x,y,z,Rsm=Rsm)
	
	#get Req and MLTe
	Req = T.Lshell
	MLTe = T.MLTe
	
	#calculate Rnorm
	Rnorm = R/Req
	
	return Req,MLTe,Rnorm
