from functools import reduce

def multiply_list(numbers):
    if not numbers:
        return None
    
    result = reduce(lambda x, y: x * y, numbers)
    return result

#Example
numbers = [2, 3, 4, 5]
result = multiply_list(numbers)
print("Result of multiplying all numbers:", result)