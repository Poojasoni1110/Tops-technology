#Write a Python program to read an entire text file.
with open("read.txt", "r") as file:
    content = file.read()
    print(content)

