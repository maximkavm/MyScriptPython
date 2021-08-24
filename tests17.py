x=float(input())
y=float(input())
x1=float(input())
y1=float(input())

if (0<x) and (0<y) and  (0<x1) and (0<y1) : 
    print ("YES")
elif (0>x) and (0<y) and (0>x1) and (0<y1):
    print ("YES")
elif (0>x) and (0>y) and (0>x1) and (0>y1):
    print ("YES")
elif (0<x) and (0>y) and (0<x1) and (0>y1):
    print ("YES")
else:
    print ("NO")