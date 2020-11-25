from utils import *
from wiretap_ch import *

def sendToChannelY(codeword):
    """send the codeword to the legitimate channel

    Args:
        codeword (vector np.arry of bit): the codeword to be trasmitted

    Returns:
        list: codeword received and the number of error intrduced
    """
    received_codeword, _, number_of_errors, _ = wiretap_channel(np.reshape(codeword,-1))
    received_codeword = np.array(received_codeword).reshape(-1,1) #make it column vector
    return received_codeword, number_of_errors

def sendToChannelZ(codeword):
    """send the codeword to the eavesdropper channel

    Args:
        codeword (vector np.arry of bit): the codeword to be trasmitted

    Returns:
        list: codeword received and the number of error intrduced
    """

    _,  received_codeword, _ ,number_of_errors = wiretap_channel(np.reshape(codeword,-1))
    received_codeword = np.array(received_codeword).reshape(-1,1) #make it column vector
    return received_codeword, number_of_errors

