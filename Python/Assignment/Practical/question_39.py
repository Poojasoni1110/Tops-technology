#  Write a Python program to find the second smallest number in a list.

list=[10,40,78,25]
# print(list)
list.sort()

if len(list)>=2:
    print("Second smallest number is::",list[1])
else:
    print("none")