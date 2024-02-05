import math

def sphere_volume(radius):
    if radius < 0:
        return "Invalid radius (negative value)"
    else:
        volume = (4 / 3) * math.pi * radius**3
        return volume
