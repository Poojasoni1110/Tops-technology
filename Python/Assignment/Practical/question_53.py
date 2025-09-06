''' Write a Python script to print a dictionary where the keys are 
numbers between 1 and 15.''' 

dict1={}
for i in range(1,16):
    if i%2==0:
       dict1[i]="Even number"
    else:
        dict1[i]="Odd number"
print(dict1)


