import numpy as np
import math as m
import random as r

class Results:
    def __init__(self, array, errors):
        self.array = array
        self.errors = errors

def BSC(message, error):
    mean = len(message) * error
    variance = mean * (1 - error)
    standard_dev = m.sqrt(variance)
    number_errors = np.random.normal(mean, standard_dev)
    user_message = np.array(message)
    flag_array = np.zeros(len(message))
    x = int(number_errors) if (number_errors - int(number_errors)) < 0.5 else int(number_errors) + 1
    x = 0 if x < 0 else x
    #print(x)
    for i in range(x):
        position = r.randint(0, len(user_message) - 1)
        if flag_array[position] == 0:
            user_message[position] = 1 if user_message[position] == 0 else 0
            flag_array[position] = -1
        else:
            i = i - 1
    return Results(user_message, x)


