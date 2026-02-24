list=[]
for i in range(1,11):
    list.append(i)
print("Original list:",list)

# extract first 5 elements

first_five=list[:5]
print("Extracted first 5 elements:",first_five)

last_five=list[5:]
print("Extracted last 5 elements:",last_five)