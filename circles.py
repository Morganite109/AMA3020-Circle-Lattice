import matplotlib.pyplot as plt
import numpy as np

def plot_circle(r, color='blue'):
    x = np.linspace(-r, r, 1000)
    y_positive = np.sqrt(r**2 - x**2)
    y_negative = -np.sqrt(r**2 - x**2)

    plt.plot(x, y_positive, label='Circle', color=color)
    plt.plot(x, y_negative, label='Circle', color=color)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Circles with 16 lattice points with radius <10')
   
    plt.xticks(np.arange(-10, r+1, step=1))  # Set ticks for natural numbers on x-axis
    plt.yticks(np.arange(-10, r+1, step=1))  # Set ticks for natural numbers on y-axis
   
    plt.grid(True)
    plt.scatter(0, 0, color='black', label='Origin (0, 0)')
    
    plt.savefig('circle.pdf')

# Example
plot_circle(np.sqrt(65),color='blue')
plot_circle(np.sqrt(85),color='red')
plt.axis([-10,10,-10,10])  
plt.axis('equal')
points65 = [
  (1,8),
  (8,1),
  (1,-8),
  (8,-1),
  (-1,8),
  (-8,1),
  (-1,-8),
  (-8,-1),
  (4,7),
  (7,4),
  (4,-7),
  (7,-4),
  (-4,7),
  (-7,4),
  (-4,-7),
  (-7,-4),
]
  
points85= [ 
  (2,9),
  (9,2),
  (2,-9),
  (9,-2),
  (-2,9),
  (-9,2),
  (-2,-9),
  (-9,-2),
  (6,7),
  (7,6),
  (6,-7),
  (7,-6),
  (-6,7),
  (-7,6),
  (-6,-7),
  (-7,-6),
]

# Unzip the points into separate lists of x and y coordinates
x_coords65, y_coords65 = zip(*points65)
plt.scatter(x_coords65, y_coords65, color='black',marker='x')

x_coords85, y_coords85 = zip(*points85)
plt.scatter(x_coords85, y_coords85, color='black',marker='x')

plt.savefig('16pts.png')
plt.savefig('16pts.pdf')
