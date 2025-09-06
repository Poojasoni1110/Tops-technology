#Write a Python program to read a file line by line and store it into a list.

with open("read.txt","r") as file:
    data=file.readlines()

print(data)