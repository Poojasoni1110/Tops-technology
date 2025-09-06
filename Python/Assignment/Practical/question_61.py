#Write a Python function to calculate the factorial of a number (a nonnegative integer) 

def factorial(n):
    if n<0:
        return "non-negative integer"
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

print(factorial(5))