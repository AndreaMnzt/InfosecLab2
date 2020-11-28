import numpy as np
import math as m
import random as r

class Results:
    def __init__(self, array, errors):
        self.array = array
        self.errors = errors

def BSC(message, error):
    #mean = len(message) * error
    #variance = mean * (1 - error)
    #standard_dev = m.sqrt(variance)
    #number_errors = np.random.normal(mean, standard_dev)
    number_errors_binomial=np.random.binomial(len(message), error)
    #print(number_errors_binomial)
    #print(number_errors)
    user_message = np.array(message)
    flag_array = np.zeros(len(message))

    #print(x)
    for i in range(number_errors_binomial):
        position = r.randint(0, len(user_message) - 1)
        if flag_array[position] == 0:
            user_message[position] = 1 if user_message[position] == 0 else 0
            flag_array[position] = -1
        else:
            i = i - 1
    return Results(user_message, number_errors_binomial)

    #np.random.choice(n, size=error_bits, replace=False)



