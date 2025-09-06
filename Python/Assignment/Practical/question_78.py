#  Write a python program to find the longest words. 

text=input("Enter the string::")

word=text.split()
max_length=0
longest=[]

for i in word:
    if len(i)> max_length:
        longest=[i]
    elif len(i)==max_length:
        longest.append(i)
print(longest)
