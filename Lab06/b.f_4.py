import time
import math

def calculate_square_root(number, miliseconds):
    seconds = miliseconds/1000

    time.sleep(seconds)

    square_root = math.sqrt(number)

    print(f"Square root of {number} after {miliseconds} miliseconds is {square_root}")

#Example
number = 25100
delay_miliseconds = 2123

calculate_square_root(number, delay_miliseconds)