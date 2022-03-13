import re 
txt = input()
words = re.findall('[A-Z][a-z]*', txt)
print(' '.join((words)))