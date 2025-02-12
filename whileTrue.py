while True:
    print('1.French Burger')
    print('2.Chicken Items')
    print('3.Veg Items')
    print('4.Exit')
    user_in=int(input('Enter Your Choice:'))
    if user_in==1:
        print('French burgers in lesser cost')
    elif user_in==2:
        print('Welcome to chicken items')
    elif user_in==3:
        print('Welcome to veg items')
    elif user_in==4:
        print('Exit')
        break
    else:
        print('invalid output')