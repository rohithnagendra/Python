import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
## the plot function have the nessecary atrribute for plotting
plt.plot(x, y, marker='x',linestyle='--',color='g',label='y = x^2')

plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()


categories = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(categories, values, color=['red', 'green', 'blue', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")
plt.show()

import numpy as np
##decides drawing of a line
x = np.linspace(0, 10, 100)
##trignometry function sin(x)
y = np.sin(x)

plt.plot(x, y, linestyle='--',color='r',label='Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.title("Line Plot Example")
plt.grid()
plt.show()


x = np.random.rand(50)
y = np.random.rand(50)
##                color      size            outline                       
plt.scatter(x, y, c='blue' , alpha=0.5, edgecolors='black')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title("Scatter PLot Example")
plt.show()
