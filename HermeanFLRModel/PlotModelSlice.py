import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from .Model import Model
from .Tools.WithinMP import WithinMP
from .Tools.PlotPlanet import PlotPlanetYZ
import DateTimeTools as TT


def PlotModelSlice(mlt,Alpha,fig=None,maps=[1,1,0,0],zlog=True,
					scale=[1.0,500.0],dr=0.05,dz=0.05,zrange=[-2.0,2.0],
					Rsm=1.42):
	'''
	Plot the density for slice of the magnetosphere at some magnetic 
	local time.
	
	Inputs
	======
	mlt : float
		Magnetic local time (hours)
	Alpha : float|str
		Power law exponent (0-6). Can be 'variable' if youw ant to try 
		the dodgy variable model.
	fig : None|obj
		None : new figure is created
		matplotlib.pyplot : use existing plot window, new subplot
		pyplot.Axes : use existing subplot.
	maps : list
		4-element list [xmaps,ymaps,xmap,ymap] denoting the number of 
		subplots horizontally (xmaps) and vertically (ymaps) and their 
		positions (xmap,ymap)
	zlog : bool
		Logarithmic color axis
	scale : float
		2-element array defining the color scale limits
	dr : float
		radial grid size (R_m)
	dz : float
		z-axis grid size (R_m)
	zrange : list
		2-element array defining the z axis range
	Rsm : float
		Subsolar standoff distance of the magnetopause
		
	
	
	'''

	nz = np.int32(np.round((zrange[1]-zrange[0])/dz))
	zaxis = np.arange(nz+1)*dz + zrange[0]
	zcent = np.arange(nz)*dz + zrange[0] + 0.5*dz
	
	
	rmp = 1.42*(2.0/(1.0 + np.cos((mlt-12.0)*15.0*np.pi/180.0)))**0.5
	rrange = [0.0,dr*(np.ceil(rmp/dr))]
	nr = np.int32(np.round((rrange[1]-rrange[0])/dr))
	raxis = np.arange(nr+1)*dr + rrange[0]
	rcent = np.arange(nr)*dr + rrange[0] + 0.5*dr
	
	#grid of positions
	rg,zg = np.meshgrid(rcent,zcent)	
	
	
	xg = -rg*np.cos(mlt*np.pi/12)
	yg = -rg*np.sin(mlt*np.pi/12)

	
	#calculate the density
	model = Model(Alpha,'MSM')
	rho = model.Calc(xg.flatten(),yg.flatten(),zg.flatten()).reshape((nz,nr))

	#work out which positions are from within the MP
	wmp = WithinMP(xg.flatten(),yg.flatten(),zg.flatten(),Rsm).reshape((nz,nr))
	good = np.where((wmp) | (wmp == False))
	
	#create the grid to be plotted
	xg,yg = np.meshgrid(raxis,zaxis)
	grid = np.zeros((nz,nr),dtype='float32')+np.nan
	grid[good] = rho[good]


	#get the scale
	if scale is None:
		if zlog:
			scale = [np.nanmin(grid[grid > 0]),np.nanmax(grid)]
		else:
			scale = [np.nanmin(grid),np.nanmax(grid)]
	
	#z label
	if zlog:
		ztitle = 'Density log$_{10}$(amu cm$^{-3}$)'
	else:
		ztitle = 'Density (amu cm$^{-3}$)'
	
	#set norm
	if zlog:
		norm = colors.LogNorm(vmin=scale[0],vmax=scale[1])
	else:
		norm = colors.Normalize(vmin=scale[0],vmax=scale[1])	
	

	
	if fig is None:
		fig = plt
		fig.figure()
	if hasattr(fig,'Axes'):	
		ax = fig.subplot2grid((maps[1],maps[0]),(maps[3],maps[2]))
	else:
		ax = fig
		
	sm = ax.pcolormesh(xg,yg,grid,cmap='gnuplot',norm=norm)

	ax.set_aspect(1.0)
	ax.set_xlim(0.0,zrange[1]-zrange[0])
	ax.set_ylim(zrange[0],zrange[1])
	ax.set_xlabel(r'$\rho$ ($R_M$)',size='large')
	ax.set_ylabel('$z$ ($R_M$)',size='large')

	PlotPlanetYZ(ax,1.0,[0.0,0.0,-0.19],zorder=3.0)
	
	hh,mm,_,_ = TT.DectoHHMM(mlt)
	mltstr = '{:02d}:{:02d} MLT'.format(hh[0],mm[0])
	ax.text(0.02,0.99,mltstr,ha='left',va='top',transform=ax.transAxes)

	divider = make_axes_locatable(ax)
	cax = divider.append_axes("right", size="5%", pad=0.05)

	cbar = plt.colorbar(sm,cax=cax) 
	cbar.set_label(ztitle)
	
	return ax
