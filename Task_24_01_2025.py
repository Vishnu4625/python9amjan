#1.Company Tax
#q1=int(input('Enter 1st Quarter amount:'))
#q2=int(input('Enter 2nd Quarter amount:'))
#q3=int(input('Enter 3rd Quarter amount:'))
#q4=int(input('Enter 4th Quarter amount:'))
#sum = q1+q2+q3+q4
#print('Sum of all quarters is',sum)
#if sum>=1000000 and sum<2000000:
#    print('GST is 18%',(sum*18)/100)
#elif sum>=2000000 and sum<4000000:
#    print('GST is 25%',(sum*25)/100)
#elif sum>=4000000:
#    print('GST is 30%',(sum*30)/100)
#else:
#    print('Enter correct quarter amounts')
#2.Odd or Even
#for x in range(10):
#    if x%2==0:
#        print(x,'is even number')
#    else:
#        print(x,'is odd number')
#3.Prime No
first = int(input('Prime number from:'))
last = int(input('Prime number to:'))
print('Prime numbers between',first,'to',last,'are:')
for x in range(first,last):
   if x>1:
       for i in range(2,x):
           if x%i == 0:
               break
       else:
           print(x)
#4.Leap Year
# year = int(input('Enter a year:'))

# if (year % 4 == 0):
#     print(year,'is a leap year.')
# else:
#     print(year,'is not a leap year.')