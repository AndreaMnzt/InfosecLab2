import numpy as np
from utils import *

def binningEncoder(u):
    '''
    Encode a binary array of three digits with a (7,4) Hamming code
    :param u: binary array of three digits
    :return: a list of corresponding codewords
    '''
    u = np.vstack((0,u))
    G_list = [stringToBits('1000').T,
              stringToBits('0100').T,
              stringToBits('0010').T,
              stringToBits('0001').T,
              stringToBits('1101').T,
              stringToBits('1011').T,
              stringToBits('0111').T]
    G = np.vstack(G_list).reshape((-1,4))
    c1 = G.dot(u)%2
    c2 = np.logical_not(c1)*1
    return [c1,c2]
