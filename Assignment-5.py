import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load or create a sample dataset
# You can replace this with your dataset (e.g., df = pd.read_csv('your_data.csv'))
data = {
    'A': np.random.rand(100),
    'B': np.random.rand(100),
    'C': np.random.rand(100) + 0.5 * np.random.rand(100),
    'D': np.random.rand(100) - 0.3 * np.random.rand(100)
}

# Create DataFrame
df = pd.DataFrame(data)

# a. Find the correlation matrix
corr_matrix = df.corr()
print("Correlation Matrix:")
print(corr_matrix)

# Find the covariance matrix
cov_matrix = df.cov()
print("\nCovariance Matrix:")
print(cov_matrix)

# b. Plot the correlation matrix and visualize relationships using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()
