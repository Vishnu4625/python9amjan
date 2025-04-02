# try:
#     a=int(input('enter a number:'))
#     b=int(input('enter a number:'))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('Denominator never be zero')
# except ValueError:
#     print('provide numerical')

# mob=input('enter mobile number')
# try:
#     if len(mob)==10:
#         print('valid')
#     else:
#         raise ValueError 
# except Exception as e:
#     print(e)

# Name Error


# def menu(item):
#     try:
#         if item=='pizza':
#             print('Enjoy your pizza')
#         elif item=='idli':
#             print('Enjoy your idli')
#         elif item=='burger':
#             print('Enjoy your burger')
#         else:
#             raise NameError(item,'not defined')
#     except Exception as e:
#         print(e)
#     finally:
#         print('Program execution completed')
# def main():
#     item=input('Enter the item:')
#     menu(item)
# main()

# Finally
def fun(x):
    try:
        res=100/x
        print('inside try')
    except:
        print('inside except')
    else:
        print('inside else')
    finally:
        print('inside finally')
    
def main():
    x=int(input('Enter x:'))
    fun(x)
main()

    
