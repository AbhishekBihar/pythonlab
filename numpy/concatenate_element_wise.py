import numpy as np
a=np.array(['python','mohd'],dtype=np.str)
b=np.array(['program','ahsan'],dtype=np.str)
c=np.char.add(a,b)
print(c)