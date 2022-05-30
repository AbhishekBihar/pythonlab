import random
import string
a=random.choice(string.ascii_letters)
print(a)
b=int(input("enter the limit"))

str=''
a=random.randint(1,b)
for i in range(a):
    str=str+random.choice(string.ascii_letters)
print(str)