# Write python program that user to enter only odd numbers, else will raise an exception. 
try:
    num=int(input("Enter the only odd number::"))
    if num %2 ==0:
        raise ValueError('This is not odd number')
except ValueError as e:
    print("Error!!",e)
else:
    print("Odd number is::-",num)