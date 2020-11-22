#import external functions from files 
import numpy as np
from utils import *


def main():

    print("Example to use utils function, I will comment this part on Tuesday")
    print("Utils functions have a description, please if you have time comment your code")
    print("- hexToBin('0xAB41') returns 1010101101000001 as a column vector:")
    binary_string = hexToBin('0xAB41') #converts a hex number, given as a string, to an array of binary numbers
    print(binary_string)


    print("- binToHex([1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,1] returns '0xAB41' as a string:")
    print(binToHex(binary_string))

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