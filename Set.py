#Set:
# 1. Unordered
# 2. Immutable
# 3. unindexed
# 4. Duplication NOT Allove
# 5. Any datatype
# 5. Mix of different data type

#creating set
name={"aditya","ram","sham"}
print(name)

print(len(name))

print(type(name))

#Accesing of set
for x in name:
    print(x)

# Checking the item is present in set
if "ram" in name:
    print("ram is in the names")

# checking the ites is in the set
if "gita" not in name:
    print("gita is not present in names")

#add items in set
name.add("rohan")
print(name)


#adding the list items in set 
name_list=["pranav","man"]
name.update(name_list)
print(name)

#removing items from set
name.remove("man")
print(name)

#try to remove an item from set which not present in set
name.discard("gita")       #discaed function not give any erreor if value is not present in the set
print(name)

# #joining of two sets
s1={1,2,3,4}
s2={5,6,4}
# print(s1, s2)

s3=s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

# onley dupicate valu to print
s1.intersection_update(s2)   #.... insert_update function does the updation pf dupiicate value in s1 set repleacint the set's items
print(s1)

#Keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)


#example
a=[1,2,3,4,5]
b=[4,5,6,7]
c=[4,5,7,3,6,8,9]
print(a,b,c)
c.append(3)
print(c)

# type cast list to sets
s1=set(a)
s2=set(b)
s3=set(c)
print(s1,s2,s3)

# finding the duplicate values
s1s2=s1.intersection(s2)
final=s1s2.intersection(s3)
print(final)

d=list(final)
print(d)