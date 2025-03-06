# # Q1
# val='123 5565 66'
# # op: 6,21,12
# a=val.split()
# for x in a:
#     sum=0
#     for y in x:
#         sum+=int(y)
#     print(sum)

# Q2
# val='abcd def ghi'
# op: a e i

# Q3
# val='rama is going rama'
# # op: 'is going'
# b=[] 
# a=val.split()
# for x in a:
#     if x in b:
#         pass
#     else:
#         b.append(x)
# print(b)
# # print(list(set(b).symmetric_difference(set(c))))
# print(a)
# Q4 0 to 100 without for loop
# use while loop
# Q5
val='rama is going'
# o is coimg stop iteration
# use while loop
i=0
while i<len(val):
    if val[i]=='o':
        break
    else:
        print(val[i])
    i+=1
