# Write a Python program to map two lists into a dictionary.

#for counter import the collections
from collections import Counter

#two list
lst1=["a","b","c","d"]
lst2=[400,400,400,300]

#map two list into dictonary
dict=dict(zip(lst1,lst2))

#print into counter
print(Counter(dict))