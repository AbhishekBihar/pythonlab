pi=22/7
diameter = float(input('Diameter of circle: '))
angle = float(input('angle measure: '))
if angle < 360:
    len_arc=((pi*diameter)*(angle/360))
    print(len_arc)
else:
    print("angle is out of the  range")