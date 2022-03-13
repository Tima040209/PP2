import re 
txt = input()
if re.search('^ab*$',txt):
    print("Found")
else :
    print("None")
