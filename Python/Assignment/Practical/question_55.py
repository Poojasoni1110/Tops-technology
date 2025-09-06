# Write a Python script to merge two Python dictionaries.

dict1={"name":"pooja","age":20}
dict2={"course":"data analytics","location":"parimal"}

print("Dict1 is::-",dict1)
print("Dict1 is::-",dict2)
dict3=dict1.copy()
dict3.update(dict2)
print("Dict3 is::-",dict3)
