nums = list(map(int,input().split()))
def histogram( x=[] ):
    for i in range(len(x)):
        print('*'*x[i])
histogram(nums)