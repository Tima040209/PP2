import re 
txt = input()
if re.search('^ab{2,3}$',txt):
    print("Found")
else :
    print("None")
