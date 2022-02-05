word = input()
x = input()
first = word.find(x)
last = word.rfind(x)
if (first!=last):
 print(first,last)
else:
 print(first)