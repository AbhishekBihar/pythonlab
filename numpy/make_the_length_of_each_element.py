import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
c= np.char.center(x, 15, fillchar='_')
l = np.char.ljust(x, 15, fillchar='_')
r = np.char.rjust(x, 15, fillchar='_')
print(c)
print( l)
print(r)