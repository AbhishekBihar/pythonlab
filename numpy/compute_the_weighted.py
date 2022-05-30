import numpy as np
a = np.arange(9).reshape((3,3))
print("Original flattened array:")
print(a)
print("Weighted average along the specified axis of the above flattened array:")
print(np.average(a, axis=1, weights=[1./4, 2./4, 2./4]))