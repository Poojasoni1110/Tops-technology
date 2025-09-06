# Write a Python program to find the highest 3 values in a dictionary

dict={"maths":90,"science":75,"SS":80,"hindi":96,"gujrati":92}

#store the top 3 values 
top=[]

for values in dict.values():
    top.append(values)

    #list only top 3 values
    top=sorted(top,reverse=True)[:3]
    
print(top)