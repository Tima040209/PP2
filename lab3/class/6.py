#Write a program which can filter prime numbers in a list by using filter function. 
# Note: Use lambda to define anonymous functions.
nums= list(map(int, input().split()))
prime = list(filter(lambda x:all( x % y != 0 for y in range(2,x)), nums))
print (prime)
