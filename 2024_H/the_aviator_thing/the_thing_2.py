# tackle outliers one
import random
import numpy as np

def suggest_range(last_numbers):
    if len(last_numbers) < 2:
        raise ValueError("Insufficient data to suggest a range")

    # Use numpy to calculate the interquartile range (IQR)
    q1 = np.percentile(last_numbers, 25)
    q3 = np.percentile(last_numbers, 75)
    iqr = q3 - q1

    # Calculate suggested range based on the IQR
    lower_bound = max(1, int(q1 - 1.5 * iqr))
    upper_bound = int(q3 + 1.5 * iqr)

    return lower_bound, upper_bound

# Example usage:
last_50_numbers = [2.33, 1.55, 2.21, 3.14, 2.89, 1.23, 2.45, 3.67, 1.89, 2.34,
                   1.67, 2.98, 2.11, 3.45, 1.78, 2.56, 3.22, 2.01, 1.34, 2.89,
                   3.45, 2.11, 1.67, 2.33, 1.89, 2.45, 3.00, 1.34, 2.56, 2.11,
                   1.78, 2.89, 3.45, 2.34, 1.67, 2.98, 2.11, 3.45, 1.78, 2.56,
                   3.22, 2.01, 1.34, 2.89, 3.45, 2.11, 1.67, 2.33, 1.89, 11.95, 300.40, 1000.24]

range_suggestion = suggest_range(last_50_numbers)
print(f"Suggested range: random.randint({range_suggestion[0]}, {range_suggestion[1]})")
