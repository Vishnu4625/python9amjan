# val='rama is going'
# print(val.title())
# word=input('enter a word')
# if word==word[::-1]:
#     print(f'{word} is pallindrome')
# else:
#     print('Not a pallindrome')
# val='rama'
# print(val.isalpha())
# print(val.isnumeric())
# val2='123'
# print(val2.isnumeric())
# print(val2.isalnum())

pass1=input('enter your password:')
numeric=[]
alpha=[]
spl=[]
if len(pass1)>=8 and len(pass1)<=13:
    print('password length is valid')
    for x in pass1:
        if x.isalpha():
            alpha.append(x)
        elif x.isnumeric():
            numeric.append(x)
        else:
            spl.append(x)
    if len(alpha)>=4 and len(numeric)>=4 and len(spl)>=1:
        print('password is valid')
    else:
        print('Password is invalid')
else:
    print('password length is invalid')