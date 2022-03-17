from time import sleep
import math
def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
z = int(input())
y = int(input())
print("Square root after specific miliseconds:",delay(lambda x: math.sqrt(x), y, z) ) 
