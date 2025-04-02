lst=[1,2,3,5]

for x in lst:
    if x%2==1:
        print(x)
    else:
        pass

print([x for x in lst if x%2==1])

k=list(filter((lambda x:x%2==1),lst))
print(k)

print(sum(lst))

from functools import reduce
k=reduce((lambda x,y:x+y),lst)
print(k)