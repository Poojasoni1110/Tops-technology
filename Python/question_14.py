# Write a python program to sum of the first n positive integers. 

num=input("Enter the number::")
if int(num)> 0 and num.isdigit():
    num=int(num)
    
    total=num*(num+1)//2
    print(f"sum of {num} is::",total)
else:
    print("Enter the valid input")