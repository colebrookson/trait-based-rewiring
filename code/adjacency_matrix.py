import numpy as np
import random


def assign_trait_values(organism_type: str, organism_id: int) -> list:
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

    trait_list = [organism_id, \
                  organism_type, \
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

    sp_list = [None]*n
    i = 0
    while (i < n):
        organism_type = random.sample(['Producer', \
                                       'Producer', \
                                       'Consumer'], 1)[0]
        sp_list[i] = assign_trait_values(organism_type = organism_type, \
                                         organism_id = i)
        i += 1 # increment

    return sp_list

test_species = define_species_list(n = 4)

test_species[0][4][1]
test_species[2][3]

def determine_interaction(predator: int, prey: int, species_list:list) -> int:
    predator = 1; prey = 0; species_list = test_species


    pred_hab = species_list[predator][4]
    prey_hab = species_list[prey][4]
    prey_size = species_list[prey][2]
    pred_min = species_list[predator][3][0]
    pred_max = species_list[predator][3][1]

    if (predator == prey) or (species_list[predator][1] == 'Producer'):
        value = 0 # this is assuming no canibalism!!!
    elif (((prey_hab[1] >= pred_hab[1] and prey_hab[1] <= pred_hab[2]) or \
          (prey_hab[2] >= pred_hab[1] and prey_hab[2] <= pred_hab[2])) and \
          (prey_size <= pred_max and prey_size >= pred_min)):
          value = 1
    else:
        value = 0

    return value
x = determine_interaction(1, 0, test_species)
def create_interaction_matrix(species_list:list) -> np.array:
    """
    This function takes in the species list and returns an interaction matrix
    that will form the basis of the networks to then be created
    """
    j = 1; i = 0; species_list = test_species
    interaction_matrix = np.zeros(shape = (len(species_list), \
                                           len(species_list)), \
                                           dtype = np.int8)

    for i in range(interaction_matrix.shape[0]): # rows are prey
        for j in range(interaction_matrix.shape[1]): # cols are predators
            interaction_matrix[i][j] = \
                    determine_interaction(predator = j, \
                                          prey = i, \
                                          species_list = species_list)

test_species
interaction_matrix

### Important Assumptions
# No canibalism
# No variation in habitat association width
