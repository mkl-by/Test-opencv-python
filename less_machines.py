import numpy as np


# Функция сигмоида
# для определения значения весов в нейронных сетях

def sigmoid(x, der=False):
    if der:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

# in data
x = np.array([[1, 0, 1],
              [1, 0, 1],
              [0, 1, 0],
              [0, 1, 0]]
             )
# out data
y = np.array([[0, 0, 1, 1]]).T

# делаем случайные числа более определенными
np.random.seed(1)

# инициализируем веса случайным образом со средним 0
syn0 = 2 * np.random.random((3, 1)) - 1

# далее процесс обучения
l1 = []

for iter in range(10000):
    l0 = x
    l1 = sigmoid(np.dot(l0, syn0))
    l1_error = y - l1
    l1_delta = l1_error * sigmoid(l1, True)
    syn0 += np.dot(l0.T, l1_delta)

print(l1)

new = np.array([1, 1, 1])
l1_new = sigmoid(np.dot(new, syn0))
print(l1_new)
