# tackle outliers 2

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
real_world_data = [2.06, 1.90, 6.73, 1.78, 1.10, 2.19, 1.22, 1.28, 9.65, 12.79,
                   1.48, 3.74, 5.57, 1.69, 5.12, 1.01, 2.80, 1.58, 2.00, 9.06,
                   1.13, 2.56, 2.33, 1.03, 1.39, 1.45, 1.49, 1.36, 169.64, 4.14,
                   1.00, 2.35, 1.20, 3.42, 1.09, 1.05, 1.94, 22.05, 1.05, 1.79,
                   1.59, 1.88, 1.70, 1.76, 1.29, 2.79, 2.84, 15.97, 2.50, 1.07]

range_suggestion = suggest_range(real_world_data)
print(f"Suggested range: random.randint({range_suggestion[0]}, {range_suggestion[1]})")
