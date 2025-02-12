name=input("Enter Name:")
per=int(input("Enter Percentage:"))
if per<35:
    print(name, "Failed")
elif per>=35 and per<50:
    print(name, "C Grade")
elif per>50 and per<90:
    print(name, "B Grade")
elif per<=90 and per>=100:
    print(name, "A Grade")
else:
    print("Invalid Marks")