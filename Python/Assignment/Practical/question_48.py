# Write a Python script to sort (ascending and descending) a dictionary by value.
dict1={"Iphone15":85000,"Iphone 16":100000,"Iphone 12":75000}

asce= dict(sorted(dict1.items(), key= lambda item:item[1]))
print("Ascending oreder is::",asce)

desc= dict(sorted(dict1.items(), key=lambda item:item[1], reverse=True))
print("Descending oreder is::",desc)