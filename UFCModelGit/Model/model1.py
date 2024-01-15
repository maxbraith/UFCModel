#imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense

df = pd.read_csv('traindata.csv')

#columns that need one-hot encoding
columns2encode = ['referee', 'venue', 'billing', 'redCorner_nation', 'blueCorner_nation']

#encode
encoder = OneHotEncoder(sparse=False)
data2encode = df[columns2encode]
encoded_cols = encoder.fit_transform(data2encode)

#create df for encoded columns
encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(columns2encode))

#drop original columns
df.drop(columns2encode, axis=1, inplace=True)

#add enocded columns
df = pd.concat([df, encoded_df], axis=1)

#x,y split
target_column = 'winner'
y = df[target_column]
x = df.drop(target_column, axis=1)

#create train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


# Define the deep learning model
model = Sequential([
    Dense(64, activation='relu', input_shape=(x_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid') 
])

#compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train
model.fit(x_train, y_train, epochs=300, batch_size=124)

#accuracy
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")









