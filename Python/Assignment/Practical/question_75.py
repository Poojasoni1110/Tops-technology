# Write a Python program to read last n lines of a file. 

n=1
with open("read.txt","r") as file:
    data=file.readlines()
    for i in data[-n:]:
        print(i)