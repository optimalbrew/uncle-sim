"""
MIT License

This code was generated with the assistance of ChatGPT and Claude AI too!
You are free to use, modify, and distribute this code under the terms of the MIT License.
See the LICENSE file for details.
"""

"""
This is a simulation for the second order statistic for n=5 exponential random variables with heterogeneous rates.
By itself, it is not enough to visualize the distribution of uncles (see the readme). We need
the joint distribution of the second order statistic and the sum of two iid exponentials.
"""


import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Number of variables and samples
n = 5
num_samples = 100_000

# Create heterogeneous rate parameters that sum to 1
raw_rates = np.array([0.1, 0.3, 0.05, 0.25, 0.3])
rate_params = raw_rates / raw_rates.sum()  # Normalize to sum to 1

# Generate samples: shape = (num_samples, n)
samples = np.array([
    np.random.exponential(scale=1/lambda_i, size=num_samples)
    for lambda_i in rate_params
]).T  # transpose to shape (num_samples, n)

# Sort each row and get the 2nd order statistic (index 1)
second_order_stats = np.sort(samples, axis=1)[:, 1]

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(second_order_stats, bins=100, density=True, alpha=0.7, color='skyblue')
plt.title('Empirical PDF of 2nd Order Statistic (n=5 Exponentials, Heterogeneous Rates)')
plt.xlabel('Value of $X_{(2)}$')
plt.ylabel('Density')
plt.grid(True)
#plt.show()

plt.savefig('plots/2nd-order-stat-sim.png', dpi=300, bbox_inches='tight')
plt.close()

# Optionally: print mean and std for summary
print(f"Mean of X_(2): {np.mean(second_order_stats):.4f}")
print(f"Std  of X_(2): {np.std(second_order_stats):.4f}")
