unit=int(input("No: of TV manufactured:"))
if unit<10:
    print("Will only get monthly salary")
elif unit>=10 and unit<15:
    print("Salary Is:",unit*100)
elif unit>=15 and unit<30:
    print("Salary Is:",unit*200)
else:
    print("Salary Is:",unit*250)
