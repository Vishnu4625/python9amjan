# List
# lst=[]
# print(type(lst))
# lst=[1,2.2,'rama', (1+2j), True]
# print(lst)
# Inbuild functions
# append
# sales = [110,23,55]
# sales.append(69)
# print(sales)
# insert
# sales1 = [110,23,55]
# sales1.insert(0,69)
# print(sales1)
# Extend
# Max
# sales=[110,23,6007,55,1004]
# print(max(sales))
# sales.sort()
# # sales[-1]
# print(sales[-1])
# sales=[110,23,6007,55,1004]
# max_num=0
# for x in sales:
#     if x>max_num:
#         max_num=x
# print(max_num)
# sales=[110,23,6007,55,1004]
# max_num=sales[0]
# for x in sales:
#     if x<max_num:
#         max_num=x
# print(max_num)
# Manual Sort
# val=[1,2,34,5,6,8]
# for x in range(len(val)):
#     for y in range(len(val)):
#         if val[x]<val[y]:
#             val[x],val[y]=val[y],val[x]
#         else:
#             val[x],val[y]=val[x],val[y]
# print(val)
# list comprehention for loop
# val=[1,2,3]
# print([x**3 for x in val])
# list comprehention if condition
# val=[1,2,3,5,7,20]
# #op;[2,20]
# emp_lst=[]
# for x in val:
#     if x%2==0:
#         emp_lst.append(x)
# print(emp_lst)
# even
# print([x for x in val if x%2==0])
# odd
# print([x for x in val if x%2!=0])
# len
# print(len([x for x in val if x%2!=0]))
# addition of numbers
# sum=0
# for x in val:
#     sum+=x
# print(sum)

# id=[1,1,2,3,41,4,3]
# # op:-[1,2,3,41,4]
# emp_lst=[]
# for x in id:
#     if x in emp_lst:
#         pass        
#     else:
#         emp_lst.append(x)
# print(emp_lst)
# Set
# sale1={1,3,5}
# sale2={1,6,7}
# print(sale1.intersection(sale2))#intersection
# print(sale1.union(sale2))#
# a={1,2,3,4}
# b={1,2,3,4}
# c={1,2,3,6,7}
# print((a.intersection(b).intersection(c)))
python={1,2,3,4}
java={1,2,3,4,55}
sql={1,2,3,6,7}
for x in python,java,sql:
    for y in x:
        if y in (python and java) and (sql and python) and (sql and java):
            pass
        else:
            print(y)
