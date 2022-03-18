import os
print('Exist:', os.access('c:/Users/1/Desktop/pp2/lab6', os.F_OK))
print('Readable:', os.access('c:/Users/1/Desktop/pp2/lab6', os.R_OK))
print('Writable:', os.access('c:/Users/1/Desktop/pp2/lab6', os.W_OK))
print('Executable:', os.access('c:/Users/1/Desktop/pp2/lab6', os.X_OK))