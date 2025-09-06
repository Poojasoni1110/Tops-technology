#Write a Python function that checks whether a passed string is palindrome or not.

def palindrom(s):
    return s== s[::-1]

print(palindrom("pooja"))
print(palindrom("nayan"))