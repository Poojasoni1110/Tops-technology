#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# take 3 number
num1=int(input("Enter number1::"))
num2=int(input("Enter number2::"))
num3=int(input("Enter number3::"))

#check the two values are equal
if num1==num2 or num2==num3 or num3==num1:
    print("two number are equal sum will be zero")
else:
    sum=num1+num2+num3
    print(sum)