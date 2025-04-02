# lst=[10,20,30,40]
# def get_sum():
#     sum=0
#     for x in lst:
#         sum+=x
#     print(sum)
# get_sum()

# def get_prod():
#     prod=1
#     for x in lst:
#         prod*=x
#     print(prod)
# get_prod()

# def login(ref):
#     def wrapper(user,pass1):
#         if user=='vishnu' and pass1==12345:
#             ref(user,pass1)
#         else:
#             print('Please login with correct username and password')
#     return wrapper
# @ login
# def pay_gate_way(user,pass1):
#         print('Login Successfull and you are in Payment gateway page')
# pay_gate_way('vishnu',12345)
# pay_gate_way('yuva',12345)

import copy
# Shallow Copy
# lst1=[[10,20],[30,40]]
# lst2=copy.copy(lst1)
# print(lst1)
# print(lst2)
# print(lst1 is lst2)
# lst1.append([50,60])
# print(lst1)
# print(lst2)
# lst1[1][0]=300
# print(lst1)
# print(lst2)

# Deep Copy
# lst1=[[10,20],[30,40]]
# lst2= copy.deepcopy(lst1)
# print(lst1)
# print(lst2)
# print(lst1 is lst2)
# lst1.append([50,60])
# print(lst1)
# print(lst2)
# lst1[1][0]=300
# print(lst1)
# print(lst2)

# val1=[10,20,2,3,4]
# val1.sort()
# print(val1[0])
# print(val1[-1])

atom=[1,4,66,7,88]
atom.sort()
print(atom[0]+atom[-1])