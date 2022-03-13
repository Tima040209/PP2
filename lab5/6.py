import re 
txt = input()
pat = re.sub("\s|\.|,",":",txt)
print(pat)