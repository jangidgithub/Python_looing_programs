# list=["mango","apple","kiwi","orange"]

# for loop

# for a in list:
#     print(a)

# user difined list 

list=[]
n= int(input("enter the value list :"))
for index in range(0,n):
    elements=input("enter the value:")
    list.append(elements)
print(list)

list2=[]
n= int(input("enter the value list :"))
for index in range(0,n):
    elements=int(input("enter the value:"))
    list2.append(elements)
print(list2)

mixed=list+list2
print(mixed)

# def squre(x):
#     for i in x:
#         print(int(i))

# squre(list)

# while loop 

# i=0
# list=[]
# n= int(input("enter the value list :"))
# while i<n:
#     elements=input("enter the value:")
#     list.append(elements)
#     i += 1
# print(list)

# list inside list program

# list=[["mango","apple"],["kiwi","orange"]]

# for subset in list:
#     for i in subset:
#       print(i)

# print(list[1][0]) 2d list printing one element

# print(type(list))

# a=list(range(0,4))
# print(a)   