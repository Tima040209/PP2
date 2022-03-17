word = input()
def Palin(txt):
    cnt = -1
    cnt2  = 0
    for i in txt:
        if txt[cnt2]!=txt[cnt]:
            return False
        else:
            cnt = cnt-1
            cnt2 = cnt2+1
    return True
if Palin(word) == True: 
    print("Yes")
else: 
    print("No")
        