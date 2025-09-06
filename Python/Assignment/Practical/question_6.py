#Write a Python program to get the Fibonacci series of given range.
#  
# Define the range
start = 10
end = 100

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Generate Fibonacci numbers in range
while a <= end:
    if a >= start:
        print(a, end=" ")
    a, b = b, a + b
