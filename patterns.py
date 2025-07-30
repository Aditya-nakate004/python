# #printing patterns in rows and collumns
# # n is no. of rows & 5 for collumns
# n= int(input("enter the num:"))
# for x in range(n):
#     print("*"*5)

# #

# for x in range(n):#loop for rows
#     for i in range (1,n+1):#loop for collumns
#         print(i, end="")
#     print()#print satatement for next row

#
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        
        print(j, end="")
    print()