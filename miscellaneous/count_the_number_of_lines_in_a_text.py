open_fil=open("apple.txt")
a=open_fil.read()
count=0
s=a.split()
for i in s:
    if i:
        count=count+1
    print(count)
