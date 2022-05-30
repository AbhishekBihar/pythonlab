a={'a':10,'b':20,'c':30}
b={'a':20,'b':30,'c':40}
c={}
for i,j in a.items():
    for k,l in b.items():
        if i==k:
            c[i]=j+l
print(c)