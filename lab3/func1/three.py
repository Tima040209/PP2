def solve(numheads,numlegs):
    x = 2 * numheads
    y = numlegs - x
    print("Rabbits ",y/2)
    print("Chickens ",numheads - y/2)
solve(int(input()),int(input()))