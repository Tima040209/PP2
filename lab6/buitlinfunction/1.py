nums = list(map(int,input().split()))
def mult_nums(list) :
    int = 1
    for i in list:
        int = int*i
    return int
print(mult_nums(nums))
