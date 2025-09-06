# Write a Python program to count the number of lines in a text file. 

count=0
with open("read.txt","r") as file:
    for line in file:
        count+=1
print(count)