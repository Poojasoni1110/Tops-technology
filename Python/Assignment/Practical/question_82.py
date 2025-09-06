# Write a Python program to copy the contents of a file to another file. 

with open("read.txt","r") as file:
    data=file.read()

with open("file1.txt","w") as file:
    file.write(data)


