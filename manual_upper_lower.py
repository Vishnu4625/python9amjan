# val='rama'
# val2='VISHNU'
# for x in val:
#     # print(f'ASCII value of {x} is {ord(x)}')
#     ord_val=ord(x)
#     print(chr(ord_val-32))
# for y in val2:
#     ord_val1=ord(y)
#     print(chr(ord_val1+32))
val='dDRc'
# print(val.swapcase())
for x in val:
    ord_val=ord(x)
    if ord_val in range(65,90):
        ord_val+=32
        print(chr(ord_val),end='')
    else:
        ord_val-=32
        print(chr(ord_val),end='')