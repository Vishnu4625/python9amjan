# for row in range(5):
#     for col in range(row+1):
#         print('*', end='')
#     print()
# print()
for row in range(5):
    for col in range(5-row):
        print('*', end='')
    print()