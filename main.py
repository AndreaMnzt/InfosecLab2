   
#import external functions from files 
import numpy as np
from utils import *
from binning_encoder import *
from binning_decoder import *
from random_binning_encoder import *
from wiretap_ch import *
from task5 import *
import matplotlib.pyplot as plt
import random

def main():
    np.random.seed(0) # set random seed for replicability
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
    x = '1001000'
    x_array = stringToBits(x)
    loop_iterations = 10000
    prob_y = np.zeros(4)
    prob_z = np.zeros(4)
    dict_y = dict()
    dict_z = dict()
    (possible_config_y, tot_config_y) = computeConfigDistrib(7, 1)
    (possible_config_z, tot_config_z) = computeConfigDistrib(7, 3)
    for i in range(0, loop_iterations):
        (y, z, error_bits_y, error_bits_z) = wiretap_channel(np.reshape(x_array, -1))
        y_string = bitsToString(y.reshape((-1,1)))
        dict_y[y_string] = dict_y.get(y_string, 0) + 1

        z_string = bitsToString(z.reshape((-1,1)))
        dict_z[z_string] = dict_z.get(z_string, 0) + 1

        prob_y[error_bits_y] += 1
        prob_z[error_bits_z] += 1

    # check that every configuration has been generated
    cnt_gen_config_y = 0 # counter of distinct y configurations
    cnt_gen_config_z = 0 # counter of distinct z configurations
    for key in dict_y:
        dict_y[key] /= loop_iterations
        cnt_gen_config_y += 1
        print("P[y = {} ] = {}".format(key, dict_y[key] / loop_iterations))
    for key in dict_z:
        dict_z[key] /= loop_iterations
        cnt_gen_config_z += 1
        print("P[z = {} ] = {}".format(key, dict_z[key] / loop_iterations))

    print()
    print("Total configurations for y: {}\tNumber of generated configurations: {}".format(int(tot_config_y), cnt_gen_config_y))
    print("Total configurations for z: {}\tNumber of generated configurations: {}".format(int(tot_config_z), cnt_gen_config_z))
    print()

    # print the probability of 0, 1, 2, 3 errors in both y and z

    prob_y /= loop_iterations
    prob_z /= loop_iterations
    for i in range(0,4):
        print("P[{} errors in y] = {}".format(i, prob_y[i]))
    print()
    for i in range(0,4):
        print("P[{} errors in z] = {}".format(i, prob_z[i]))

    # two plots for checking uniformity of the outputs - the red line represents the uniform distribution

    # the histogram of the data y
    plt.bar(list(dict_y.keys()), dict_y.values(), color='b')
    plt.axhline(y=1/tot_config_y, color='r', linestyle='-')
    plt.xticks(x, " ")
    plt.title("Frequency of possible outputs y")
    plt.show()

    # the histogram of the data z
    plt.bar(list(dict_z.keys()), dict_z.values(), color='g')
    plt.axhline(y=1/tot_config_z, color='r', linestyle='-')
    plt.xticks(x, " ")
    plt.title("Frequency of possible outputs z")
    plt.show()


    #########################################################
    #  TASK 2: Implement the random binning encoder
    print("\n# Task 2 # Implement the random binning encoder:")

    u_s = [ stringToBits('001'),
            stringToBits('010'),
            stringToBits('011'),
            stringToBits('100'),
            stringToBits('101'),
            stringToBits('110'),
            stringToBits('111')
            ]

    print("- The generated codewords are:")
    for j in range(0,len(u_s)):
        codewords = binningEncoder(u_s[j])
        print("For message [%s]: [%s] and [%s]" %( bitsToString(u_s[j]), bitsToString(codewords[0]), bitsToString(codewords[1])))

    #########################################################
    #  TASK 3: Implement the random binning decoder
    print("\n# Task 3 # Implement the random binning decoder:")
    
    print("- Without a channel: ")
    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u_s[2]), bitsToString(binningDecoder(binningEncoder(u_s[2])[0])[0]), str(binningDecoder(binningEncoder( u_s[2])[0])[1])))
    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u_s[4]), bitsToString(binningDecoder(binningEncoder(u_s[4])[0])[0]), str(binningDecoder(binningEncoder( u_s[4])[0])[1])))
    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u_s[6]), bitsToString(binningDecoder(binningEncoder(u_s[6])[0])[0]), str(binningDecoder(binningEncoder( u_s[6])[0])[1])))

    print("\n- With a channel:")
    u = u_s[2]
    c = randomBinningEncoder(u)
    y = wiretap_channel(c.T)
    d,e = binningDecoder(y[0].T)

    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u), bitsToString(d),str(e)))

    u = u_s[4]
    c = randomBinningEncoder(u)
    y = wiretap_channel(c.T)
    d, e = binningDecoder(y[0].T)

    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u), bitsToString(d), str(e)))

    u = u_s[6]
    c = randomBinningEncoder(u)
    y = wiretap_channel(c.T)
    d, e = binningDecoder(y[1].T)
    print(c)
    print(y)
    print("For the message [%s] the decodified message is [%s], with [%s] corrected errors" %(bitsToString(u), bitsToString(d), str(e)))

    #########################################################
    #  TASK 4: Verify perfect secrecy
    print("\n# Task 4 # Verify perfect secrecy:")
    
    
    
    #########################################################
    #  TASK 5: Simulate transmission over a binary symmetric channel
    print("\n# Task 5 # Simulate transmission over a binary symmetric channel:")
    print("Number of errors on each output:")
    error_legitimate_channel = 0.03
    error_eavesdropper_channel = 0.1
    binary_sequence=np.zeros(5000)
    results = noise( binary_sequence, error_legitimate_channel)
    print(" For legitimate channel y: Expected errors =[%s], Generated errors =[%s]" %(int(len(binary_sequence)*error_legitimate_channel), results.errors))
    results = noise(binary_sequence, error_eavesdropper_channel)
    print(" For eavesdropper channel z: Expected errors =[%s], Generated errors =[%s]" %(int(len(binary_sequence)*error_eavesdropper_channel), results.errors))
    print("\nSimulating several trasmission between random binning encoder and legitimate decoder")
    number_of_transmission=300;
    array_codewords=[]
    bits_string=""

    for i in range(number_of_transmission):
        random_bits=bin(random.randint(0, 7))[2:].zfill(3)
        codewords = randomBinningEncoder(random_bits)
        print(codewords)
        array_codewords[i]=codewords
    for i in range(len(array_codewords)):
        bits_string+=array_codewords[i]
    string_with_errors=noise(bits_string, error_legitimate_channel)
    print(string_with_errors)
    #for i in range(len(string_with_errors))





    #########################################################
    #  TASK 6: Evaluate the system security over the wiretap BSC
    print("\n# Task 6 # Evaluate the system security over the wiretap BSC:")
    




    #########################################################
    # END OF main()

if __name__ == "__main__":  # main definition
    main()