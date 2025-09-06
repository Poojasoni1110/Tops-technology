# Write a Python program to count the frequency of words in a file.  

with open("read.txt","r") as file:
    read=file.read().lower()

word=read.split()
freq={}

for words in word:
    if words in freq:
        freq[words]+=1
    else:
        freq[words]= 1 
for words,count in freq.items():
    print(words,count)