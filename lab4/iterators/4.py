n = int(input())
m = int(input())
def gen_even(x,y):
    while x <= y:
        yield x*x
        x+=1

for x in gen_even(n,m):
    print(x)
