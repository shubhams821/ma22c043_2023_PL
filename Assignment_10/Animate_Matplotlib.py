import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function f(x, t) that changes over time
def f(x, t):
    return (x+t)**2 *0.5 + 2*(np.sin(10*(x-t))) # Example function (you can change this)

# Create the initial plot
x = np.linspace(0, 2 * np.pi, 1000)
t = 4

fig, ax = plt.subplots()
line, = ax.plot(x, f(x, t))
time_text = ax.text(0.8, 0.9, '', transform=ax.transAxes, fontsize=12, color='red')


# Function to update the plot with respect to time
def update(t):
    line.set_ydata(f(x, t))
    time_text.set_text(f'Time: {t:.2f}')
    return line, time_text

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 200), blit=True)

# Show the animation
plt.show()
