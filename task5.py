import numpy as np
import math as m
import random as r

class Results:
    def __init__(self, array, errors):
        self.array = array
        self.errors = errors

def BSC(message, error):

    number_errors_binomial=np.random.binomial(len(message), error)

    user_message = np.array(message)

    errors_array=np.random.choice(len(message)-1, number_errors_binomial, replace=False)
    for i in range(len(errors_array)):
        index=errors_array[i]
        user_message[index] = 1 if user_message[index] == 0 else 0

    return Results(user_message, number_errors_binomial)





