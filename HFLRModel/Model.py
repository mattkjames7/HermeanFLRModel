import numpy as np
from .Tools.MSOtoFLC import MSMtoFLC,MSOtoFLC
from .GetModelFunc import GetModelFunc

def _DummyConv(*args):
	'''
	Dummy conversion function
	
	'''
	Re,M,Rn = args
	return Re,M,Rn


class Model(object):
	def __init__(self,Alpha,Coords='MSM'):
		'''
		Initialize a Model object instance. 
		
		Inputs
		======
		Alpha : float|str
			Power law value (between 0 and 6) or 'variable' to use a 
			questionable variable alpha.
		Coords : str
			Define the input coordinate system.
			'MSM' : Mercury solar magnetospheric coordinates (x,y,z)
			'MSO' : Mercury solar orbital coordinates (x,y,z)
			'FLC' : Field line coordinates (Req,MLTe,Rnorm)
		
		'''

		#set the coordinate conversion function
		if Coords == 'FLC':
			#use dummy function
			self.CoordConv = _DummyConv
		elif Coords == 'MSO':
			# use MSOtoFLC
			self.CoordConv = MSOtoFLC 
		else:
			# use MSMtoFLC
			self.CoordConv = MSMtoFLC

		
		
		#set the model parameters and model function
		self.ModelFunc = GetModelFunc(Alpha)
		
	def Calc(self,*args):
		'''
		Calculate the model plasma mass density (amu cm^-3)
		
		Inputs
		======
		*args : arguments list
			Should be three inputs - the coordinate system depends on
			the "Coords" keyword used when initializing the object.
			
		Returns
		=======
		rho : float
			Plasma mass density (amu cm^-3)
		
		'''
		#convert coordinates
		Req,MLT,Rnorm = self.CoordConv(*args)
		
		#calculate model
		return self.ModelFunc(Req,Rnorm)
