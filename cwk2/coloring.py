import matplotlib.pyplot as plt
import numpy as np

X = np.random.randint(0, 2, (512, 512))  # sample 2D array
y = np.random.randint(0, 2, (256, 256))
left = np.empty((512, 512))
for i in range(512):
    for j in range(512):
        left[j, i] = X[j, i]
for i in range(256):
    for j in range(256):
        left[j + 128, i + 124] = y[j, i]
right = np.empty((512, 512))
for i in range(512):
    for j in range(512):
        right[j, i] = X[j, i]
for i in range(256):
    for j in range(256):
        right[j + 128, i + 132] = y[j, i]

plt.matshow(left, cmap='gray')
plt.savefig('left.png')
b = plt.matshow(right, cmap='gray')
plt.savefig('right.png')
