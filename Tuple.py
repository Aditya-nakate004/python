#use to store multiple itemsin a value
#properties:
# ordered, immutable, Duplicate allowed, Any datatype,
# mix of different datatype
colors=("red","Yellow","green")
print(colors)

#Creating of one item tuple
fruites=("apple",)   #need to give "," after end of items 
                    #When the "," is not geven at the end of items it consider as the string not tuple
print(fruites)
print(type(fruites))

print(len(colors))

#Accessing of tuples
print(colors[1])        #..using of the index numbers
print(colors[-1])       #..using of negative index
print(colors[1:3])



#checking if item is presint in tuple
if "red" in colors:
    print("red color is present in the tuples")
else:
    print("this color is not present in tuple")

#checking if item is not present in tuple
if "voilet"  not in colors:
    print("this color is not present in tuple")


#traverse the tuple
for i in colors:
    print(i)

#concanite two tuples
more_color=("blue","Orange")
new_colors=more_color+colors
print(new_colors)

#unpacking the tuples
color1, color2, color3=colors
print(color1, color2, color3)

#reverse tuple

new_tuple=(1,2,3,4,5,6)
list=[]
for x in reversed(new_tuple):
    list.append(x)

print(list)
output_tuple=tuple(list)
print(output_tuple)

