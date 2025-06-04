"""
MIT License

This code was generated with the assistance of Claude AI.
You are free to use, modify, and distribute this code under the terms of the MIT License.
See the LICENSE file for details.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Create plots directory if it doesn't exist
os.makedirs('plots', exist_ok=True)

def order_statistics_heterogeneous_exponential(rates, size=1):
    """
    Generate samples where each sample contains both the smallest and second smallest
    values from draws of different exponential distributions with given rates.
    
    Args:
        rates: List of rate parameters for different exponential distributions
        size: Number of samples to generate
    Returns:
        Tuple of (smallest, second_smallest) values
    """
    # Generate matrix where each column is from a different exponential
    samples = np.zeros((size, len(rates)))
    for i, rate in enumerate(rates):
        samples[:, i] = np.random.exponential(scale=1/rate, size=size)
    # Sort each row and get both statistics
    sorted_samples = np.sort(samples, axis=1)
    return sorted_samples[:, 0], sorted_samples[:, 1]  # smallest, second smallest

def sum_two_exponential(lambd=1.0, size=1):
    """
    Generate samples where each sample is the sum of two draws from
    an exponential distribution.
    """
    return np.random.exponential(scale=1/lambd, size=size) + \
           np.random.exponential(scale=1/lambd, size=size)

# Simulation parameters
n_simulations = 100000  # Number of samples to generate

# Define rates for the 5 exponential distributions that sum to 1
# Using different rates to make it more interesting
rates = [0.3, 0.25, 0.2, 0.15, 0.1]  # These sum to 1
assert abs(sum(rates) - 1.0) < 1e-10, "Rates must sum to 1"

# Generate samples
smallest_samples, second_smallest_samples = order_statistics_heterogeneous_exponential(rates, n_simulations)
sum_samples = sum_two_exponential(1.0, n_simulations)

# Create histograms
plt.figure(figsize=(12, 6))

plt.hist(smallest_samples, bins=50, alpha=0.5, density=True, 
         label=f'Smallest of 5 exponentials\nwith rates {rates}')
plt.hist(second_smallest_samples, bins=50, alpha=0.5, density=True, 
         label=f'Second smallest of 5 exponentials\nwith rates {rates}')
plt.hist(sum_samples, bins=50, alpha=0.5, density=True,
         label='Sum of two exponentials (rate=1)')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Comparison of Distributions')
plt.legend()

# Save the histogram plot
plt.savefig('plots/density_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

# Calculate and display summary statistics
print("\nSummary Statistics:")
print("\nSmallest of 5 Heterogeneous Exponentials:")
print(f"Mean: {np.mean(smallest_samples):.4f}")
print(f"Variance: {np.var(smallest_samples):.4f}")
print(f"Median: {np.median(smallest_samples):.4f}")

print("\nSecond Smallest of 5 Heterogeneous Exponentials:")
print(f"Mean: {np.mean(second_smallest_samples):.4f}")
print(f"Variance: {np.var(second_smallest_samples):.4f}")
print(f"Median: {np.median(second_smallest_samples):.4f}")

print("\nSum of Two Exponentials (rate=1):")
print(f"Mean: {np.mean(sum_samples):.4f}")
print(f"Variance: {np.var(sum_samples):.4f}")
print(f"Median: {np.median(sum_samples):.4f}")

# Perform Kolmogorov-Smirnov tests
ks_stat1, p_value1 = stats.ks_2samp(smallest_samples, sum_samples)
ks_stat2, p_value2 = stats.ks_2samp(second_smallest_samples, sum_samples)
ks_stat3, p_value3 = stats.ks_2samp(smallest_samples, second_smallest_samples)

print("\nKolmogorov-Smirnov tests:")
print(f"Smallest vs Sum of Two:")
print(f"KS statistic: {ks_stat1:.4f}")
print(f"p-value: {p_value1:.4f}")

print(f"\nSecond Smallest vs Sum of Two:")
print(f"KS statistic: {ks_stat2:.4f}")
print(f"p-value: {p_value2:.4f}")

print(f"\nSmallest vs Second Smallest:")
print(f"KS statistic: {ks_stat3:.4f}")
print(f"p-value: {p_value3:.4f}")

# Create CDF plot
plt.figure(figsize=(12, 6))
plt.hist(smallest_samples, bins=50, density=True, cumulative=True, 
         histtype='step', label='Smallest CDF')
plt.hist(second_smallest_samples, bins=50, density=True, cumulative=True, 
         histtype='step', label='Second smallest CDF')
plt.hist(sum_samples, bins=50, density=True, cumulative=True,
         histtype='step', label='Sum CDF')
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.title('Empirical Cumulative Distribution Functions')
plt.legend()

# Save the CDF plot
plt.savefig('plots/cdf_comparison.png', dpi=300, bbox_inches='tight')
plt.close() 