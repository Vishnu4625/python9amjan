total_Classes=200
no_Class=int(input("Enter No: of classes attended:"))
per=(no_Class/total_Classes)*100
print("Your percentage is:")
print(per)
if per>=75:
    print("Student is eligible")
else:
    print("Student is not eligible")