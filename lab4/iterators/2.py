n = int(input())
def gen_even(x):
    for i in range(x):
        if i % 2==0:
            yield i 
print(list(gen_even(n)))            