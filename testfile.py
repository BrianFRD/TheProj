import numpy as np

def leaky_relu(x):
    return np.maximum(0.2 * x, x)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sq(x):
    return x ** 2
    