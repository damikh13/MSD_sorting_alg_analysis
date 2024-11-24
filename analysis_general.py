import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('msd_results_diff_sizes.csv')

def normalize(y):
    return y / y[0]

x = df['size'].values # input sizes

# plot 1: normalized execution time
plt.figure(figsize=(16, 10))
plt.plot(df['size'], normalize(df['worst time']), label='worst time', marker='o')
plt.plot(df['size'], normalize(df['avg time']), label='average time', marker='s')
plt.plot(df['size'], normalize(df['best time']), label='best time', marker='^')

# theoretical curves for visual comparison
plt.plot(x, normalize(x), label='O(n)', linestyle='--')
plt.plot(x, normalize(x * np.log(x) / np.log(9)), label='O(n log_9 n)', linestyle='--')
plt.plot(x, normalize(x**2), label='O(n^2)', linestyle='--')
plt.plot(x, normalize(x**3), label='O(n^3)', linestyle='--')

# plot customization
plt.title('normalized execution time vs input size', fontsize=16)
plt.xlabel('input size', fontsize=14)
plt.ylabel('normalized time', fontsize=14)
plt.legend(fontsize=12)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

# saving the plot
plt.savefig('normalized_execution_time.png', dpi=600, bbox_inches='tight')
plt.show()
plt.close()

# plot 2: normalized number of operations
plt.figure(figsize=(16, 10))
plt.plot(df['size'], normalize(df['worst ops']), label='worst operations', marker='o')
plt.plot(df['size'], normalize(df['avg ops']), label='average operations', marker='s')
plt.plot(df['size'], normalize(df['best ops']), label='best operations', marker='^')

plt.plot(x, normalize(x), label='O(n)', linestyle='--')
plt.plot(x, normalize(x * np.log(x) / np.log(9)), label='O(n log_9 n)', linestyle='--')
plt.plot(x, normalize(x**2), label='O(n^2)', linestyle='--')
plt.plot(x, normalize(x**3), label='O(n^3)', linestyle='--')

plt.title('normalized number of operations vs input size', fontsize=16)
plt.xlabel('input size', fontsize=14)
plt.ylabel('normalized number of operations', fontsize=14)
plt.legend(fontsize=12)
plt.xscale('log')
plt.yscale('log')
plt.grid(True)

plt.savefig('normalized_operations_count.png', dpi=600, bbox_inches='tight')
plt.show()
plt.close()

print("plots saved as 'normalized_execution_time.png' and 'normalized_operations_count.png'.")