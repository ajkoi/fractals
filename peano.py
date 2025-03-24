import matplotlib.pyplot as plt
import numpy as np

def peano_curve(start=(0, 0), size=1, depth=5):
    if depth== 0:
        return [start]

    # Calculate the size of the sub-squares
    sub_size = size / 3

    # Recursively generate the Peano curve for each sub-square
    points = []

    points += peano_curve((start), sub_size, depth-1)
    points += peano_curve((start[0], start[1]+sub_size), sub_size, depth-1)
    return points
# Generate Peano curve points
order = 2
points = peano_curve()
# Extract x and y coordinates
x_coords, y_coords = zip(*points)

# Plot the Peano curve
plt.figure(figsize=(6, 6))
plt.plot(x_coords, y_coords, 'b-', lw=1)
plt.title(f'Peano Curve (Order {order})')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
