# Write a Python function to get the largest number, smallest num 
# and sum of all from a list.

def lst(list):
    largest=max(list)
    small=min(list)
    total=sum(list)

    print("Largest number:",largest)
    print("smallest number:",small)
    print("total of list:",total)
    
list=[10,20,30,90]
lst(list)