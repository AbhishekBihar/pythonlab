def prime(n):
    sum1=0
    for i in range(1,n+1):
        if n%i==0:
            sum1+=1
    print(sum1)
    return sum1==2
n=int(input())
out=prime(n)
print(out)