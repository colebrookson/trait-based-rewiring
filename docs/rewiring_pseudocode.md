# Trait-based Rewiring Algorithm & Analysis Outline

The purposes of this document are to:
1. Outline the general purposes of this project
2. Describe the components of the analysis broadly, and
3. Specifically outline the various programs that will jointly perform the analysis
4. Act as a reference for anyone trying to implement this analysis in a different language/framework

## Project Overview

## Analysis Components

### Network Construction

#### Define network shape and # of spp (also need connectance here -- 0.1-0.2 is biologically plausible)

make network as before, and get connectance afterwards. then have a connectance
cap so if it's > 0.2, resample randomly down to max 02 and look across those
values of connectance that you'll see afterwards
    this comes from taking the range of possible trait values and narrowing it
    or making it wider to capture more/less connectance

#### Assign trait values to each sp

#### Populate interaction matrix

### Biomass Model Formulation

so do the fucntional response where it sums to 1 but then you cut it off at 0.1


#### Functions to define biomass model for each sp

#### Draw initial biomass values for each sp

everyone does the same method from this (bros 2006 paper), and everything is
between 0.05 and 1 --- maybe don't do this?

take body size, assign a range and draw randomly from the range for Biomass   
    someone from michel's group (nuria galliana) and maybe some mccann ppl do this
    nuria's paper is in eco letter

#### Simulate network dynamics out to a stable point

could linearize your system and take those as your initial Biomass

alternatively, could just run it for like 1000 timesteps to et it sort of stable

save all your initial parameters

save initial topologies, initial interaction strengths, initial biomasses, the
time every species goes extinct, keep track of when new species are incorporated
i.e when your topology changes and then final biomasses

save initial, save first 100 right after perturbation, every 50 from then on,
and then the last 200

### Instigation of Rewiring

#### Assign press vs. pulse

make sure the cycle for pulse doesn't coincide with the cycle you save (make
that the number you're pulsing on is not a multiple of the cycle you're saving on)



#### Select trait values (and corresponding species) to target

#### Impose

### Tracking Biomass Outputs Through Rewiring


### Outputs

-you can have like predator and some prey items then plot the pulse, press and no change for the last 300 time steps or something
    - same networks will be given pulse, press, and no change, (i.e. lets say you have 300 networks), you take the mean and sd of each network interaction
-community persistence, y would be persistence, x would be some sort of rewiring thing (ex. range of traits you'd take in), or any sort of network metric (i.e. modularity, connectance, etc),
and then you compare your no rewiring scenarios that are the exact same and the rewiring scenarios

-persistence on x, and network metric on y




## Pseudocode
