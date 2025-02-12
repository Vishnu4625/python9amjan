def Book(q):
    if q=='y':
        print('Currently Booking is opened Only for Bangalore to Chennai route and below are the available seats:')
        for x in range(1,3):
            print(x)
        while True:
            print('Select a seat no:')
            seat = int(input())
            if seat==1:
                print('Window Seat Selected')
                break
            elif seat==2:
                print('Side Seat Selected')
                break
            else:
                print('Invalid Input, Print Try Again!!!')
                break
    elif q=='n':
        print('Have a Nice Day!!')
    else:
        print('Try Again with correct input y/n')
q=input('Would you like to book a ticket please enter y/n:')
a=Book(q)

        
