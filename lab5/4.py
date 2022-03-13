import re 
txt = input()
if re.search('[A-Z][a-z]+$',txt):
    print("Found")
else :
    print("None")
