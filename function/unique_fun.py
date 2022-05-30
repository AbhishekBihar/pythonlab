def uni_lst(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
l=list(map(int,input('enter a list').split()))
out=uni_lst(l)
print(out)