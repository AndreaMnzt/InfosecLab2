import numpy as np 
import math
from utils import *
from random_binning_encoder import *
from send_to_channel import *
from binning_decoder import *
import matplotlib.pyplot as plt


def main():
    simulation(print_results_of_simulation = True)

def simulation(print_results_of_simulation = True):
    _, Z_cardinality = computeConfigDistrib(7,3)
    Z_cardinality = int(Z_cardinality)
    u_s = [ stringToBits('001'),
            stringToBits('010'),
            stringToBits('011'),
            stringToBits('100'),
            stringToBits('101'),
            stringToBits('110'),
            stringToBits('111')
            ]

    #simulation
    dict_u_codewords = {} #dictionary with key = u and value = dictianary of codewords and their frequency
    for u_index in range(len(u_s)): #for every message 
        
        dict_codeword_frequency = {}
        number_of_simulations = 100*Z_cardinality;
        for sim_index in range(number_of_simulations): # do 100*|Z| simulations, in which:
            codeword = randomBinningEncoder(u_s[u_index]) # compute the codeword to trasmit
            rec_codeword = sendToChannelZ(codeword)[0] #trasmit the codeword

            #now we add the codeword to a dictionary with codeword and number of occurrance
            if bitsToString(rec_codeword) in dict_codeword_frequency:
                dict_codeword_frequency[bitsToString(rec_codeword)] += 1/number_of_simulations
            else:
                dict_codeword_frequency[bitsToString(rec_codeword)] = 1/number_of_simulations

        #at the end of the simulation add the dictionary for the current u
        #to the dictionary of key = u and value = dictionary dict_codeword_frequency for u
        dict_u_codewords[bitsToString(u_s[u_index])] = dict_codeword_frequency
        
    ##### print
    if print_results_of_simulation:
        
        for figure_index in range(1,7+1):
            ax1=plt.subplot(7, 1, figure_index)
            dictionary_to_plot = dict_u_codewords[bitsToString(u_s[figure_index-1])]
            ax1.bar(dictionary_to_plot.keys(),dictionary_to_plot.values())
            ax1.get_xaxis().set_visible(False)
            #ax1.title.set_text(bitsToString(u_s[figure_index-1]))
                
        plt.suptitle("Frequency of received codewords for Z")
        plt.show()




def computeConfigDistrib(length_of_codeword, max_errors):
    possible_config = np.zeros(max_errors+1) #at index i number of possible configuration wirg i errors

    for i in range(0, max_errors+1):
        config_i = math.comb(length_of_codeword,i)
        possible_config[i] = config_i

    tot_config = possible_config.sum()
    return (possible_config, tot_config)


if __name__ == "__main__":
    main()