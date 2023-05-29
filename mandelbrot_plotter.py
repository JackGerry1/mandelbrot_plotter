import numpy as np
import matplotlib.pyplot as plt

# Set the size of the grid
width, height = 1000, 1000

# Define the range of the grid in the complex plane
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

# Create a 2D array of complex numbers
c = np.zeros((width, height), dtype=np.complex128)
for i in range(width):
    for j in range(height):
        c[i, j] = complex(x_min + i / (width - 1) * (x_max - x_min), y_min + j / (height - 1) * (y_max - y_min))

# Create an array to store the iteration counts
iters = np.zeros((width, height), dtype=np.int32)

# Apply the iterative process and store the iteration counts
z = np.zeros((width, height), dtype=np.complex128)
for n in range(256):
    mask = np.abs(z) <= 2.0
    iters[mask] = n
    z[mask] = z[mask]**2 + c[mask]

# Plot the Mandelbrot set
plt.imshow(iters.T, cmap='jet', extent=(x_min, x_max, y_min, y_max))
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()