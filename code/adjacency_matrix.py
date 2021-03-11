import numpy as np
import random


def assign_trait_values(organism_type: str) -> list:
    """
    Function takes in the type of organism and returns a list of the various
    traits for that organism to be passed to the next list

    Parameters
    """
    if organism_type == 'Producer': # All for producer
        # beta for producers should be 0.34 (Brose 2019 paper on body size)
        body_size = np.random.exponential(scale = 0.34, size = 1)[0]
        prey_limits = [None]*2
        habitat_midpoint = round((np.random.uniform(low = 0, \
                                             high = 1, \
                                             size = 1)[0]), 3)
        habitat = [habitat_midpoint, 0, 0]
        if habitat_midpoint >= 0.2:
            habitat[1] = round((habitat_midpoint - 0.2), 3)
        else:
            habitat[1] = 0
        if habitat_midpoint <= 0.8:
            habitat[2] = round((habitat_midpoint + 0.2), 3)
        else:
            habitat[2] = 1
    else: # all for consumer
        # beta for non-producers = 800 (Brose 2019 paper on body size)
        body_size = np.random.exponential(scale = 800, size = 1)[0]
        prey_limits = [0.05*body_size, 0.65*body_size]
        habitat_midpoint = round((np.random.uniform(low = 0, \
                                             high = 1, \
                                             size = 1)[0]), 3)
        habitat = habitat = [habitat_midpoint, 0, 0]
        if habitat_midpoint >= 0.2:
            habitat[1] = round((habitat_midpoint - 0.2), 3)
        else:
            habitat[1] = 0
        if habitat_midpoint <= 0.8:
            habitat[2] = round((habitat_midpoint + 0.2), 3)
        else:
            habitat[2] = 1

    trait_list = [organism_type, \
                  body_size, \
                  prey_limits, \
                  habitat, \
                  None] # biomass

    return trait_list


def define_species_list(n: int) -> list:
    """
    Function takes in the number of species and returns a list of lists
    with a sublist for each species with necessary locations for the pieces
    of data

    Parameters

    TO-DO:
    1. Add in customization for web shape such that you can pass a shape
    (probably something like hourglass, top/bottom-heavy) and then that can be
    the thing that defines how many consumers there are etc
    """
    # initialize species list
    n = 4
    sp_list = [None]*(n+1)
    i = 0
    while (i <= n):
        organism_type = random.sample(['Producer', \
                                       'Producer', \
                                       'Consumer'], 1)[0]
        sp_list[i] = assign_trait_values(organism_type)
        i += 1 # increment
        print(i)
    return sp_list

test_species = define_species_list(n = 4)
