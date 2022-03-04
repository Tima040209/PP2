N = int(input())
def gen_squares(N):
    for i in range(N):
        yield i**2
print(list(gen_squares))
