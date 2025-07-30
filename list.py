list=["apple","Banana","mango"]
#printing list
print(list)

#Accesing by +ve index list data using index num.(0---n)
print(list[2])

#Accesing by -ve index list data using index num.(-1,-2,....)
print(list[-1])

#manipulating the list
list[2]="stobarry"
print(list)

#finding the lengthe of list
print(len(list))

#printing the type of list
print(type(list))

#checking if an item is present in list
if "Banana" in list:
    print("Banana part of list")

#Checking if an item is not present in list
if "mango" not in list:
    print("mango is not present in list")

#Accesing the item from the list
print(list[0:2])
print(list[-3:-1])

#append().......use to insert item at the end of list
#insert().......use index num. to insert item in list
#extend()

#append()
list.append("mango")
print(list)

#inseert    
list.insert(2,"chree")  #2 is the index num. and "chree" is item to insert in list
print(list)

#extend()
#extend is use to extend or list within the list
more_fruits=["gavav","fig"]
list.extend(more_fruits)
print(list)

#remove()........remove sppeecitf items
#pop().........remove items using the index num.../ ...when index is not mantion on pop function it removes last item of list

#remove()
num=[1,2,3,4,5]
num.remove(2)     # 2 is the item name not the index oe len no..
print(num)

#pop()
num.pop(2)  #....removing the 2nd index item of num.
print(num)

num.pop() #.....removing last item of num
print(num)



#sorting the list
#*Ascending
#*Dscending

animals=["lion","tiger","cow","monkey"]
animals.sort()   #....by default it in ACENDING ORDER
print(animals)
animals.sort(reverse=True)    #....DECENDING ORDER
print(animals)

animals.reverse()   #.......REVERSING THE DECENDING ORDERED LIST
print(animals)



#LIST COMPRENCIVE

List=[3,5,6,7,8,9]
print(List)
new_list=[]
#Without list comprensive
for i in List:
    if i>5:
        new_list.append(i)
        print(new_list)

#Nested List
list1=[45,34,[35,23],46,78]   
print(list1)
print(list1[2])
print(list1[2][0])
