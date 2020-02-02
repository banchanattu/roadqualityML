#This file contains the calculation of DFT



import numpy as np
import numpy.fft as FFT

class DFTCalculator:

	'''
    classdocs
    '''
     
	def __init__(self):
	   '''
        Constructor
       '''
       
	def getRealPartArray(self,X):
		retX = []
		for i in X:
			retX.append(np.real(i));
		retX[0] = 0
		return retX

	def getMagnitude(self, X ):
		retX = [];
		retX = abs(X)/len(X)
		retX[0] = 0
		return retX
	
	def getFrequencyData(self, X):
		dataarray = FFT.fft(X)
		return dataarray[:len(dataarray)/2]
		
	def getFrequencyArray(self, n):
		dataarray = FFT.fftfreq(n,1.0/30)
		return dataarray[:len(dataarray)/2]
		

			
			


