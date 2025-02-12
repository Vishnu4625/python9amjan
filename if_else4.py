him_Road=int(input("enter himalayan road speed:"))
loc_Road=int(input("enter local road speed:"))
nat_Road=int(input("enter national road speed:"))
avg=(him_Road+loc_Road+nat_Road)/3
print(avg)
if avg>=60:
    print("You are eligible")
else:
    print("You are not eligible")