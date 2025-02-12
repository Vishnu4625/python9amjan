# # Divisible by 3 & 5
# num=int(input('Enter an integer number:'))
# if num%3==0 and num%5==0:
#     print('Fizzbuzz')
# elif num%3==0:
#     print('Fizz')
# elif num%5==0:
#     print('Buzz')
# else:
#     print('Not divisible by 3 and 5')
# # Leap Year
# year=int(input('Enter Year:'))
# if year%4==0 or (year%100==0 and year%400==0):
#     print(year,'is Leap Year')
# else:
#     print(year,'Not a leap year')
# # Largest Number
# a=int(input('1st number:'))
# b=int(input('2nd number:'))
# c=int(input('3rd number:'))
# if a>b and a>c:
#     print(a,'is the largest')
# elif b>a and b>c:
#     print(b,'is the largest')
# else:
#     print(c,'is the largest')
#Temperature
celcius = int(input('Enter Temperature in celius:'))
if celcius<10:
    print('Cold')
elif celcius>=10 and celcius<25:
    print('Warm')
elif celcius>=25:
    print('Hot')
else:
    print('Invalid Input')