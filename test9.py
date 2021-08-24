x=int(input())
if x%10==0:
   print(x,"studentov")
elif ((x%10)==1 and (x%100)//10<1) or ((x%10)==1 and (x%100)//10>=2):
   print(x,"student")
elif ((x%10)==2 and (x%100)//10<1) or ((x%10)==2 and (x%100)//10>=2):
   print(x,"studenta")
elif ((x%10)==3 and (x%100)//10<1) or ((x%10)==3 and (x%100)//10>=2):
   print(x,"studenta")
elif ((x%10)==4 and (x%100)//10<1) or ((x%10)==4 and (x%100)//10>=2):
   print(x,"studenta")
elif (x%10)+10==11 or (x%10)+10==12 or (x%10)+10==13 or (x%10)+10==14: 
   print(x,"studentov")
elif (x%10)==5 or (x%10)==6 or (x%10)==7 or (x%10)==8 or (x%10)==9:
   print(x,"studentov")
else:
   print("!!!")

