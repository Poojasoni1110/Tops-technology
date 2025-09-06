# Write a Python program to count the occurrences of each word in a given sentence.

text=input("Enter the string::")


#convert the string into lowercase because of the case sensitive language
lower=text.lower()

#split the string into words
split=lower.split()
# print(split)

#create the dictionary to store the words
word_count={}

#count the words
for word in split:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

#print the words occurrence
for word,count in word_count.items():
    print(word,count)