#from graph import *
import math
a=3
b=1
m=8
c=a/b
i=0
X=0

while i in range(10):
    X=(a*X+b)%m
    print(X)
    i+=1

#print("{:4}{:4}{:4}".format(a,b,c))
#print (math.sqrt(a))
#print ("с = {:8.1f}".format(c))
