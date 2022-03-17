 #the = tuple(input())
def Tr(tup):
    for i in tup:
        if i != True:
            return False
    return True 
#if(Tr(the)) : 
 #   print("Yes")
#else :
 #   print("No")
tuple3 = (True, True, True)
tuple2 = (True, False, True)
print(Tr(tuple3))
print(Tr(tuple2))
    
    