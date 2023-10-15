!pip install celluloid
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

# Define the function f(x, t) that changes over time
def f(x, t):
    return (x+t)**2 *0.5 + 2*(np.sin(10*(x-t)))  

# Create the initial plot
x = np.linspace(0, 2 * np.pi, 1000)
fig, ax = plt.subplots()
time_text = ax.text(0.8, 0.9, '', transform=ax.transAxes, fontsize=12, color='red')

camera = Camera(fig)

# Generate animation frames
for t in np.linspace(0, 2 * np.pi, 200):
    y = ax.plot(x, f(x, t))
    # time_text.set_text(f'Time: {t:.2f}')
    plt.legend(y, [f'time {t}'])
    camera.snap()

# Create the animation
animation = camera.animate()

# Show the animation
animation.save('animation.mp4')
