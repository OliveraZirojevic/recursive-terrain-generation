import numpy as np
import matplotlib.pyplot as plt


noise = np.random.normal(0, 1, 1000)

plt.figure(figsize = (10, 4))
plt.plot(noise)

plt.show()