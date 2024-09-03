import numpy as np
from scipy.stats import skew, kurtosis


data = [5, 8, 6, 4, 2, 1]

mean = np.mean(data)

variance = np.var(data)

skewness = skew(data)

kurt = kurtosis(data)

print(f"Mean (First Moment): {mean}")
print(f"Variance (Second Moment): {variance}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurt}")
