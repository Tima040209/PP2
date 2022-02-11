from operator import le
from string import ascii_lowercase, ascii_uppercase
lengh = int(input())
a = []
for i in range(lengh):
    s = input() 
    x = 0
    y = 0
    z = 0  
    for i in s: 
        if i in ascii_uppercase: x+=1
        if i in ascii_lowercase: y+=1
        if i >= '0' and i <='9' :z+=1
    if x>0 and y > 0 and z > 0: a.append(s) 
a=sorted(list(set(a)))    
print(len(a))          
for i in a:
    print(i)
    

   