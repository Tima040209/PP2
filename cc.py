s = input()
def lowercase(l):
    if l >= 'a' and l <='z':
        print(l,end="")
    elif l>='A' and l <= 'Z':
        print(chr(ord(l) + 32),end="") 
    else:
        print(l,end="")       
for i in s:
    lowercase(i)        
      
