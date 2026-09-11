import os

if os.path.exists("Notes.txt"):
    os.remove("Notes.txt")
    print("THe file has been removed")
else:
    print("The file doesnot exists")