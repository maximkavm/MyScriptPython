x=int(input())
y=int(input())
if (1<y<8) and (1<x<8):
    print (8)
elif (x==1 or x==8) and (y==1 or y==8):
    print (3)
elif ((x==1 or x==8) and (1<y<8)) or ((y==1 or y==8) and (1<x<8)):
    print (5)
