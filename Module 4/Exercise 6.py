import random
import math

pi = math.pi

# Area of a circle is πr^2 and the radius is 1
circle_area = pi
# Since the radius of the circle is 1, the lengths of the square will be 2, making the area 2*2=4
square_area = 4
n = 0

generated_points_input = int(input("Enter the amount of points that should be generated: "))
N = 0

while N < generated_points_input:
    generated_points = random.uniform(0, 4)
    N += 1

    if generated_points <= pi:
        n += 1

print("The approximated value of pi is", 4*n/generated_points_input)
