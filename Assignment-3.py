import numpy as np
from scipy.stats import skew, kurtosis

def calculate_moments(data):
    n = len(data)
    mean = np.mean(data)
    variance = np.var(data, ddof=1)  
    std_dev = np.std(data, ddof=1)   

    moments = {
        'mean': mean,
        'variance': variance,
        'std_dev': std_dev,
        'third_moment': np.mean((data - mean) ** 3),
        'fourth_moment': np.mean((data - mean) ** 4)
    }
    
    return moments

def calculate_skewness(data):
    return skew(data)

def calculate_kurtosis(data):
    return kurtosis(data)

def get_user_input():
    user_input = input("Enter a list of numbers : ")
    data = list(map(float, user_input.split()))
    return data

if __name__ == "__main__":
    data = get_user_input()

    moments = calculate_moments(data)
    print("\nMoments:")
    for key, value in moments.items():
        print(f"{key}: {value}")

    data_skewness = calculate_skewness(data)
    print(f"\nSkewness: {data_skewness}")

    data_kurtosis = calculate_kurtosis(data)
    print(f"Kurtosis: {data_kurtosis}")
