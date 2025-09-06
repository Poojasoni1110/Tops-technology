#Write a Python function to check whether a number is perfect or not.

def perfect_num(num):
    if num <= 0:
        return False
    
    sum = 0
    for i in range(1, num):
        if num % i == 0:   # check if i is a divisor
            sum += i
    
    return sum == num

print(perfect_num(6))   
print(perfect_num(28))  
print(perfect_num(12))  
