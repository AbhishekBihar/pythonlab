import numpy as np
f=np.array(['whEre','Are','you','comIng','from'])
print("before performing the oprations")
print(f)
print("after performing the operations")
print(np.char.upper(f))
print(np.char.lower(f))
print(np.char.swapcase(f))
print(np.char.title(f))