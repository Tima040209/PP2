"""*def length(nomeOfFile):
        with open(nomeOfFile) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
path = "c:/Users/1/Desktop/pp2/lab6/dir_and_files/four.txt"
print("Number of lines in the file: ",length(path))"""

import os
def length(fname):
    with open(fname) as f:
        for id, item in enumerate(f): 
            print ("id = ",id," value = ",item)
        return id+1
show_cur_dir = os.getcwd()
print(show_cur_dir)
path = "c:/Users/1/Desktop/pp2/lab6/dir_and_files/four.txt"
print("Number of lines in the file: ", length(path))
