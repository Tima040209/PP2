import re 
txt = input()
if re.search('^a.*b$',txt):
    print("Found")
else :
    print("None")