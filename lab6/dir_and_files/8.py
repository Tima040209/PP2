import os
path = "c:/Users/1/Desktop/pp2/lab6/dir_and_files/file.doc"
#path = "delete_dir/delete_dir"
if os.path.exists(path):
    if os.path.isdir(path):
        os.rmdir(path)
    else:
        os.remove(path)
    print ("Deleting was succesfully finished")
else:
    print("The file does not exist")
