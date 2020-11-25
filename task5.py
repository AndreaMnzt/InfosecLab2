import numpy as np
import math as m
import random as r


def task_5(message, error_bob, error_eve):
    bob_message = noise(message, error_bob)
    eve_message = noise(message, error_eve)
    # print(bob_message)
    #print(len(bob_message))
    return np.vstack((bob_message, eve_message))


def noise(message, error_user):
    mean_user = len(message) * error_user
    variance_user = mean_user * (1 - error_user)
    standard_dev_user = m.sqrt(variance_user)
    number_errors_user = np.random.normal(mean_user, standard_dev_user)
    user_message = message
    flag_array = np.zeros(len(message))
    x = int(number_errors_user) if (number_errors_user - int(number_errors_user)) < 0.5 else int(number_errors_user) + 1
    x = 0 if x < 0 else x
    #print(x)
    for i in range(x):
        position = r.randint(0, len(user_message) - 1)
        if flag_array[position] == 0:
            user_message[position] = 1 if user_message[position] == 0 else 0
            flag_array[position] = -1
        else:
            i = i - 1
    return user_message


#print(task_5(np.repeat(np.array([0, 1]), 1000), 0.001, 0.001))