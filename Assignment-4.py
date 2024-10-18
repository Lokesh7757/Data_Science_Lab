from math import comb

def binomial_distribution(n, p, k):
    # Calculate binomial probability using the formula:
    # P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)
    binomial_prob = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return binomial_prob

# Get input from user
try:
    n = int(input("Enter the number of trials (n): "))
    p = float(input("Enter the probability of success (p): "))
    k = int(input("Enter the number of successes (k): "))

    if n < 0 or k < 0 or k > n or not (0 <= p <= 1):
        raise ValueError("Invalid input values. Please ensure 0 <= k <= n and 0 <= p <= 1.")

    # Calculate and display the result
    result = binomial_distribution(n, p, k)
    print(f"The binomial probability for {k} successes out of {n} trials is: {result:.5f}")

except ValueError as ve:
    print(f"Error: {ve}")
