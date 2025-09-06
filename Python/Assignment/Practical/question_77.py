#Write a Python program to read a file line by line store it into a variable.

with open("read.txt","r") as file:
    data=file.read()
    print(data)