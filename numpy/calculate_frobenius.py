import numpy as np
a = np.arange(1, 10).reshape((3, 3))
print("Original array:")
print(a)
print("Frobenius fnorm and the condition number:")
print(np.linalg.norm(a, 'fro'))
print(np.linalg.cond(a, 'fro'))
import numpy as np
a = np.array([[1,2,3],[0,1,4]])
print (a.size)