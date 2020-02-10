import numpy as np
import tensorflow as tf
import processfile as DataFile
import datetime


# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

log_dir="logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1,write_graph=True)


#filename ='/Users/i827954/isaacproject/roadquality/CaminDiablo/a.csv'

dataFile = DataFile.ProcessFile()
pathName = '/Users/i827954/isaacproject/roadquality/CaminDiablo'
pathdata = [
            ['/Users/i827954/isaacproject/roadquality/CaminDiablo', dataFile.BAD ],
            ['/Users/i827954/isaacproject/roadquality/GreatValleyPkwy', dataFile.GOOD],
            ['/Users/i827954/isaacproject/roadquality/GrandLine1', dataFile.BAD],
            ['/Users/i827954/isaacproject/roadquality/GrandLine2', dataFile.BAD],
            ['/Users/i827954/isaacproject/roadquality/MtnHouseToGreatValley', dataFile.BAD]
            ];

#frequecyArrayList, yvalfordirectory  = dataFile.getFrequencyArrayListForFiles(pathName, dataFile.GOOD)
frequecyArrayList = []
yvalfordirectory = []

for i in range(len(pathdata)):
  frequecyArrayList1, yvalfordirectory1 = dataFile.getFrequencyArrayListForFiles(pathdata[i][0], pathdata[i][1])
  frequecyArrayList = frequecyArrayList + frequecyArrayList1
  yvalfordirectory = yvalfordirectory + yvalfordirectory1

anninputsize = 1000
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(400, input_shape=(300,), activation='relu'),
  tf.keras.layers.Dense(500,  activation='relu'),
tf.keras.layers.Dense(1,  activation='relu')
])

# frequecyArrayList = [[1,2,3,4,5,6,7,8,9,10],
#          [2,3,4,5,6,7,8,9,0,10],
#          [5,6,7,8,9,0,4,5,6,10]]
# yvalfordirectory = [1,1,1,1,1,1]

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', 'mse'])
print np.asanyarray(frequecyArrayList).shape
    #, yvalfordirectory.shape
#x_val = tf.convert_to_tensor(frequecyArrayList)
x_val = np.asarray(frequecyArrayList)
y_val = np.asarray(yvalfordirectory)
#y_val = np.asarray([0,0,1,1,1,1])
model.fit(x_val, y_val,epochs=1000, batch_size=128, callbacks=[tensorboard_callback])

