#This program will read a CSV file and print output

#import the library for CSV reading since we need to use them 
import csv

class CSVReader:
	#Array to use the X directional accelerator value
	Xarray = [] 
	#Array to use the Y directional accelerator value
	Yarray = []
	#Array to use the Z directional accelerator value
	Zarray = []

	Iarray = []
	samplerate = 0.00
	samplingperiod = 0.00
	#Fundamental Frequency
	F0 = 0.00
    
	datafilename = ""
    
	def __init__(self, filename, sampling_rate, distance):
		'''
		Constructor
		'''
		self.samplerate = sampling_rate
		self.samplingperiod = 1.0/self.samplerate
		self.datafilename = filename
		self.T = 0
		self.D = distance
		self.S = 0
     
	#defining a function to read and initialize data from CSV
	def intilializeXYZArrayFromCSV(self):
		row_counter = 0
		with open(self.datafilename) as csvDataFile:
			csvReader = csv.reader(csvDataFile, delimiter=';')
			print csvDataFile
			for row in csvReader:
				#Since first line is the header, ignore 0th row
				if  row_counter > 2 :
					self.Iarray.append(float(row_counter))
					self.Xarray.append(float(row[1]))
					self.Yarray.append(float(row[2]))
					self.Zarray.append(float(row[3]))
				row_counter = row_counter + 1
			#T is the experiment time
        	self.T = self.samplingperiod * row_counter
        	#F0 is the fundamental frequency
        	self.F0 = 1.0/self.T
        	self.S  = self.D/self.T
		return
	
	def getXArray(self):
   		return self.Xarray[:600]
   
	def getYArray(self):
		return self.Yarray[:600]

	def getZArray(self):
		return self.Zarray[:600]
	
	def getIArray(self):
		frequencyArray = []
		for x in self.Iarray:
			frequencyArray.append(x * self.F0)
		return frequencyArray[:len(frequencyArray)/2]
		
	def convertFrequencyToDistanace(self, AR):
		distanceArray = []
		for x in AR:
			distanceArray.append(self.S*-1.0/x)
		
		return distanceArray
	
	def getFundamentalFrequency(self):
		return self.F0
		
	def getAverageSpeed(self):
		return self.S
		
	def getDistance(self):
		return self.D
		
	def getExperimentTime(self):
		return self.T
		
		