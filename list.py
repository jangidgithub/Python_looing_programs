# synatx of list is '[a,b,2,5.4,....]'

# a=[2,5.4,"Rahul"]
# print(type(a[2]))
# print(type(a))

# adding methods

# 1 append()
# 2 insert()
# 3 adding two list use for '+' these operator
# 4 extend method 

# append -----> add by default last at list

# a.append("jangid")
# print(a)

# insert -----> add the item using index value 

# a.insert(2,"mango")
# print(a)

# concardinate(adding two lists)

# b=['grap','kiwi']
# mixed=a+b
# print(mixed)

# extend

# a.extend(b)
# print(a)

# Deleteing methods 

# pop,del,remove 

# in keyword using list 
# n= input("enter item will you check in list :")

# if n in a:
#     print("Yes ! that is present in it")
# else:
#     print("No ! that is not present in it")

#<*********************min or max function*****************************>

# b=[2,3,8,6]   
# print("Minimum number of this list is:",min(b))
# print("Maximum number of this list is:",max(b))

#  <*********************count list inside list*****************************>

a=[2,3,8,6,[3,4,10],[4,9],[2]] 

def count_list(x):
    count=0
    for i in x:
        if type(i)==list:
            count += 1
    return count
print(count_list(a))
 