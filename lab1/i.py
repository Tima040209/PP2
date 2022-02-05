n = int(input())
for i in range(0,n):
    x = input()
    if (x.find("@gmail.com")!=-1):
        print(x.replace("@gmail.com",""))