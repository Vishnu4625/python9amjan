def add():
    a,b=10,20
    c=a+b
    print(c)
    def sub():
        d=a-b
        print(d)
    return sub

a=add()
a() 