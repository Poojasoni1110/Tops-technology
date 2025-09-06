# Write a Python program to get the Factorial number of given numbers.

num=int(input("Enter the number::"))
if num<0:
    print("Negative number is not defined")
elif num==0:
    print("Factorial of 0 is 1,please Enter valid number")
else:
    fact = 1
    for i in range(1,num + 1):
        fact*=i
    print(f"factorial of {num} is::",fact)
