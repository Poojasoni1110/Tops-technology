#  Write a Python program to append text to a file and display the text. 

with open("read.txt","a") as file:
    file.write("\nPooja soni")

with open("read.txt","r") as file:
    data=file.read()
    print(data)