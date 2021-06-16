# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense



dataset = loadtxt('optimal.csv', delimiter=',')

#print(dataset)

# split into input (X) and output (y) variables
x = dataset[:,0:11]
y = dataset[:,11]
print(x)

model = Sequential()
model.add(Dense(15, input_dim=11, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='Adadelta', metrics=['accuracy'])

model.fit(x, y, epochs=500, batch_size=10)

print(model.evaluate(x, y, verbose=0))
