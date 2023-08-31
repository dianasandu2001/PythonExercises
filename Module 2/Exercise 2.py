import math

radius = float(input("Enter a radius of a circle here."))
area = float(math.pi) * radius * radius
print(f"The area of your circle is = {area: .3f}")

#I originally tried this deffinition for the area and it didn't work
#area = float(math.pi) * math.sqrt(radius)