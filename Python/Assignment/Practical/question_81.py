#Write a Python program to write a list to a file.

lst=['php','java','python']

with open("read.txt",'w') as file:
    for item in lst:
        file.write("\n" + item)