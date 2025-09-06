# Write python program that swap two number with temp variable and without temp variable. 

num1=int(input("enter num1::"))
num2=int(input("enter num2::"))
print("befor the swap number")
#befor the swap
print("Num1 is:",num1)
print("Num2 is:",num2)
#with the temp variable
temp=num1
num1=num2
num2=temp
#after the swap number
print("after the swap number")
print("Num1 is:",num1)
print("Num2 is:",num2)
print("****************************************")
#swap without temp variable 
a = int(input("Enter A : ")) 
b = int(input("Enter B : ")) 
print("befor the swap number")
print("A is:",a)
print("B is:",b)
b = b + a 
a = b - a 
b = b - a 
print("after the swap number")
print("A is:",a) 
print("B is:",b) 