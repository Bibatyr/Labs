def solve(numheads, numlegs):
    if numheads <= 0 or numlegs <= 0 or numheads > numlegs:
        return "No solution"
    
    num_rabbits = (numlegs - 2*numheads)/2

    num_chickens = numheads - num_rabbits

    if num_rabbits >= 0 and num_chickens >= 0 and num_rabbits.is_integer() and num_chickens.is_integer():
        return int(num_rabbits), int(num_chickens)
    else:
        return "No solution"
