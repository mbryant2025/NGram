data = []

import matplotlib.pyplot as plt

for i in range(11):
    data.append(0)

for i in range(-99, 100):
    data.append(-i / (100**2-i**2)**0.5)

for i in range(10):
    data.append(0)

#Normalize to [-1, 1]
data = [x / 7.017923929582525 for x in data]

print(len(data))

print(data)

plt.plot(data)

plt.show()

