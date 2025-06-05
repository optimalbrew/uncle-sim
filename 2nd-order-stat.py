"""
MIT License

This code was generated with the assistance of ChatGPT.
You are free to use, modify, and distribute this code under the terms of the MIT License.
See the LICENSE file for details.
"""


# The pdf of the second order statistic $X_{(2)}$ is given by
# $$
# f_{X_{(2)}}(x) = \sum_{\substack{i, j = 1 \\ i \ne j}}^n 
# \lambda_i \frac{\lambda_j}{\lambda_j - \lambda_i}
# e^{-\lambda_i x} 
# \prod_{\substack{k=1 \\ k \ne i, j}}^n e^{-\lambda_k x}, \quad x \geq 0
# $$

"""
This is a simulation for the second order statistic for n=5 exponential random variables with heterogeneous rates.
By itself, it is not enough to visualize the distribution of uncles (see the readme). We need
the joint distribution of the second order statistic and the sum of two iid exponentials.

"""


import numpy as np
import matplotlib.pyplot as plt

# Set up the rate parameters (same as simulation)
raw_rates = np.array([0.1, 0.3, 0.05, 0.25, 0.3])
rates = raw_rates / raw_rates.sum()  # normalize to sum to 1
n = len(rates)

# Evaluation grid
x_vals = np.linspace(0, 30, 1000)
pdf_vals = np.zeros_like(x_vals)

# Compute exact PDF of X_(2)
for idx, x in enumerate(x_vals):
    total = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            lambda_i = rates[i]
            lambda_j = rates[j]
            # Avoid division by zero (would only happen if lambda_i == lambda_j)
            if np.isclose(lambda_i, lambda_j):
                continue
            term = (
                lambda_i *
                (lambda_j / (lambda_j - lambda_i)) *
                np.exp(-lambda_i * x) *
                np.prod([np.exp(-rates[k] * x) for k in range(n) if k != i and k != j])
            )
            total += term
    pdf_vals[idx] = total

# Plot
plt.figure(figsize=(10, 6))
plt.plot(x_vals, pdf_vals, label="Exact PDF", color="crimson", lw=2)
plt.title("Exact PDF of 2nd Order Statistic (n=5, Heterogeneous Exponentials)")
plt.xlabel("x")
plt.ylabel("Density")
plt.grid(True)
plt.legend()
#plt.show()

plt.savefig('plots/2nd-order-stat.png', dpi=300, bbox_inches='tight')
plt.close()
