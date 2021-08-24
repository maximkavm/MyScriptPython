a=15112
b = 0
c = 0
while a >0:
    c=a
    a = a//10
    b += c-a*10
    
print(b)