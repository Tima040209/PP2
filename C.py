def print_matrix(arr):
    for ar in arr:
        for el in ar:
            print(el,end=" ")
        print()     
n = int(input())
arr=[]
for i in range(n) :
    arr2 = []

    for j in range(n) :
        if j==i: arr2.append(j*i)
        elif j == 0: arr2.append(i)
        elif i == 0: arr2.append(j)
        else: arr2.append(0) 
    arr.append(arr2)    
print_matrix(arr)        
