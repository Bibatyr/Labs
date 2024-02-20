import math

def degree_to_radian(n):
    radians = n * (math.pi / 180)
    return radians

#Example:
n = float(input("Input degree: "))
radians = degree_to_radian(n)
print("Output radian:", radians)