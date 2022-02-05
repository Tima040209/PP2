x = int(input())
g = input()
if g =='b':
    print(x*1024)
elif g == 'k':
     m = int(input())
     print(f"{(x/1024):.{m}f}")