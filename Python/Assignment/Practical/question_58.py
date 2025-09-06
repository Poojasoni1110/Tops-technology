'''Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output: 
• Counter ({'item1': 1150, 'item2': 300}) '''

from collections import Counter
Sample_data= [
    {'item': 'item1', 'amount': 400}, 
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
] 

#store the value in counter
dict=Counter()
# print(Sample_data)

for i in Sample_data:
    dict[i['item']] += i['amount']

print(dict)