nums = list(map(int, input().split())) 
def spy_game(x=[]):
    cnt = 0
    for i in range(len(nums)):
        if x[i]==0 and x[i+1]==0 and x[i+2]==7:
            print(True)
            cnt+=1
            break
    if cnt == 0:
        print(False)   
spy_game(nums)