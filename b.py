"""s=str(input())
x = 0
cnt = 0
def my_func(int):
   global x
   x = x + int
   print(x)
   x=-1
for i in s:
    x=+1
    my_func(ord(s[x]))
print(x)
if x >= 300:
    print("It is tasty!")
else:
    print("Oh, no!")"""
n = input()
sum = 0
for i in n:
    sum+=(ord(i))
if sum>=300:
    print("It is tasty!")
else:
    print("Oh, no!")