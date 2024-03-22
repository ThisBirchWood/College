import matplotlib.pyplot as plt

# Data
vertices = [5, 10, 15, 20, 50, 100, 200, 500, 1000]
densities = [0.05, 0.5, 0.75, 1]

times = [
    [8.15E-05, 1.37E-04, 0.00023302, 0.00021792, 0.00058372, 0.00164186, 0.00583189, 0.02020272, 0.07508275],
    [6.91E-05, 0.00014389, 0.00043884, 0.00029206, 0.0015975, 0.00599917, 0.02250993, 0.16116213, 0.61705025],
    [1.00E-04, 0.00016813, 0.0004353, 0.00037058, 0.00208811, 0.00771736, 0.03165786, 0.24275615, 0.97673828],
    [9.28E-05, 0.0002481, 0.00028535, 0.00059417, 0.00260134, 0.01188141, 0.04310994, 0.31114721, 1.40748295]
]

# Plot each density separately
for i, density in enumerate(densities):
    plt.plot(vertices, times[i], label=f'Density = {density}')

plt.xlabel('Number of Vertices')
plt.ylabel('Time Taken')
plt.title('Time Taken by Prim\'s Algorithm for Different Densities')
plt.legend()
plt.grid(True)
plt.yscale('log')  # Using logarithmic scale for better visualization of the data
plt.show()