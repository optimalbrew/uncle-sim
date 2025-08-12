"""
Generates miner and sibling miner identities.
In every round, each miner draws an expo r.v. from their own distribution
Lowest distribution -> miner of main trunk block
All others whose draw is within a "lag tolerance" are counted as siblings 
"""
import numpy as np
from scipy.stats import expon, poisson

num_miners = 7
num_blocks = 20
#include as sibling if time is within tolerance of minimum draw
lag_tolerance_for_siblings = 15 #seconds, 

# time between blocks in seconds for individual miners
times = np.linspace(60, 200, num_miners) #miner 0 has highest hashpower
rates = [1/t for t in times]

mu = sum(rates)
# this is minimum of the times between blocks (the mean of the compound poisson distribution)
print(f"\nMinimum of the times between blocks (Expected blocktime): {1/mu} seconds")


def determine_miner_and_siblings():
    # Exponential random samples for each miner in every round
    draws = [expon.rvs(scale=1/r, size=1) for r in rates]
    min_time = min(draws) #lowest draw
    
    idx_main_trunk = []
    idx_sibling = []
    for i in range(len(draws)):
        if draws[i] == min_time:
            idx_main_trunk.append(i)
        if draws[i] < (min_time + lag_tolerance_for_siblings) and i not in idx_main_trunk:
            idx_sibling.append(i)
    
    return idx_main_trunk, idx_sibling


for h in range(num_blocks):
    miner,sibs = determine_miner_and_siblings()
    if len(sibs) > 0:
        print(f"Block Ht {h}. Miner: {miner} and Sibling miners: {sibs}")
    else:
        print(f"Block Ht {h}. Miner: {miner}. No Siblings.")


############ Example Output#############
"""
Minimum of the times between blocks (Expected blocktime): 15.894185200054944 seconds
Block Ht 0. Miner: [2]. No Siblings.
Block Ht 1. Miner: [5] and Sibling miners: [2, 3]
Block Ht 2. Miner: [5]. No Siblings.
Block Ht 3. Miner: [3] and Sibling miners: [4, 5]
Block Ht 4. Miner: [1]. No Siblings.
Block Ht 5. Miner: [1]. No Siblings.
Block Ht 6. Miner: [2]. No Siblings.
Block Ht 7. Miner: [2]. No Siblings.
Block Ht 8. Miner: [3]. No Siblings.
Block Ht 9. Miner: [5]. No Siblings.
Block Ht 10. Miner: [3] and Sibling miners: [0]
Block Ht 11. Miner: [0]. No Siblings.
Block Ht 12. Miner: [0] and Sibling miners: [1, 5]
Block Ht 13. Miner: [0] and Sibling miners: [2]
Block Ht 14. Miner: [2]. No Siblings.
Block Ht 15. Miner: [4] and Sibling miners: [1]
Block Ht 16. Miner: [0]. No Siblings.
Block Ht 17. Miner: [0]. No Siblings.
Block Ht 18. Miner: [0]. No Siblings.
Block Ht 19. Miner: [2] and Sibling miners: [4]
"""