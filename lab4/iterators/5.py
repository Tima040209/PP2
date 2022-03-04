n = int(input())
def odd(x):
    while x >= 0:
        yield x
        x = x - 1
for x in odd(n):
    print(x)
        
