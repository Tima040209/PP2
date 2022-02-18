def Centi(x):
    return (5 / 9)*(x-32)
nums= list(map(float, input().split()))
for i in nums:
    print(Centi(i),end=" ")
