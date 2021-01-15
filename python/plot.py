import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random as r, os, numpy
import data 
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
price = data.data()
# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))
    ys.append(float(price.getPrice()))
    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys, label='LTP')
    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('LTP Over LTT')
    plt.ylabel('LTP')
    plt.xlabel('LTT')
    plt.legend()

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
