s = input()
sum = 0
for i in range(0,len(s)):
    x = int(s[i])
    sum+= s*2**(len(s)-1-i)
print (sum)
