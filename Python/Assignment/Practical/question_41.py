#  Write a Python program to check whether a list contains a sub list 
'''
lst=[10,20,30,40,50,60]
lst1=[10,20]
if lst1 in lst:
    print("list conatin sublist")
else:
    print("list not contain sublist")
'''

lst = [10, 20, 30, 40, 50, 60]
lst1 = [10, 20]

found = False
n = len(lst1)

for i in range(len(lst) - n + 1):
    if lst[i:i+n] == lst1:
        found = True
        break

if found:
    print("List contains sublist")
else:
    print("List does not contain sublist")
