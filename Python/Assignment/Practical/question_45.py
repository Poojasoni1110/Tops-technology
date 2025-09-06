#  Write a Python program to unzip a list of tuples into individual lists. 

#Create the list into tuple
list_tuple=[(10,20),(30,40)]

#create two different list and "*" operator is used for unpacking list of tuples
list1,list2=zip(*list_tuple)

#convert into list
print("Convert into list1::",list(list1))
print("Convert into list2::",list(list2))