#Write a Python function to check whether a number is in a given range 

def check_range(start,num,end):
    if start<= num <=end:
        return True
    else:
        return False
print(check_range(1,5,10))
print(check_range(2,10,5))