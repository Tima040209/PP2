num = list(map(int,input().split()))
k=0
for i in range(2,num[0]):
        if (num[0] % i == 0):
            k+=1
if (num[0]<=500) and (k==0) and (num[1]%2==0):
        print("Good job!") 
else :
        print("Try next time!")          