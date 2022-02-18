arr = list(map(int, input().split()))
def filter_prime(x):
    cnt = 0
    for i in range(2,x-1):
        if x % i == 0:
            cnt+=1
    if cnt == 0:
        print(x,end = " ")
for i in arr:
    filter_prime(i)
        
    
