#Line Graph showing Temperature Readings Over a Week

import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [20, 22, 19, 23, 21, 24, 20]

# Plot
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.title('Temperature Readings Over a Week')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()
