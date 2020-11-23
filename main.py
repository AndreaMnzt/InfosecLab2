#import external functions from files 
import numpy as np
from utils import *


def main():

    ### Introduction to utils function, i will comment this on tuesday
    print("- Example to use utils function, I will comment this part on Tuesday")
    print("- Utils functions have a description, please if you have time comment your code")

    print('-- stringToBits(string_of_bits) function returns the numpy array for the given string of bits')  
    print('-- e.g. the numpy array for the string "0001001" is: ')
    bit_array = stringToBits('0001001')
    print(bit_array)
    print("Note: for all the internal calculation you should work with numpy arrays, since they provide us an 'algebraic sintax' to work with")

    print('-- bitsToString(array_of_bits) function returns the string representation of a numpy bit array')
    print('-- e.g. we can convert the above defined array to his string: ')
    bit_string = bitsToString(bit_array)
    print(bit_string)
    
    print("-- Note: bitsToString is useful to print the result after it's been used as numpy array for the computation")

    #########################################################
    #  TASK 1: Implement the uniform error channel

    print("\n# Task 1 # Implement the uniform error channel:")
    


    #########################################################
    #  TASK 2: Implement the random binning encoder
    print("\n# Task 2 # Implement the random binning encoder:")



    #########################################################
    #  TASK 3: Implement the random binning decoder
    print("\n# Task 3 # Implement the random binning decoder:")
    
    
    
    #########################################################
    #  TASK 4: Verify perfect secrecy
    print("\n# Task 4 # Verify perfect secrecy:")
    
    
    
    #########################################################
    #  TASK 5: Simulate transmission over a binary symmetric channel
    print("\n# Task 5 # Simulate transmission over a binary symmetric channel:")
    
    
    
    #########################################################
    #  TASK 6: Evaluate the system security over the wiretap BSC
    print("\n# Task 6 # Evaluate the system security over the wiretap BSC:")
    




    #########################################################
    # END OF main()

if __name__ == "__main__":  # main definition
    main()