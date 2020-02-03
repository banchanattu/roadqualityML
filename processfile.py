import csvreader as CSV
import math as MATH
import calculatedft as DFT
import os
import numpy as np
class ProcessFile:
    fileName= ""
    GOOD = 1
    BAD = 0
    # Read the csv file and returns an array of magnitued of accelerator value
    def getMagnitudeData(self, fileName):
        csvfile = CSV.CSVReader(fileName, 30, 1)
        csvfile.intilializeXYZArrayFromCSV()

        X = csvfile.getXArray()
        Y = csvfile.getYArray()
        Z = csvfile.getZArray()

        length = len(X)
        MAG = [0] * length
        for i in range(0, length - 1, 1):
            MAG[i] = MATH.sqrt(X[i] ** 2 + Y[i] ** 2 + Z[i] ** 2)
        dftcalculator = DFT.DFTCalculator()

        frequencies = dftcalculator.getRealPartArray( dftcalculator.getFrequencyData(MAG))
        return frequencies[:1000];

    # For a given directory read each file and return an array of array of frequencies
    def getFrequencyArrayListForFiles(self, directoryPathName, roadCondition):
        dirlist = os.listdir(directoryPathName)
        frequecyArrayList = [[]]*len(dirlist)
        yvalarray = []
        for i in range(len(dirlist)):
            frequecyArrayList[i] = self.getMagnitudeData(directoryPathName + "/" + dirlist[i]);
        if roadCondition == self.GOOD:
            yvalarray = [1]*len(dirlist)

        return frequecyArrayList, yvalarray;


