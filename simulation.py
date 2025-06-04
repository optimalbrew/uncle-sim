import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def second_largest_exponential(n_samples, lambd=1.0, size=1):
    """
    Generate samples where each sample is the second largest value from
    n_samples draws from an exponential distribution.
    """
    # Generate n_samples x size matrix of exponential random variables
    samples = np.random.exponential(scale=1/lambd, size=(size, n_samples))
    # Sort each row and get the second largest value
    return -np.sort(-samples, axis=1)[:, 1]

def sum_two_exponential(lambd=1.0, size=1):
    """
    Generate samples where each sample is the sum of two draws from
    an exponential distribution.
    """
    return np.random.exponential(scale=1/lambd, size=size) + \
           np.random.exponential(scale=1/lambd, size=size)

# Simulation parameters
n_simulations = 100000  # Number of samples to generate
lambd = 1.0            # Rate parameter
n_samples = 3          # Number of samples to draw from for second largest

# Generate samples
second_largest_samples = second_largest_exponential(n_samples, lambd, n_simulations)
sum_samples = sum_two_exponential(lambd, n_simulations)

# Create histograms
plt.figure(figsize=(12, 6))

plt.hist(second_largest_samples, bins=50, alpha=0.5, density=True, 
         label=f'Second largest of {n_samples} exponentials')
plt.hist(sum_samples, bins=50, alpha=0.5, density=True,
         label='Sum of two exponentials')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title(f'Comparison of Distributions (λ={lambd})')
plt.legend()

# Calculate and display summary statistics
print("\nSummary Statistics:")
print("\nSecond Largest of 3 Exponentials:")
print(f"Mean: {np.mean(second_largest_samples):.4f}")
print(f"Variance: {np.var(second_largest_samples):.4f}")
print(f"Median: {np.median(second_largest_samples):.4f}")

print("\nSum of Two Exponentials:")
print(f"Mean: {np.mean(sum_samples):.4f}")
print(f"Variance: {np.var(sum_samples):.4f}")
print(f"Median: {np.median(sum_samples):.4f}")

# Perform Kolmogorov-Smirnov test
ks_stat, p_value = stats.ks_2samp(second_largest_samples, sum_samples)
print(f"\nKolmogorov-Smirnov test:")
print(f"KS statistic: {ks_stat:.4f}")
print(f"p-value: {p_value:.4f}")

plt.show() 