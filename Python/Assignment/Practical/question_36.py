'''Write a Python function that takes a list and returns a new list with 
unique elements of the first list. '''

def unique(lst):
    uniq=[]
    for i in lst:
        if i not in uniq:
            uniq.append(i)
    return uniq
    
new_lst=[1,2,3,1,4]
print(unique(new_lst))
    
