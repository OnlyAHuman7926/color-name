print("Program started")

import pandas as pd
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

print("Importing finished!")

data = pd.read_csv("data.csv", sep=',')

X = data[['Red', 'Green', 'Blue']]
Y = data[[str(i) for i in range(11)]]

print(X)
print(Y)

trainX, testX, trainY, testY = train_test_split(X, Y, test_size=0.1, random_state=114)

model = Sequential()
model.add(Input(shape=(trainX.shape[1],)))
model.add(Dense(6, activation="relu"))
model.add(Dense(9, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(11, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(trainX, trainY, batch_size = 16, epochs=500, verbose=1)

score = model.evaluate(testX, testY, verbose=1)
print("Percentage Accuracy:", score[1] * 100)

plt.plot(history.history["loss"])
plt.legend(["Loss"])
plt.ylabel("Loss")
plt.xlabel("Epoch")
plt.show()

import joblib
joblib.dump(model, "model.keras")
print("Saved!")

input()