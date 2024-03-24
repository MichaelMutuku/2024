# Stop Number.

import numpy as np

def choose_stop_number(data, multiplier=1.5):
    mean_value = np.mean(data)
    stop_number = mean_value * multiplier
    return stop_number

def simulate_game(points, stop_number, num_tries):
    total_points = points
    for _ in range(num_tries):
        # Simulate generating a random number (replace with your actual logic)
        generated_number = np.random.uniform(1, 11)

        if generated_number > stop_number:
            total_points += generated_number * 2

        points -= 2  # Deduct 2 points per try

    return total_points

# Example usage:
historical_data = [2.06, 1.90, 6.73, 1.78, 1.10, 2.19, 1.22, 1.28, 9.65, 12.79,
                   1.48, 3.74, 5.57, 1.69, 5.12, 1.01, 2.80, 1.58, 2.00, 9.06,
                   1.13, 2.56, 2.33, 1.03, 1.39, 1.45, 1.49, 1.36, 169.64, 4.14,
                   1.00, 2.35, 1.20, 3.42, 1.09, 1.05, 1.94, 22.05, 1.05, 1.79,
                   1.59, 1.88, 1.70, 1.76, 1.29, 2.79, 2.84, 15.97, 2.50, 1.07]

stop_number = choose_stop_number(historical_data)
print(f"Chosen stop number: {stop_number}")

total_points = simulate_game(100, stop_number, 50)
print(f"Total points obtained: {total_points}")
