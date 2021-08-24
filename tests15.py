x=int(input())
y=int(input())
z=int(input())

if (x<=y<=z ): 
    print (x,'\n',y,'\n',z)
elif (y<=x<=z ): 
    print (y,'\n',x,'\n',z)
elif (y<=z<=x): 
    print (y,'\n',z,'\n',x)
elif (z<=x<=y ): 
    print (z,'\n',x,'\n',y)
elif (x<=z<=y): 
    print (x,'\n',z,'\n',y)
elif (z<=y<=x): 
    print (z,'\n',y,'\n',x)
