total_name=int(input("enter no of names:"))
list_of_names=[]
for i in range(total_name):
    name=input("Enter the name:")
    list_of_names.append([name])
print("Names given are:",list_of_names)
sorted_name=[x[0] for x in list_of_names]
sorted_name.sort()
for j in sorted_name:
    print(j)
