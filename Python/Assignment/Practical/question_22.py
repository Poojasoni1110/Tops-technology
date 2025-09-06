# Write a Python function to reverses a string if its length is a multiple 
# of 4. 

text=input("Enter the string::")

#check if the number is divided by 4 or not
if len(text)%4==0:
    str=text[::-1]
else:
    str=text
print(str)