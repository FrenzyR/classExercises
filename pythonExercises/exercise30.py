def circleAreaCalculator(radius):
    return 3.14 * radius ** 2

def cylinderAreaCalculator(height, radius):
    return circleAreaCalculator(radius) * height

print("The area of the circle is " + str(circleAreaCalculator(2)))

print("The area of the cylinder is " + str(cylinderAreaCalculator(2, 3)))