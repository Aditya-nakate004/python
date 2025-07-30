# list=['Apple','Banana','Fig','Gavava','Pineapple']
# print(list)


# print(len(list))

# print(len(list[1]))

list2=[]

for i in range (5):

    x=input(f"Enter the strings{i+1}:")
    list2.append(x)
    
print(list2)
for i in list2:
    length=len(i)
    print(f"length of {i} is :{length}")


