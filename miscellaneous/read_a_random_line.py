import random
file=open("apple.txt")
a=file.read().splitlines()
print(a)
b=random.choices(a)
print(b)