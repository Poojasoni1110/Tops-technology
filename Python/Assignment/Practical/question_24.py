# Write a Python function to insert a string in the middle of a string. 
def insert(original,inst):
    mid=len(original)//2
    return original[:mid] + inst + original[mid:]

print(insert("pooja","soni"))