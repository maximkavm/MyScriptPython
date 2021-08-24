x=int(input())
if ((x%10)==0) or (5<=(x%10)<=9) or (11<=(x%100)<=14) or (11<=x<=14) :
   print(x,"studentov")
elif ((x%10)==1 and (x%100)//10<1) or ((x%10)==1 and (x%100)//10>=2):
   print(x,"student")
elif (2<=(x%10)<=4 and (x%100)//10<1) or (2<=(x%10)<=4 and (x%100)//10>=2):
   print(x,"studenta")
