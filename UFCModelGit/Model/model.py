#imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import ModelCheckpoint, EarlyStopping

df = pd.read_csv('traindata.csv')
df.head()

#drop nan
df = df.dropna(inplace=False)


#dropping referee
df = df.drop('referee', axis=1)

#one hot encoding all columns that are representing a string numerically
#one hot encode Billings
df_encoded = pd.get_dummies(df, columns=['billing'], prefix='billing').astype(int)
df = df.drop('billing', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode redCorner_nation
df_encoded = pd.get_dummies(df, columns=['redCorner_nation'], prefix='redCorner_nation').astype(int)
df = df.drop('redCorner_nation', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode blueCorner_nation
df_encoded = pd.get_dummies(df, columns=['blueCorner_nation'], prefix='blueCorner_nation').astype(int)
df = df.drop('blueCorner_nation', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode venue
df_encoded = pd.get_dummies(df, columns=['venue'], prefix='venue').astype(int)
df = df.drop('venue', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#remove draws
df['blueCorner'] = 1
df = df[df['winner'] != 1]
df['winner'] = df['winner'].replace(2, 1)

#x,y split
target_column = 'winner'
y = df[target_column]
X = df.drop(target_column, axis=1)

#create train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Define the deep learning model
model = Sequential()
model.add(Dense(64, activation = 'relu'))
model.add(Dense(32, activation = 'relu'))
model.add(Dense(16, activation = 'relu'))
model.add(Dense(1, activation='sigmoid'))

#earlyStopping
earlystopping = EarlyStopping(monitor='val_loss', patience=100, restore_best_weights=True)

# Define the ModelCheckpoint callback
checkpoint = ModelCheckpoint(filepath='best_model_weights.h5', save_weights_only=True, monitor='val_accuracy', save_best_only=True, verbose=1)

#compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train
model.fit(X_train, y_train, epochs=1000, batch_size=124, validation_data=(X_test, y_test), callbacks=[checkpoint, earlystopping])


#accuracy
y_hat = model.predict(X_test)
y_hat = [0 if val<0.5 else 1 for val in y_hat]
print(f'Accuracy: {accuracy_score(y_test,y_hat)}')

#Highest accuracy: 0.8864013266998342 - 01.17.2023
#Latest accuracy: 0.8814262023217247 - 01.17.2023