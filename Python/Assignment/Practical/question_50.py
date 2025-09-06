#  Write a Python script to check if a given key already exists in a dictionary.

dict1={"abc":10,"xyz":20,"pqr":30}

key=input("Enter the key:")
if key in dict1:
    print(f"{key} is exits in dictonary")
else:
    print(f"{key} does not exits in dictonary")