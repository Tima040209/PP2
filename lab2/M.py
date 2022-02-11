
z = []
while len(z) > 2:
    dat = input()
    dat = dat.split()
    z.append((dat[0],dat[1],dat[2]))
z.reverse()
z.sort()
sec = []
for i in z:
    sec.append((i[2],i[1],i[0])) 
for i in sec:
    print(i)       