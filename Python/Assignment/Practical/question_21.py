# Write a Python program to add 'in' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, 
# leave it unchanged. 

text=input("Enter the string::")

if len(text)<3:
    str=text
elif text.endswith("ing"):
    str=text + "ly"
else:
    str=text + "ing"

print(str)