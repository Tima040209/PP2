len= int(input())
nums= list(map(int, input().split()))
nums.sort()
print(int(nums[-1]) * int(nums[-2]))