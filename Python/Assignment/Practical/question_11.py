#Write a Python program to test whether a passed letter is a vowel or not.
 
char = input("Enter the character::")
if len(char)!=1 or not  char.isalpha():
    print("Please enter the single alphabet and Digit is not valid")
elif char.lower() in 'aeiou':
    print(f"{char} is a vowel")
else:
    print(f"{char} is not a vowel")
