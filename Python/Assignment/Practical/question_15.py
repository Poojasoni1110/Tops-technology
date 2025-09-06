#Write a Python program to calculate the length of a string.

# str="hello world"
str=input("Enter the string::")

#remove the space 
if str.replace(" ","").isalpha():
    print("Length of string is::",len(str))
else:
    print("Enter the only string not a digit ")