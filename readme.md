# Using Cursor-Claude for Uncle Block Simulations

The idea is to study orphaned or uncle block production in PoW chains like bitcoin or rootstock.

For every block height, what we observe is lowest draw from several exponential disrtibutions, one
for each miner (mining pool). Their individual rates $\lambda_{i}$ are unknown and unobservable. However, the *minimum* of exponentials is also an exponential with the effective rate parameter $ \lambda = \sum_{i} \lambda_{i}$

Thus, for a given difficulty, and assuming constant hashpower in the near term, what we observe is the lowest order statistic for each block height and these are random draws from $~expo(\lambda)$

In bitcoin an orphaned block is typically discarded. But in Rootstock (and in the initial PoW version of Ethereum), they are not thrown away. Instead, main chain blocks can point to "uncle" (or "ommer") blocks.
These chains actually reward miners for uncles too.

One way to think about the process is to think that an uncle block is one that was mined very close in time to the winning block at height H1. The uncle block shows up in the network before the next main block is finalized. So the winning block at heigh H2 can include a pointer to the uncle.

* Suppose the two lowest block times at height $H1$ are $b_{iH1} < b_{jH1}$ by some miners $i,j$. 
* Further suppose the lowest block time at height $H2$ is $b_{kH2}$ from some miner $k$
* We have $b_{iH1} < b_{jH1}$ which makes miner $j$'s block a "potential" uncle 
* but also $b_{jH1} < b_{iH1} + b_{kH2}$ so it can be actually pointed to by miner $k$

One way (NOT ENTIRELY CORRECT) to think about this. Compare the probability that the 2nd lowest draw from an exponential is less than a random draw from a distribution of the sum of two iid exponentials, which is a Gamma / Erlang distribution. This can be extended for the 3rd order statistic to include 2 uncles and so on.

This is not correct, because while the lowest draw from several exponentials does follow an exponential, the second lowest draw is NOT the same as drawing again from the same $\expo(\lambda)$! That, in turn will depend on the number of mining pools and their hashrates. This is a good example of learning from the AI... I noticed the error when it used a sample of 3 for the first distribution (I messed up).

One way to fix this is to assume a specific number of mining pools and their relative hashrates to determined their individual rates $\lambda_{i}$'s. Then draw random samples (one from each) in eveyr round and compare the 2nd highest value with that of the sum of exponentials. Otherwise, since $1/\lambda < 1/\lambda_{i}, \forall i$ we are giving too much of an advantage to the first process. 


## Simulation
**Initial prompt to claude 3.5 sonnet:** "use python to generate simulations to compare draws from two  distributions both derived from exponential distribution of rate lamda. the first process is the value of the second largest random draw from the exponential. the second is the sum of two random draws from the exponential"

Uses numpy etc

```
pip install -r requirements.txt
```

This is what Claude said the `simulation.py` does (or is supposed to) 
* The main simulation script that:
* Implements two functions to generate samples from both distributions
* Generates 100,000 samples for each distribution
* Creates a histogram comparison
* Calculates and displays summary statistics
* Performs a Kolmogorov-Smirnov test to compare the distributions

