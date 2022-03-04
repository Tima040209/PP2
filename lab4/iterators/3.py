n = int(input())
def gen_even(x):
    for i in range(x):
        if i % 3==0 and i % 4 == 0:
            yield i 
print(list(gen_even(n))) 