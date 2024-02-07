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

df = pd.read_csv('traindata2.csv')

dfMock = pd.read_csv('mockTestData.csv')

df = df.dropna(inplace=False)

dfMock = dfMock.dropna(inplace=False)

#dropping referee
df.drop('referee', axis=1, inplace=True)

#drop billings
df.drop('billing', axis=1, inplace=True)

#drop venue
df.drop('venue', axis=1, inplace=True)

#drop title_fight
df.drop('title_fight', axis=1, inplace=True)

df.rename(columns={'fightTime': 'redCorner_fightTime'}, inplace=True)
df.insert(32, 'blueCorner_fightTime', df['redCorner_fightTime'])

#one hot encode redCorner_nation
column = dfMock[['redCorner_nation']].copy()
df_encoded = pd.get_dummies(column, columns=['redCorner_nation'], prefix='redCorner_nation').astype(int)
df.drop('redCorner_nation', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode blueCorner_nation
column = dfMock[['blueCorner_nation']].copy()
df_encoded = pd.get_dummies(column, columns=['blueCorner_nation'], prefix='blueCorner_nation').astype(int)
df.drop('blueCorner_nation', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode redCorner_stance
column = dfMock[['redCorner_stance']].copy()
df_encoded = pd.get_dummies(column, columns=['redCorner_stance'], prefix='redCorner_stance').astype(int)
df.drop('redCorner_stance', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

#one hot encode blueCorner_stance
column = dfMock[['blueCorner_stance']].copy()
df_encoded = pd.get_dummies(column, columns=['blueCorner_stance'], prefix='blueCorner_stance').astype(int)
df.drop('blueCorner_stance', axis=1, inplace=True)
df = pd.concat([df, df_encoded], axis=1)

df['blueCorner'] = 1
df['winner'] = df['winner'].replace(2, 1)

#one hot encode redCorner_nation
column = dfMock[['redCorner_nation']].copy()
df_encoded = pd.get_dummies(column, columns=['redCorner_nation'], prefix='redCorner_nation').astype(int)
dfMock.drop('redCorner_nation', axis=1, inplace=True)
dfMock = pd.concat([dfMock, df_encoded], axis=1)

#one hot encode blueCorner_nation
column = dfMock[['blueCorner_nation']].copy()
df_encoded = pd.get_dummies(column, columns=['blueCorner_nation'], prefix='blueCorner_nation').astype(int)
dfMock.drop('blueCorner_nation', axis=1, inplace=True)
dfMock = pd.concat([dfMock, df_encoded], axis=1)

#one hot encode redCorner_stance
column = dfMock[['redCorner_stance']].copy()
df_encoded = pd.get_dummies(column, columns=['redCorner_stance'], prefix='redCorner_stance').astype(int)
dfMock.drop('redCorner_stance', axis=1, inplace=True)
dfMock = pd.concat([dfMock, df_encoded], axis=1)

#one hot encode blueCorner_stance
column = dfMock[['blueCorner_stance']].copy()
df_encoded = pd.get_dummies(column, columns=['blueCorner_stance'], prefix='blueCorner_stance').astype(int)
dfMock.drop('blueCorner_stance', axis=1, inplace=True)
dfMock = pd.concat([dfMock, df_encoded], axis=1)


#when one hot encoding, nations that have no representation in the train set have Nan values. This sets them to zero as they would have been zero if they were represented
df.fillna(0, inplace=True)

df = df.dropna(inplace=False)

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
checkpoint = ModelCheckpoint(filepath='best_model_weights2.h5', save_weights_only=True, monitor='val_accuracy', save_best_only=True, verbose=1)

#compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train
model.fit(X_train, y_train, epochs=1000, batch_size=124, validation_data=(X_test, y_test), callbacks=[checkpoint, earlystopping])

#limiting the test data to about 2021 as career stats are from 2024 for accuracy purposes
dfMock = dfMock.iloc[:1263]


#testing the model using career statistics

# x, y split for dfMock
target_column = 'winner'
y_mock = dfMock[target_column]
X_mock = dfMock.drop(target_column, axis=1)

#accuracy
y_hat = model.predict(X_mock)
y_hat = [0 if val<0.5 else 1 for val in y_hat]
print(f'Accuracy: {accuracy_score(y_mock,y_hat)}')

#0.6587490102929533

