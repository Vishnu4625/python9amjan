# 1.Right angled triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
#2.Inverted right angled triangle
# n=5
# for i in range(n,0,-1):
#     for j in range(1, i+1):
#         print('*',end='')
#     print()
#3.Pyramid star pattern
# n = int(input('Enter a number:'))
# for i in range(1,n+1,2):
#     for j in range((n-i)//2):
#         print(' ',end='')
#     for k in range(i):
#         print('*',end='')
#     print()
#4. Diamond star pattern
# n = int(input('Enter a number:'))
# for i in range(1,n+1,2):
#     for j in range((n-i)//2):
#         print(' ',end='')
#     for k in range(i):
#         print('*',end='')
#     print()
# for i in range(n-2,0,-2):
#     for j in range((n-i)//2):
#         print(' ',end='')
#     for k in range(i-1):
#         print('*',end='')
#     print()
#5. Hollow right angled triangle
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i or i==n:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
#6.inverted hollow triangle
# n=5
# for i in range(n,0,-1):
#     for j in range(1, i+1):
#         if j==1 or j==i or i==n:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
# 7.Floyd’s Triangle Pattern
# n=5
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print(j,end='')
#     print()
# 8.Pascal’s Triangle Pattern
#9. Number pyramid pattern
# n = int(input('Enter a number:'))
# for i in range(1,n+1):
#     print(' ' * (n - i), end='')
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()
# 10.Hollow diamod pattern
n = int(input('Enter a number:'))
if n%2==0:
    n += 1
for i in range(1,n+1,2):
    for j in range((n-i)//2):
        print(' ',end='')
    for k in range(i):
        if k==0 or k==i-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n-2,0,-2):
    for j in range((n-i)//2):
        print(' ',end='')
    for k in range(i):
        if k==0 or k==i-1: 
            print('*',end='')
        else:
            print(' ',end='')
    print()