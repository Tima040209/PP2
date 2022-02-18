s = list(map(int, input().split()))
def has_33(x = []):
    cnt = 0
    for i in range(len(s)):
        if x[i] == 3 and x[i+1]==3:
            print(True)
            cnt+=1
            break
    if cnt == 0:
        print(False)
has_33(s)
        