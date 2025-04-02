from math import pi
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area=0
    @abstractmethod
    def take_input(self):
        pass
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def disp_area(self):
        pass
class Circle:
    def __init__(self):
        self.r=0
        super().__init__()
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
        super().__init__()
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
        super().__init__()
    def take_input(self):
        self.h=int(input('Enter the height:\n'))
        self.b=int(input('Enter the base:\n'))
    def find_area(self):
        self.area=(self.h*self.b)/2
    def disp_area(self):
        print(f'triangle area = {self.area}')

def geometricshape(ref):
    ref.take_input()
    ref.find_area()
    ref.disp_area()

def main():
    c=Circle()
    r=Rectangle()
    t=Triangle()

    geometricshape(c)
    geometricshape(r)
    geometricshape(t)

main()