import numpy as np


def sigmoid(soma):
    return float(1.0 / (1.0 + np.exp(-soma)))


entradas = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

saidas = np.array([
    [0],
    [1],
    [1],
    [0]
])


pesos0 = np.array([
    [-0.424, -0.740, -0.961],
    [0.358, -0.577, -0.469]
])

epocas = 100

for j in range(epocas):
    print(j)






































