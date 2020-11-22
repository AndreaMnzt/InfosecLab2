import numpy as np 

def hexToBin( hex_string):
    """Convert a hex strin to a binary np.array
    e.g. "AAAA". "0xAAAA"
    NOTE: please provide the full Hex digits
    e.g. "1" WRONG!, "0001" RIGHT
    Args:
        hex_string (string): string to convert to bit
    Returns:
        np.array: bit np.array
    """    
    if (hex_string[:2] == '0x' or hex_string[:2] == '0X'):
        hex_string = hex_string[2:]

    final_length = 4*len(hex_string)

    bit_string = int(hex_string,16)
    #bit_string = [int(bit) for bit in bin(bit_string)[2:]] 
    bit_string = bin(bit_string)[2:]
    
    if len(bit_string) < final_length:
        bit_string = '0'*(final_length - len(bit_string)) + bit_string 
    
    bit_string = [int(bit) for bit in bit_string] 

    return np.reshape(np.array(bit_string),(-1,1))

def binToHex(binary_array):
    """convert a binary np.array to a hex string
    Args:
        binary_array (np.array): np.array of bits
    Returns:
        string: hex string
    """    

    hex_number = ''
    for bit in binary_array:
        hex_number += str(int(bit[0]*1))
    
    hex_number = hex(int(hex_number,2))

    return hex_number