#1.Prime No
# first = int(input('Prime number from:'))
# last = int(input('Prime number to:'))
# print('Prime numbers between',first,'to',last,'are:')
# for x in range(first,last):
#    if x>1:
#        for i in range(2,x):
#            if x%i == 0:
#                break
#        else:
#            print(x)
#2.GCD of two numbers
# num1=int(input('enter 1st number:'))
# num2=int(input('enter 2nd number:'))
# gcd=1
# for i in range(1,min(num1,num2)):
#     if num1%i==0 and num2%i==0:
#         gcd=i
#     else:
#         print(end='')
# print('GCD of',num1,'and',num2,'is', gcd)
# #3.Armstrong number
# num=int(input('Enter a number:'))
# num_str=str(num)
# num_len=len(num_str)
# sum=0
# for digit in num_str:
#     sum+=int(digit)**num_len
#     print(sum)
# if sum==num_str:
#     print(num, 'is an Armstrong Number')
# else:
#     print(num,'is not an Armstrong Number')
#4.Reverse Number
# num=int(input('Enter a number:'))
# rev_num=0
# while num!=0:
#     digit=num%10
#     rev_num=rev_num*10+digit
#     num//=10
# print('reverse is',rev_num)
#5.Count Number of Digits
# num=int(input('Enter a number:'))
# count=len(str(abs(num)))
# print('Number of digits in',num,'is',count) 
#6.Fibonacci Series
# num=int(input('Enter a number:'))
# a,b=0,1
# for i in range(num):
#     print(a)
#     a,b=b,a+b
#7.Sum of odd number
# num = int(input('Enter a number:'))
# sum = 0   
# for i in range(1,num+1,2):
#     sum += i
# print('Sum of odd numbers are:',sum)
#8.Find largest and smallest digit
# num = int(input('Enter a number:'))
# digit=[int(digit) for digit in str(num)]
# print('Smallest digit is:',min(digit))
# print('Largest digit is:',max(digit))
#9.Sum of Square of numbers
# num = int(input('Enter a number:'))
# sum = 0
# for i in range(1,num+1):
#     sum += i**2
# print('Square of first',num,'are',sum)
#10.Count vowels in a string
str = input('Enter the String:')
vowels = 'aeiouAEIOU'
count=0
for char in str:
    if char in vowels:
        count += 1
    else:
        print(end='')
print('Number of vowels in string',str,'is',count)