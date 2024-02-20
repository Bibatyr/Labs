def trapezoid_area(base1, base2, height):
    area = 0.5 * (base1 + base2)*height
    return area

#Example:
height = float(input("Height: "))
base1 = float(input("Base1: "))
base2 = float(input("Base2: "))
area = trapezoid_area(base1, base2, height)
print("Expected Output:", area)