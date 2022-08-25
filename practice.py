# n=[2,3,4]
# for i in n:
#     print(i**2)

# def squre(x):
#     for i in x:
#         print(i)

# squre(n)

# n=list(range(1,4))
# print(n)

# it is very easy programe to create a revers list

# def reverse_list(x):
#     print(n[::-1])

# reverse_list(n)

# reverse list by help of append or pop function
# list=[]
# def reverse_list(x):
#     for i in range(len(x)):
#         a=x.pop()
#         c=list.append(a)
#     return c


# reverse_list(n)
# print(list)


# reverse element list

# words=['abc','kjh']
# a=[]
# def reverse_ele(x):
#         for subset in x:
#            b=a.append(subset[::-1])
#         return b


# reverse_ele(words)
# print(a)

# <*********************practice 3*****************************>

numbers=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
def even_odd(x):
        for subsets in x:
                if subsets%2==0:
                        a=even.append(subsets)
                else:
                        b=odd.append(subsets)
        output=[even,odd]     
        return output

print(even_odd(numbers))

# <*********************practice 4*****************************>

# a=[1,2,3,4]
# b=[2,3,8,6]
# c=[]
# def union(a,b):
#         for subsets in a:
#                 if subsets in b:
#                         d=c.append(subsets)   
#         return d

# union(a,b)
# print(c)



# comprehension

# l=['abc','tuv']

# l2=[subset [::-1] for subset in l]
# print(l2)


# num to string with comprehension 

# list=['true','false',1,2.2,5]
# def sting(list):
#     new_list=[str(item) for item in list if (type(item)==int or type(item)==float)]
#     return new_list

# print(sting(list))

# n=int(input("Enter the number :"))
# for i in range (1,11):
#     print(f"{i}:{i*n}")