import numpy as np

a = np.matrix('0.1 0.82 0.5')
print(a)

a = np.where(a > 0.5, 1, 0)
print(a)