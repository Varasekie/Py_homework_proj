import numpy as np

np.random.seed(1337)  # for reproducibility
import pandas as pd
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import SimpleRNN, Activation, Dense
from keras.optimizers import Adam

import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

TIME_STEPS = 1  # same as the height of the image
INPUT_SIZE = 2  # same as the width of the image
BATCH_SIZE = 15
BATCH_INDEX = 0
OUTPUT_SIZE = 2
CELL_SIZE = 2
LR = 0.00001
# filename = 'D:\\learning\\20MCM\\data\\2021_MCM_Problem_C_Data\\2021MCMProblemC_DataSet.xls'
# train
filename = 'D:\\learning\\20MCM\\data\\data_10_train.xls'

filename_test = 'D:\\learning\\20MCM\\data\\data_near.xls'
# filename = 'C:\\Users\\86139\\Desktop\\data.xls'
# read train
longitude = pd.read_excel(filename)
x1_name = 'Latitude'
x2_name = 'Longitude'
isNot = 'Lab Status'
# for i in range(18):
X1_train = longitude[x1_name]
x2_train = longitude[x2_name]
isNot_train = longitude[isNot]
# num = len(x1)
X_train = [[],[]]
# y_train = [[],[]]
# for i in range(len(isNot_train)):
#     if isNot_train[i] == 0:
#         X_train[0].append(X1_train[i])
#         X_train[1].append(X1_train[i])
#     else:
#         y_train[0].append(X1_train[i])
#         y_train[1].append(X1_train[i])

X_train = np.array(X_train)
# print(X_train)
y_train = np.array(isNot_train)

# read test
test = pd.read_excel(filename_test)
x1_test = test[x1_name]
x2_test = test[x2_name]
isnot_test = test[isNot]

X_test = [[],[]]
y_test = [[],[]]
for i in range(len(isNot_train)):
    if isNot_train[i] == 0:
        X_test[0].append(X1_train[i])
        X_test[1].append(X1_train[i])
    else:
        y_test[0].append(X1_train[i])
        y_test[1].append(X1_train[i])
X_test = np.array(X_test)
# print(X_train)
y_test = np.array(y_test)


X_train = X_train.reshape(-1, 1, 2) / 180.  # normalize
X_test = X_test.reshape(-1, 1, 2) / 180.  # normalize
y_train = np_utils.to_categorical(y_train, num_classes=2)
y_test = np_utils.to_categorical(y_test, num_classes=2)

# build RNN model
model = Sequential()

# RNN cell
model.add(SimpleRNN(
    # for batch_input_shape, if using tensorflow as the backend, we have to put None for the batch_size.
    # Otherwise, model.evaluate() will get error.
    batch_input_shape=(BATCH_SIZE, TIME_STEPS, INPUT_SIZE),  # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
    units=CELL_SIZE,
))

# output layer
model.add(Dense(OUTPUT_SIZE))
model.add(Activation('softmax'))

# optimizer
adam = Adam(LR)
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# training
for step in range(len(X_train)):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch = X_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :, :]
    Y_batch = y_train[BATCH_INDEX: BATCH_INDEX + BATCH_SIZE, :]
    cost = model.train_on_batch(X_batch, Y_batch)
    BATCH_INDEX += BATCH_SIZE
    BATCH_INDEX = 0 if BATCH_INDEX >= X_train.shape[0] else BATCH_INDEX

    if step % 500 == 0:
        cost, accuracy = model.evaluate(X_test, y_test, batch_size=y_test.shape[0], verbose=False)
        print('test cost: ', cost, 'test accuracy: ', accuracy)
