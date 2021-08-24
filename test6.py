k=int(input())
i=0
g=0
t=0
while t<k:
    if i%2==1: 
        g=g+i
        t=t+1
    i=i+1

print(g)