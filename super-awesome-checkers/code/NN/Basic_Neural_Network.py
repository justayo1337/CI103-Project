# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:23:41 2021

@author: Jake
"""

import tensorflow as tf
import numpy as np
import pandas as pd
from tensorflow.keras import datasets, layers, models

data=[
      1,1,1,1,
      1,1,1,1,
      1,1,1,1,
      0,0,0,0,
      0,0,0,0,
      -1,-1,-1,-1,
      -1,-1,-1,-1,
      -1,-1,-1,-1
      ]
data2=[
      1,1,1,1,
      1,1,1,1,
      1,1,1,1,
      0,0,0,0,
      0,0,0,0,
      -1,-1,-1,-1,
      -1,-1,-1,-1,
      -1,-1,-1,-1
      ]

label=[
      1,1,1,1,
      1,1,1,1,
      1,1,1,1,
      0,0,0,0,
      0,0,0,1,
      1,1,1,0,
      1,1,1,1,
      1,1,1,1
      ]



model = models.Sequential()
model.add(tf.keras.Input(shape=(32,1),name="Input"))
model.add(layers.Dense(8,activation='relu'))
model.add(tf.keras.layers.Dense(32))



model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

history = model.fit(data, label, epochs=5)


predictions = model.predict(data2)
print(len(predictions))
"""
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
"""
