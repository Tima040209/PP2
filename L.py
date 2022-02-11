brack =input()
x = [0]
for i in range(len(brack)):
    if x[-1]=='[' and brack[i]==']' : x.pop()
    elif x[-1]=='{' and brack[i]=='}' : x.pop()
    elif x[-1]=='(' and brack[i]==')' : x.pop()
    else: x.append(brack[i])
if x == [0]: print("Yes")
else : print("No")   