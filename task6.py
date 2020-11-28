import numpy as np 
import math
from utils import *
from random_binning_encoder import *
from send_to_channel import *
from binning_decoder import *
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
#from mpl_toolkits.mplot3d import Axes3D
from task5 import * #bsc
def task6():
    d_simulation_results, deltas= simulation(print_results_of_simulation=False)

    pdf_computation(d_simulation_results, deltas, print_pdf=True)
    #simulation(print_results_of_simulation = False)

def pdf_computation(d_simulation_results, deltas, print_pdf=True):
    mutual_information=[]
    for i,simulation_results in enumerate(d_simulation_results):
        #compute joint pdf
        
        dataframes = []
        #sort codewords/frequency dictionaries according to codewords
        for u in simulation_results.keys():
            dictionary_of_u = simulation_results[u]
            simulation_results[u] = {k: dictionary_of_u[k] for k in sorted(dictionary_of_u)} #sorted(dictionary_of_u.keys())
            

            #print(simulation_results[u])
            #create a pandas dataframe for the joint pdf
            df = pd.DataFrame(simulation_results[u], index = [u])
            #print(df)
            dataframes.append(df)

        print(i)
        joint_pdf = pd.concat(dataframes)

        ## normalize pdf
        joint_pdf = joint_pdf/ np.sum(joint_pdf.sum(axis = 0).to_numpy())


        #sns.jointplot(data=joint_pdf, kind="hist")
        #plt.show()
        #print(joint_pdf)
        #matplotlib.pyplot.hist2d(joint_pdf)
        
        #fig = plt.figure()
        #ax = fig.add_subplot(111, projection='3d')
        #ax.scatter(np.array(range(7)), np.array(range(128)), joint_pdf.to_numpy())
        #plt.show()

        ############# MARGINAL DISTRIBUTION
        p_z = joint_pdf.sum(axis = 0).to_dict()
        p_u = joint_pdf.sum(axis = 1).to_dict()
        
        #print(p_z)
        #print(p_u)

        # Mutual information:
        I = 0
        for u in p_u.keys():
            for codeword in p_z.keys():
            
                joint_p = joint_pdf.loc[u,codeword]
                I += joint_p *np.log2( joint_p / (p_u[u]*p_z[codeword])  )
        mutual_information.append(I)

        if (print_pdf):
            print("Joint pdf")
            print(joint_pdf)
            
            print("Marginal pdf of u")

            ax1=plt.subplot(2,1,1)
            ax1.bar(p_u.keys(), p_u.values())
        

            print("Marginal pdf of z")
            ax2=plt.subplot(2,1,2)
            
            ax2.bar(p_z.keys(), p_z.values())
            plt.show()


            print("Mutual Information: " + str(I))

    plt.plot(deltas, mutual_information)
    plt.title("Mutual information")
    plt.xlabel("Delta")
    plt.ylabel("I(u;z)")
    plt.show()

    return joint_pdf, p_u, p_z, I

def simulation(print_results_of_simulation = True):
    """run a simulation on the frequency of the keyword at Z

    Args:
        print_results_of_simulation (bool, optional): Boolean to choose if you want to print the results.
        Defaults to True.
    """

    _, Z_cardinality = computeConfigDistrib(7,3)
    Z_cardinality = int(Z_cardinality)
    u_s = [ stringToBits('000'),
            stringToBits('001'),
            stringToBits('010'),
            stringToBits('011'),
            stringToBits('100'),
            stringToBits('101'),
            stringToBits('110'),
            stringToBits('111')
            ]

    #simulation
    number_of_simulations = 100*Z_cardinality;
    delt_simulations = []
    mutual_information=[]
    deltas = np.linspace(0.2, 0.5, 20)
    for delta in deltas:
        dict_u_codewords = {} #dictionary with key = u and value = dictianary of codewords and their frequency
        for u_index in range(len(u_s)): #for every message 
        
            dict_codeword_frequency = {}
            
            for sim_index in range(number_of_simulations): # do 100*|Z| simulations, in which:
                codeword = randomBinningEncoder(u_s[u_index]) # compute the codeword to trasmit
                rec_codeword = BSC(codeword, delta).array
                #rec_codeword = sendToChannelZ(codeword)[0] #trasmit the codeword
                
                #now we add the codeword to a dictionary with codeword and number of occurrance
                if bitsToString(rec_codeword) in dict_codeword_frequency:
                    dict_codeword_frequency[bitsToString(rec_codeword)] += 1/number_of_simulations
                else:
                    dict_codeword_frequency[bitsToString(rec_codeword)] = 1/number_of_simulations
        
            #at the end of the simulation add the dictionary for the current u
            #to the dictionary of key = u and value = dictionary dict_codeword_frequency for u
            dict_u_codewords[bitsToString(u_s[u_index])] = dict_codeword_frequency
        
        delt_simulations.append(dict_u_codewords)
        

    ##### print
    #if print_results_of_simulation:
    #    
    #    for figure_index in range(1,8+1):
    #        ax1=plt.subplot(8, 1, figure_index)
    #        dictionary_to_plot = dict_u_codewords[bitsToString(u_s[figure_index-1])]
    #        ax1.bar(dictionary_to_plot.keys(),dictionary_to_plot.values())
    #        ax1.get_xaxis().set_visible(False)
    #        #ax1.title.set_text(bitsToString(u_s[figure_index-1]))
                
    #    plt.suptitle("Frequency of received codewords for Z")
    #    plt.show()
    
    return delt_simulations, deltas




def computeConfigDistrib(length_of_codeword, max_errors):
    """Compute the number of configuration of a bit mask to intruduce errors in a codeword 

    Args:
        length_of_codeword (int): lenght of a bit codeword
        max_errors (int): max number of errors to introduce in a codeword, depends on channel

    Returns:
        list: [0]: (array) where at index i there is number of possible configuration with i max errors
              [1]: (int) sum of all the possible configurations with max_errors
    """
    possible_config = np.zeros(max_errors+1) #at index i number of possible configuration wirg i errors

    for i in range(0, max_errors+1):
        config_i = math.comb(length_of_codeword,i)
        possible_config[i] = config_i

    tot_config = possible_config.sum()
    return (possible_config, tot_config)


if __name__ == "__main__":
    main()