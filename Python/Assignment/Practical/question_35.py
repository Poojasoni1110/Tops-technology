'''Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30. '''

list=[x**2 for x in range(1,30)]
result=list[:5] + list[-5:]
print(result)