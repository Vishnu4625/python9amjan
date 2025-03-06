# class plane:
#     def fly(self):
#         print('plane is flying')
#     def land(self):
#         print('plane is landing')
# class passenger_plane(plane):
#     def carry_passengers(self):
#         print('passenger plane is carrying passenders')
# class cargo_plane(plane):
#     def carry_goods(self):
#         print('cargo plane is carrying goods')
# class fighter_jet(plane):
#     def carry_weapons(self):
#         print('fighter jet is carrying weaponss')
# p1=passenger_plane()
# p1.carry_passengers()
# p1.fly()
# p1.land()
# c1=cargo_plane()
# c1.carry_goods()
# c1.fly()
# c1.land()
# f1=fighter_jet()
# f1.carry_weapons()
# f1.fly()
# f1.land()

# 2nd example
# class animal:
#     def sleep(self):
#         print('animal is sleeping')
# class cow(animal):
#     def eat_grass(self):
#         print('cow will eat grass')
# class tiger(animal):
#     def eat_meat(self):
#         print('tiger will eat meat')
# c1=cow()
# c1.eat_grass()
# c1.sleep()
# t1=tiger()
# t1.eat_meat()
# t1.sleep()

# overridding

class show:
    def add(self):
        a,b =10,20
        c=a+b
        print(c)
class demo(show):
    def add(self):
        a,b = 100,30
        c=a+b
        print(c)
d1=demo()
d1.add()