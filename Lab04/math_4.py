def parallelogram_area(n, k):
    area = n * k
    return area

#Example:
base = int(input("Length of base: "))
height = int(input("Height of parallelogram: "))
area = parallelogram_area(base, height)
print("Expected output:", area)