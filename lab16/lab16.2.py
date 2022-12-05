import numpy as np
import matplotlib.pyplot as plt

f = open('numbers.txt', 'r')
num = f.read().split(',')
num = np.sort(num)

arr = np.array([num])

unique, counts = np.unique (arr, return_counts= True)

plt.bar(unique, counts)
plt.show()