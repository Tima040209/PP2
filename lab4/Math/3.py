import math
sides = int(input("sides :"))
length = float(input("length :"))
S = sides * (length**2)/(4*math.tan(math.pi/sides))
print("area :",S)
