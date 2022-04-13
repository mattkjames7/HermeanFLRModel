import numpy as np
from .Tools.MSOtoFLC import MSMtoFLC,MSOtoFLC

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
		
		
		#set the model parameters and model function
