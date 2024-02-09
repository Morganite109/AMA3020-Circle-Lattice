import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot_sphere(center, radius):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, color='b', alpha=0.5)

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Set integer ticks for each axis
    ax.set_xticks(np.arange(int(center[0] - radius), int(center[0] + radius) + 1, 1))
    ax.set_yticks(np.arange(int(center[1] - radius), int(center[1] + radius) + 1, 1))
    ax.set_zticks(np.arange(int(center[2] - radius), int(center[2] + radius) + 1, 1))
  # points
    point = (1, 1, 1)  
    ax.scatter(*point, color='r', label='Point')
    point2 = (-1,1,1)
    ax.scatter(*point2, color='r', label='Point')
    point3 = (1,-1,1)
    ax.scatter(*point3, color='r', label='Point')
    point4 = (1,1,-1)
    ax.scatter(*point4, color='r', label='Point')
    point5 = (-1,-1,1)
    ax.scatter(*point5, color='r', label='Point')
    point6 = (-1,1,-1)
    ax.scatter(*point6, color='r', label='Point')
    point7 = (1,-1,-1)
    ax.scatter(*point7, color='r', label='Point')
    point8 = (-1,-1,-1)
    ax.scatter(*point8, color='r', label='Point')
  
    ax.set_title('Sphere')
    plt.savefig('sphere.png')
    plt.savefig('sphere.pdf')

# Example
plot_sphere(center=(0, 0, 0), radius=np.sqrt(3))


