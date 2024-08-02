def bayes_theorem(p_b_given_a, p_a, p_b):
    
    if p_b == 0:
        raise ValueError("Probability of B (P(B)) cannot be zero.")
    
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# Example usage:
p_b_given_a = float(input("Enter the probability of B given A (P(B|A)): "))
p_a = float(input("Enter the probability of A (P(A)): "))
p_b = float(input("Enter the probability of B (P(B)): "))

try:
    p_a_given_b = bayes_theorem(p_b_given_a, p_a, p_b)
    print(f"The probability of A given B (P(A|B)) is: {p_a_given_b:.4f}")
except ValueError as e:
    print(e)