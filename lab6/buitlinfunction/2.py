str = input()
def Uppers(word):
    cnt = 0
    for i in range(len(word)):
        if word[i]>='A'and word[i]<='Z':
            cnt=cnt+1
    return cnt
print(Uppers(str)) 