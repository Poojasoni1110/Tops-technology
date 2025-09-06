#Write a Python script to concatenate following dictionaries to create a new one.

dict1={"name":"pooja","surname":"soni"}
dict2={"age":20,"course":"BCA"}

dict3={}
for i in (dict1,dict2):
    dict3.update(i)

print(dict3)