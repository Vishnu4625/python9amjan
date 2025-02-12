a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=0
class Mathematics:
    def __init__(self):
        pass
    def add(self):
        c=a+b
        print('Sum of numbers',a,'&',b,'is',c)
    def sub(self):
        c=a-b
        print('Substraction of numbers',a,'&',b,'is',c)
    def mul(self):
        c=a*b
        print('Multiplication of numbers',a,'&',b,'is',c)
    def div(self):
        c=a//b
        print('Division of numbers',a,'&',b,'is',c)
d=Mathematics()
d.add()
d.sub()
d.mul()
d.div()