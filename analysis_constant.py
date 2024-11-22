import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde

constant_size = 10000
data = pd.read_csv(f'msd_results_constant_size_of_{constant_size}.csv')
ops = data['ops'].values

# calculate optimal number of bins using 'Freedman-Diaconis Rule'
q25, q75 = np.percentile(ops, [25, 75])
iqr = q75 - q25
bin_width = 2 * iqr / (len(ops) ** (1/3))
n_bins = int(np.ceil((ops.max() - ops.min()) / bin_width))

# create histogram
plt.figure(figsize=(12, 6))
n, bins, patches = plt.hist(ops, bins=n_bins, edgecolor='black', alpha=0.6, label='Histogram', density=True)

# perform Kernel Density Estimation (KED)
kde = gaussian_kde(ops)
x_vals = np.linspace(ops.min(), ops.max(), 1000) # points for smooth line
kde_vals = kde(x_vals)

# Plot the KDE line
plt.plot(x_vals, kde_vals, color='red', label='KDE (smoothed distribution)', linewidth=2)

# add mean and median lines
plt.axvline(np.mean(ops), color='r', linestyle='dashed', linewidth=2, label='mean')
plt.axvline(np.median(ops), color='g', linestyle='dashed', linewidth=2, label='median')

# customize plot
plt.title(f'operation count distribution (array size: {constant_size}, {len(ops)} measurements)')
plt.xlabel('operation count')
plt.ylabel('density')
plt.legend()

# add textual info
info = f'min: {np.min(ops):.6f}\nmax: {np.max(ops):.6f}\n'
info += f'mean: {np.mean(ops):.6f}\nmedian: {np.median(ops):.6f}\n'
info += f'standard deviation: {np.std(ops):.6f}'
plt.text(0.95, 0.95, info, transform=plt.gca().transAxes, va='top', ha='right', bbox=dict(facecolor='white', alpha=0.5))

# save and show plot
plt.tight_layout()
plt.savefig('ops_distribution_with_kde.png', dpi=600)
plt.show()
