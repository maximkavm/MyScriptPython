x=int(input())
i=3
fib1=1
fib2=1

if x==0:
    print (0)
elif x==1 or x==2: 
    print (1)
else:
    while i<=x:
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        i=i+1
    print (fib)