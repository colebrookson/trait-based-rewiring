import numpy as np
n = 10
test_list = [None] * (n+1)

i = 0
while (i <= n):
    x = np.random.uniform(low = 1, high = 10, size = 1)[0]
    test_list[i] = x
    i += 1 #increment

## ABOVE GOOD

        sp_list[i] = [con_prod, \ # consumer or producer
                      body_size, \ # body size
                      prey_limits, \ # body size of prey able to consume
                      habitat, \ # habitat association
                      None] # biomass
