import random
import string
a=int(input("enter the length of the string:"))
res = ''.join(random.choices(string.ascii_letters, k=a))
print("Random string : ",res)