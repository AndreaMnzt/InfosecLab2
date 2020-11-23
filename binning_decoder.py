import numpy as np
from utils import *
from binning_encoder import *

def binningDecoder(y):
    """Decoder of a binning hamming code, return the most probable message and the number of corrected bits

    Args:
        y (np.array of bits): codeword to decode

    Returns:
        list: first element is the most probable message
            second element is the number of corrected bits
    """
    u_s = [ stringToBits('001'),
            stringToBits('010'),
            stringToBits('011'),
            stringToBits('100'),
            stringToBits('101'),
            stringToBits('110'),
            stringToBits('111')
            ]

    #initialize counters
    min_hamming_distance = np.inf
    best_u = ''

    #for every possible message
    for j in range(0,len(u_s)):
        codewords = binningEncoder(u_s[j]) #generate the codewords
        for codeword in codewords:  # and for every codeword
            res = np.logical_xor(codeword, y)  # find where there are errors in y wrt the codeword 
            errors = np.sum(res)                # find how many errors there are

            if errors < min_hamming_distance: #if we have the min number of errors
                min_hamming_distance = errors   #min hamming distance is errors 
                best_u = u_s[j]                 #and we find the most probable trasmitted message

    return best_u, min_hamming_distance



