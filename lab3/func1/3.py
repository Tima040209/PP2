def solve(numheads,numlegs):
    x = 2 * numheads
    y = numlegs - x
    print("Rabbits ",y/2)
    print("Chickens ",numheads - y/2)
numheads = int(input())
numlegs = int(input())
solve(numheads,numlegs)