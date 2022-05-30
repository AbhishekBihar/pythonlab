def prfct(n):
    sum1=0
    for i in range(1,n):
        if n%i==0:
            sum1+=i
    print(sum1)
    return sum1==n
n=int(input())
out=prfct(n)
print(out)