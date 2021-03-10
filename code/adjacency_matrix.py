import numpy as np
import random

def define_species_list(n: int, web_shape: str) -> list:
    """
    Function takes in the number of species and returns a list of lists
    with a sublist for each species with necessary locations for the pieces
    of data

    Parameters
    """
    # initialize species list
    sp_list = []
    for i in n:
        con_prod = random.sample(['Producer', 'Producer', 'Consumer'], 1)[0]
        if con_prod == 'Producer': # All for producer
            body_size = np.random.exponential(scale = 0.34, size = 1)[0]
            prey_limits = []
            habitat_midpoint = round((np.random.uniform(low = 0, /
                                                 high = 1, /
                                                 size = 1)[0]), 3)
            habitat = [habitat_midpoint, 0, 0]
            if habitat_midpoint >= 0.2:
                habitat[1] = habitat_midpoint - 0.2
            else:
                habitat[1] = 0
            if habitat_midpoint <= 0.8:
                habitat[2] = habitat_midpoint + 0.2
            else:
                habitat[2] = 1
        else: # all for consumer
            body_size = np.random.exponential(scale = 800, size = 1)
            prey_limits = [0.05*body_size, 0.65*body_size]
            habitat_midpoint = np.random.uniform(low = 0, high = 1)
            habitat = []
            if habitat_midpoint >= 0.2:
                habitat[0] = habitat_midpoint - 0.2
            else:
                habitat[0] = 0
            if habitat_midpoint <= 0.8:
                habitat[1] = habitat_midpoint + 0.2
            else:
                habitat[1] = 1



        sp_array[i] = [con_prod, \ # consumer or producer
                       body_size, \ # body size
                       prey_limits, \ # body size of prey able to consume
                       habitat, \ # habitat association
                       NA, \ #
                       NA \
                       ]

    # assign trait values
    # beta for producers should be 0.34 (Brose 2019 paper on body size)
    # beta for non-producers = 800 (Brose 2019 paper on body size)
