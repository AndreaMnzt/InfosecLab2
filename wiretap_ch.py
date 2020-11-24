import numpy as np 
import math

def computeConfigDistrib(n, max_errors):
    possible_config = np.zeros(max_errors+1)
    for i in range(0, max_errors+1):
        # the number of possible configurations with exactly i errors are (n Choose i)
        config_i = math.comb(n,i)
        possible_config[i] = config_i
    tot_config = possible_config.sum()
    return (possible_config, tot_config)

def computeBitErrorNum(possible_config, tot_config):
    rand_val = np.random.randint(1, tot_config+1)
    error_bits = -1
    for i, config_i in enumerate(possible_config):
        if int(rand_val) <= int(config_i):
            error_bits = i
            break
        else:
            rand_val -= config_i
    return error_bits

def computeMask(n, error_bits):
    error_mask = np.full((n), 0)
    #indexes = random.sample(range(0, n), error_bits)
    indexes = np.random.choice(a=np.arange(n), size=error_bits, replace=False)
    for idx in indexes:
        error_mask[idx] = 1
    return error_mask

def wiretap_channel(x):
    """return a random (y,z) pair given as input x, where x is the sent message and y and z are the received messages by respectively legitimate receiver and eavesdropper

    Args:
        x (np.array): a row vector representation of the given x

    Returns:
        (y,z) ((np.array), (np.array)): a random (y,z) pair
    """
    n = len(x)

    # GENERATE y

    max_errors_y = 1
    (possible_config_y, tot_config_y) = computeConfigDistrib(n, max_errors_y)
    # pick a configuration from the all possible (uniformly distributed)
    # generate a uniformly random configuration with exactly error_bits bits equal to 1
    error_bits_y = computeBitErrorNum(possible_config_y, tot_config_y)
    error_mask_y = computeMask(n, error_bits_y)
    
    y = np.bitwise_xor(x.astype(int), error_mask_y.astype(int))

    # GENERATE z

    max_errors_z = 3
    (possible_config_z, tot_config_z) = computeConfigDistrib(n, max_errors_z)
    # pick a configuration from the all possible (uniformly distributed)
    # generate a uniformly random configuration with exactly error_bits bits equal to 1
    error_bits_z = computeBitErrorNum(possible_config_z, tot_config_z)
    error_mask_z = computeMask(n, error_bits_z)
    
    z = np.bitwise_xor(x.astype(int), error_mask_z.astype(int))
    return (y,z, error_bits_y, error_bits_z)
