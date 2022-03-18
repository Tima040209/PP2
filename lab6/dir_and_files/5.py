Mylist = ["one", "two", "three"]
with open("write.txt","w") as f:
    for i in Mylist:
        f.write(i+"\n")
    else:
        print("Written succesfully!")