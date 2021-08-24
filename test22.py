x=int(input())
i=3
fib1=1
fib2=1
fib=0
if x==0:
    print (0)
elif x==1 : 
    print (1)
else:
    while (fib<=x) :
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        i=i+1
        
if fib==x:
      print (i)
else:
    print ("no")
 