# n = int(input('Enter number of rows:'))
# # No:of rows
# for row in range(n,0,-1):
#     # Spaces
#     for spaces in range(n - row):
#         print(' ', end='')
#     # Columns
#     for col in range(row):
#         print('*', end='')
#     print()

# 2
# n = int(input('Enter number of rows:'))
# n=5
# # No:of rows
# for row in range(0,n+1):
#     # Spaces
#     for spaces in range(n - row):
#         print(' ', end='')
#     # Columns
#     for col in range(row):
#         print('*', end='')
#     print()
#3
# n=5
# for row in range(n):
#     for col in range(row+1):
#         print('*',end='')
#     print()
# for row in range(n):
#     for col in range(n-row):
#         print('*',end='')
#     print()
# 4
# n=7
# for row in range(1, n+1, 2):
#     for spaces in range((n-row)//2):
#         print(' ',end='')
#     for col in range(row):
#         print('*',end='')
#     print()