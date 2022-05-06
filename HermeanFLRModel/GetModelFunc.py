import numpy as np
from . import Coeffs

def GetModelFunc(Alpha):
	'''
	Return a function which can be used to calculate the model given
	a value of alpha.
	
	'''
	if isinstance(Alpha,str):
		#use the variable alpha version
		
		def ModelFunc(Req,Rnorm):
			
			#use the interpolation object to get alpha
			alpha = Coeffs.fAlphaR(Req)
			
			#get rho_eq
			rho_eq = Coeffs.fRhoEq(Req)
			
			#calculate PMD 
			rho = rho_eq*Rnorm**-alpha
			
			return rho
		
		return ModelFunc
		
	else:
		#use fixed alpha
		a = Coeffs.fa(Alpha)
		k = Coeffs.fk(Alpha)
		
		
		def ModelFunc(Req,Rnorm):
			
			#get rho_eq
			rho_eq = a*Req**k
			
			#now pmd
			rho = rho_eq*Rnorm**-Alpha
			
			return rho
			
		return ModelFunc
