# Write a Python program to get unique values from a list 

#using set()
lst=[11,12,13,11,14,10,12,15,13]
unique= list(set(lst))
print("unique values from list:", unique)

# using Loop
unique_list=[]
for i in lst:
    if i not in unique_list:
        unique_list.append(i)
print("unique values:",unique_list)
