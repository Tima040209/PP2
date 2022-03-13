import re 
txt = input()
if re.search('^[a-z]+_[a-z]+$',txt):
    print("Found")
else :
    print("None")
