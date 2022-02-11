n = int(input())
def print_matrix(arr):
    for ar in arr:
        for el in ar:
            print(el,end="")
        print()  
arr=[]
if n%2 !=0:
    for i in range(n) :
        arr2 = []
        for j in range(n) :
            if j>= n-i-1: arr2.append("#")
            else: arr2.append(".") 
        arr.append(arr2)    
    print_matrix(arr) 
else:
    for i in range(n) :
        arr2 = []
        for j in range(n) :
            if j<= i: arr2.append("#")
            else: arr2.append(".") 
        arr.append(arr2)    
    print_matrix(arr)       
