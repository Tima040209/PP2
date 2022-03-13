import re
txt = input()
x = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', txt)
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', x).lower())