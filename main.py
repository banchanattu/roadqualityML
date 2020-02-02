import numpy as np
import tensorflow as tf
import csvreader as CSV
import math as MATH
import calculatedft as DFT
print("hello")

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

filename ='/Users/i827954/isaacproject/roadquality/CaminDiablo/a.csv'
csvfile = CSV.CSVReader(filename,30, 1)
csvfile.intilializeXYZArrayFromCSV()

X = csvfile.getXArray()
Y = csvfile.getYArray()
Z = csvfile.getZArray()

length = len(X)
MAG = [0] * length
for i in range(0, length-1, 1):
    MAG[i] = MATH.sqrt(X[i] ** 2 + Y[i] ** 2 + Z[i] ** 2)
dftcalculator = DFT.DFTCalculator()

frequencies = dftcalculator.getFrequencyData(MAG)
anninputsize = 1000
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(anninputsize, input_shape=(2,), activation='relu'),
  tf.keras.layers.Dense(500,  activation='relu'),
tf.keras.layers.Dense(1,  activation='softmax')
])

print len(frequencies)