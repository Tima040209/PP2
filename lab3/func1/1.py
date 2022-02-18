def Ounces(x):
    return x*28.3495231
nums= list(map(int, input().split()))
ounc = list()
for i in nums:
    ounc.append(Ounces(i))
for i in ounc:
    print(i, end=" ")    


    