def pt(x):
    t,y=[1],[0]
    for i in range(x):
        print(t)
        t=[l+r for l,r in zip(y+t,t+y)]
    
pt(7)