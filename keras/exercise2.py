from keras.models import Model
from keras.layers import Dense, Input

inputTensor = Input(shape=(100,))
H1 = Dense(10, activation='relu')(inputTensor)
H2 = Dense(20, activation='relu')(H1)

output=Dense(1, activation='softmax')(H2)

model = Model(inputs=inputTensor, outputs=output)

model.summary()