from math import pi
class Circle:
    def __init__(self):
        self.r=0
        self.area=0
    def take_input(self):
        self.r=int(input('Enter the radius:\n'))
    def find_area(self):
        self.area=pi*self.r**2
    def disp_area(self):
        print(f'circle area = {self.area}')

class Rectangle:
    def __init__(self):
        self.l=0
        self.b=0
        self.area=0
    def take_input(self):
        self.l=int(input('Enter the length:\n'))
        self.b=int(input('Enter the breath:\n'))
    def find_area(self):
        self.area=self.l*self.b
    def disp_area(self):
        print(f'rectangle area = {self.area}')

class Triangle:
    def __init__(self):
        self.h=0
        self.b=0
        self.area=0
    def take_input(self):
        self.h=int(input('Enter the height:\n'))
        self.b=int(input('Enter the base:\n'))
    def find_area(self):
        self.area=(self.h*self.b)/2
    def disp_area(self):
        print(f'triangle area = {self.area}')

def main():
    c=Circle()
    r=Rectangle()
    t=Triangle()

    c.take_input()
    c.find_area()
    c.disp_area()

    r.take_input()
    r.find_area()
    r.disp_area()

    t.take_input()
    t.find_area()
    t.disp_area()

main()