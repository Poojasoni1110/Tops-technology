#Write a Python program to create a dictionary from a string. 
# Note: Track the count of the letters from the string.

string="poojasoni"

dict={}

for char in string:

    #check the char is already exits or not 
    dict[char]=dict.get(char,0)+1
print(dict)