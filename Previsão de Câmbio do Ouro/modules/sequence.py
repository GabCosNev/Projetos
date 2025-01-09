import numpy as np

def create_sequences(data, n_steps_in, n_steps_out):
    X, y = [], []

    for i in range(len(data) - n_steps_in - n_steps_out):
        X.append(data[i:i + n_steps_in])
        y.append(data[i + n_steps_in:i + n_steps_in + n_steps_out])
    
    return np.array(X), np.array(y)


def teste():
    print('testando')