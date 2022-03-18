import os
print("Test a path exists or not:")
path = r'c:/Users/1/Desktop/pp2/lab6'
print(os.path.exists(path))
path = r'c:/Users/1/Desktop/pp2/lab7'
print(os.path.exists(path))
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))