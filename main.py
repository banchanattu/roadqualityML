import numpy as np
import tensorflow as tf
import processfile as DataFile
import datetime
print("hello")


# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

log_dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1,write_graph=True)


filename ='/Users/i827954/isaacproject/roadquality/CaminDiablo/a.csv'

dataFile = DataFile.ProcessFile()
pathName = '/Users/i827954/isaacproject/roadquality/CaminDiablo'

frequecyArrayList, yvalfordirectory  = dataFile.getFrequencyArrayListForFiles(pathName, dataFile.GOOD)

anninputsize = 1000
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(500, input_shape=(1000,), activation='relu'),
  tf.keras.layers.Dense(500,  activation='relu'),
tf.keras.layers.Dense(1,  activation='softmax')
])

# frequecyArrayList = [[1,2,3,4,5,6,7,8,9],
#          [2,3,4,5,6,7,8,9,0],
#          [5,6,7,8,9,0,4,5,6]]
# yvalfordirectory = [0,1,1]

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'mse'])
print frequecyArrayList.shape, yvalfordirectory.shape
model.fit(frequecyArrayList,yvalfordirectory, epochs=1000, batch_size=128, callbacks=[tensorboard_callback])

