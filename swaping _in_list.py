n=int(input("Enter the size of list:"))
list=[]

for i in range(n):
    num=int(input())
    list.append(num)

print(list)
inx1=int(input("Enter the index 1:"))   
inx2=int(input("Enter the index 2:"))

tem=list[inx1]   #...storing index no.1 item in tem variable

list[inx1]=list[inx2]
list[inx2]=tem

print(list)


