pi=22/7
r=float(input("enter the radius"))
angle=float(input("enter the angle"))
if angle<360:

    aos=((pi*r**2)*(angle/360))
    print(aos)
else:
    print("angle does not exist")