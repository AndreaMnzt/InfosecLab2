from binning_encoder import *
import numpy as np
from numpy.random import rand

def randomBinningEncoder(u):
    """return a random codeword of the message u

    Args:
        u (np.array of 3 bits): message to encode

    Returns:
        codeword (np.array of 7 bits): codeword randomly chosen
    """
    codewords = binningEncoder(u)

    codeword = codewords[ round(rand()) ]  #random generate a number = 0 or 1, 
                                           # so i randomly chose the codeword
    
    return codeword

