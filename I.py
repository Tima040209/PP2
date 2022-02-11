n = int(input())
disks = []
cnt = 0
for i in range(n):
    oper = input().split()
    if oper[0]=="1": disks.append(oper[1])
    else:cnt+=1
for i in range(cnt): 
    print(disks[i],end=' ')    
